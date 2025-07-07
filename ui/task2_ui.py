import os
import json
import streamlit as st
from pyvis.network import Network
from neo4j import GraphDatabase
from config import settings
import streamlit.components.v1 as components


def fetch_graph_data(selected_nodes=None, relation_types=("CONTAINS", "RELATED_TO")):
    """ Fetch nodes and edges from the Neo4j graph database (full graph or selected subgraph) """
    driver = GraphDatabase.driver(
        settings.NEO4J_URI,
        auth=(settings.NEO4J_USERNAME, settings.NEO4J_PASSWORD)
    )

    nodes = {}
    edges = set()

    with driver.session() as session:
        if selected_nodes:
            query = """
            MATCH (start)
            WHERE start.name IN $selected
            CALL {
                WITH start
                MATCH path = (start)-[r*1..]->(end)
                WHERE ALL(rel IN r WHERE type(rel) IN $types)
                RETURN path
            }
            RETURN path
            """
            result = session.run(query, selected=selected_nodes, types=relation_types)

            for record in result:
                path = record["path"]
                for node in path.nodes:
                    node_id = str(node.id)
                    if node_id not in nodes:
                        nodes[node_id] = {
                            "id": node_id,
                            "label": node.get("name", f"Unnamed-{node_id}"),
                            "title": str(dict(node)),
                            "props": dict(node)
                        }
                for rel in path.relationships:
                    src = str(rel.start_node.id)
                    tgt = str(rel.end_node.id)
                    rel_type = rel.type
                    edges.add((src, tgt, rel_type))
        else:
            query = """
            MATCH (n)-[r]->(m)
            WHERE type(r) IN $types
            RETURN id(n) AS src_id, id(m) AS tgt_id,
                   properties(n) AS src_props, properties(m) AS tgt_props,
                   type(r) AS rel_type
            """
            result = session.run(query, types=relation_types)

            for record in result:
                src = str(record["src_id"])
                tgt = str(record["tgt_id"])
                rel_type = record["rel_type"]

                if src not in nodes:
                    nodes[src] = {
                        "id": src,
                        "label": record["src_props"].get("name", f"Unnamed-{src}"),
                        "title": str(record["src_props"]),
                        "props": record["src_props"]
                    }
                if tgt not in nodes:
                    nodes[tgt] = {
                        "id": tgt,
                        "label": record["tgt_props"].get("name", f"Unnamed-{tgt}"),
                        "title": str(record["tgt_props"]),
                        "props": record["tgt_props"]
                    }
                edges.add((src, tgt, rel_type))

    driver.close()
    return list(nodes.values()), list(edges)


def fetch_all_node_names():
    """ Fetch all unique node names from the Neo4j database for dropdown selection."""
    driver = GraphDatabase.driver(
        settings.NEO4J_URI,
        auth=(settings.NEO4J_USERNAME, settings.NEO4J_PASSWORD)
    )
    with driver.session() as session:
        result = session.run("MATCH (n) RETURN DISTINCT n.name AS name ORDER BY name")
        names = [record["name"] for record in result]
    driver.close()
    return names

def visualize_with_pyvis(nodes, edges):
    """ Create an interactive graph visualization using Pyvis and save it as HTML. """
    net = Network(height="750px", width="100%", directed=True, notebook=False)
    net.barnes_hut()

    for node in nodes:
        net.add_node(node["id"], label=node["label"], title=node["title"], color="#f39c12")

    for src, tgt, rel_type in edges:
        color = "#3498db" if rel_type == "CONTAINS" else "#2ecc71"
        net.add_edge(src, tgt, title=rel_type, color=color)

    net.set_options("""
    var options = {
      "nodes": {
        "font": {
          "size": 18
        }
      },
      "edges": {
        "arrows": {
          "to": {
            "enabled": true
          }
        },
        "smooth": {
          "type": "cubicBezier",
          "forceDirection": "horizontal",
          "roundness": 0.4
        }
      },
      "physics": {
        "barnesHut": {
          "gravitationalConstant": -12000,
          "centralGravity": 0.3,
          "springLength": 110
        },
        "minVelocity": 0.75
      }
    }
    """)

    net.save_graph("task2_graph.html")
    return "task2_graph.html"


def render():
    """ Render the Task 2 UI for knowledge graph visualization and semantic linking. """
    st.title("Knowledge Graph and Semantic Linking")

    all_nodes = fetch_all_node_names()
    selected = st.multiselect("Select start node(s)", all_nodes)

    show_contains = st.checkbox("Show CONTAINS", value=True)
    show_related_to = st.checkbox("Show RELATED_TO", value=True)

    rel_types = []
    if show_contains:
        rel_types.append("CONTAINS")
    if show_related_to:
        rel_types.append("RELATED_TO")

    if not rel_types:
        st.warning("Please select at least one relationship type.")
        return

    with st.expander("🔍 Show / Hide Graph Visualization", expanded=True):
        if st.button("Visualize Selected Subgraph"):
            if not selected:
                st.warning("Select one or more nodes to begin.")
                return
            with st.spinner("Loading subgraph..."):
                nodes, edges = fetch_graph_data(selected_nodes=selected, relation_types=rel_types)
                if not nodes:
                    st.warning("No nodes/relationships found.")
                    return
                st.success(f"Loaded {len(nodes)} nodes and {len(edges)} relationships.")
                html_path = visualize_with_pyvis(nodes, edges)
                with open(html_path, "r", encoding="utf-8") as f:
                    components.html(f.read(), height=800, scrolling=True)

                st.markdown("### Node Properties")
                for node in nodes:
                    with st.expander(f"🔹 {node['label']}"):
                        st.json(node["props"])

        if st.button("Visualize Full Graph"):
            with st.spinner("Loading entire graph..."):
                nodes, edges = fetch_graph_data(relation_types=rel_types)
                if not nodes:
                    st.warning("No nodes/relationships found.")
                    return
                st.success(f"Loaded {len(nodes)} nodes and {len(edges)} relationships.")
                html_path = visualize_with_pyvis(nodes, edges)
                with open(html_path, "r", encoding="utf-8") as f:
                    components.html(f.read(), height=800, scrolling=True)

                st.markdown("### Node Properties")
                for node in nodes:
                    with st.expander(f"🔹 {node['label']}"):
                        st.json(node["props"])
