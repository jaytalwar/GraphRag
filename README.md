# Project: Graph-RAG Based Agentic System

This project aims to build a knowledge graph from product documentation. Interns will work over a 5-week timeline to parse documentation, ingest it into a Neo4j graph database, identify semantic relationships, and build a retriever to query the graph and expose it through an agentic chat interface.

## Project Goals
-   Parse Markdown documentation into structured JSON data.
-   Construct a hierarchical knowledge graph in Neo4j.
-   Enrich the graph with additional semantic links between documentation nodes.
-   Develop a Python-based retriever to query the knowledge graph based on user input.
-   (Optional) Create a simple Streamlit UI for interacting with the retriever.

## Technology Stack
-   **Programming Language:** Python
-   **Graph Database:** Neo4j
-   **User Interface (Optional):** Streamlit
-   **Documentation Format:** Markdown

## Getting Started
1.  Ensure you have Python (3.10+) and Pip installed.
2.  Set up a local Neo4j instance
3.  Clone this repository.
4.  Refer to `timeline.md` for task breakdown and details.
5.  The product documentation to be processed is located in the `/docs` directory.

## Project Structure
-   `/docs`: Contains the raw product documentation in Markdown format.
-   `timeline.md`: Outlines the project tasks, assignments, and deadlines.
-   `README.md`: This file - provides an overview of the project.