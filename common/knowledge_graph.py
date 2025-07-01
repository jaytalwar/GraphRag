import os
import json
from neo4j import GraphDatabase
 
class KnowledgeGraph:
    def __init__(self, uri, username, password, data_directory, text_processor,database="neo4j"):
        """ Initializes a connection to a Neo4j database and sets up paths and processors for handling data and text processing."""
        self.driver = GraphDatabase.driver(uri, auth=(username, password))
        self.data_directory = data_directory
        self.text_processor = text_processor
        self.database = database
        self.json_nodes = {}
        with open("queries.json","r") as f:
            self.queries=json.load(f)
 
    def close(self):
        """ Shuts down the connection to the Neo4j database by closing the driver."""
        self.driver.close()
 
    def load_json_files(self):
        """ Reads all .json files from the specified data directory, loads their contents, and stores each file's data. """
        for filename in os.listdir(self.data_directory):
            if filename.endswith(".json"):
                path = os.path.join(self.data_directory, filename)
                with open(path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.json_nodes[data['path']] = data
 
    def create_node(self, tx, node):
        """ Adds a unique File or Directory node to Neo4j with its path, name, content, and generated embedding."""
        label = "Directory" if node['type'] == 'directory' else "File"
        embedding = self.text_processor.generate_embedding(node.get('content', ''))
        query=self.queries["create_node"].replace("{label}",label)
        tx.run(query,path=node['path'],name=node['name'],
                content=node.get('content',''),embedding=embedding)
 
    def create_relationship(self, tx, parent_path, child_path):
        """Creates a relationship between a parent and child node in the graph."""
        query = self.queries["create_relationship"]
        tx.run(query, parent_path=parent_path, child_path=child_path)
 
    def build_graph(self):
        """Load JSON nodes and build the Neo4j graph with nodes and parent-child relationships."""
        self.load_json_files()
        with self.driver.session() as session:
            session.run(self.queries["clear_graph"])
            for node in self.json_nodes.values():
                session.write_transaction(self.create_node, node)
            for parent_node in self.json_nodes.values():
                for child in parent_node.get('children', []):
                    child_path = child['path']
                    if child_path in self.json_nodes:
                        session.write_transaction(
                            self.create_relationship,
                            parent_node['path'],
                            child_path
                        )
 
 
    def get_all_document_nodes(self):
        """Return a list of all file-type nodes with their path, name, and content."""
        return [
            {
                "path": node["path"],
                "name": node["name"],
                "content": node.get("content", "")
            }
            for node in self.json_nodes.values()
            if node.get("type") == "file"
        ]
       
                   
    def run_query(self, query_name, parameters=None):
        """Executes a named Cypher query with optional parameters."""
        query = self.queries.get(query_name)
        if not query:
            raise ValueError(f"Query '{query_name}' not found in queries.json")
        with self.driver.session() as session:
            result = session.run(query, **(parameters or {}))
            return [record.data() for record in result]
 
   
    def get_node_by_path(self, path):
        """Retrieve a single node from the graph based on its file path."""
        results = self.run_query("get_node_by_path", {"path": path})
        return results[0] if results else None