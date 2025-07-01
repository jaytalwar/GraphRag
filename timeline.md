# Timeline: Graph-RAG Based Agentic System

This document outlines the tasks for project focused on building a graph RAG from product documentation using Python, Neo4j, and Streamlit.

## Tasks

---

### Task 1: Documentation Parsing and JSON Node Creation
*   **Task ID:** T1
*   **Task Description:**
    *   Understand the structure of the product documentation located in the `/docs` directory.
    *   Design and implement a Python `DirectoryParser` class to recursively parse all Markdown (`.md`) files within the `/docs` directory and its subdirectories.
    *   For each Markdown file, extract its full content.
    *   Identify its hierarchical relationship (e.g., parent document, child documents) based on the directory structure.
    *   Generate a JSON representation for each parsed document. Each JSON object should represent a potential node in the knowledge graph.
    *   The JSON object should include at least:
        *   `name`: Name of the file or directory.
        *   `content`: Processed and clean textual content of the markdown file.
        *   `children`: An array of objects with keys - name and type (if any, based on subdirectories and documents).
    *   Store these JSON objects, as individual `.json` files in a new `/temp_data` directory.
*   **Assigned to:** Aastha
*   **Expected Delivery Date:** 11th June (Wed)
*   **Status:** DONE

---

### Task 2: Basic Knowledge Graph Construction in Neo4j
*   **Task ID:** T2
*   **Task Description:**
    *   Familiarize yourself with Neo4j graph database concepts: Nodes, Relationships, Properties, and the Cypher query language.
    *   Set up a local Neo4j instance.
    *   Design and implement a Python `KnowledgeGraph` class and corresponding methods to read the JSON files generated in Task T1.
    *   Design and implement a Python `TextProcessor` class to implement various NLP related methods like embedding generation, etc.
    *   For each JSON object:
        *   Create a corresponding Node in Neo4j (e.g., with a label like `File` or `Directory`).
        *   Store key information from the JSON (like `name`, `content`, `children`, `embedding`) as properties of this Neo4j node.
    *   Establish relationships between these nodes based on the hierarchical structure identified in Task T1. For example, create a `CONTAINS` relationship from a parent document node to its child document/directory nodes.
    *   The primary deliverable is a Neo4j database populated with nodes representing each document and directory along with relationships representing their basic directory structure.
*   **Assigned to:** Jay
*   **Expected Delivery Date:18th June (Wed)
*   **Status:** DONE
  
---

### Task 3: Identifying and Creating Additional Semantic Links
*   **Task ID:** T3
*   **Task Description:**
    *   The goal of this task is to enrich the knowledge graph by adding non-hierarchical (semantic) links only between document nodes.
    *   Re-parse the content of the documents (from the JSON files).
    *   Implement a strategy to identify potential relationships between different documentation sections that are not explicitly defined by the directory structure.
    *   Design and implement a Python `DataProcessor` class that will contain methods to implement the Task T3.
    *   Define new relationship types in Neo4j to represent these discovered links (e.g., `RELATED_TO`).
*   **Assigned to:** Harshika
*   **Expected Delivery Date:** 25th June (Wed)
*   **Status:** DONE

---

### Task 4: Knowledge Graph Retriever Implementation
*   **Task ID:** T4
*   **Task Description:**
    *   Design and implement a Python `GraphRAG` class.
    *   The `GraphRAG` class should:
        *   Establish a connection to the Neo4j database.
        *   Have a core method that accepts a user's natural language query (a string) as input.
        *   Implement logic to translate this user query into one or more Cypher queries to execute against the Neo4j graph. This might involve:
            *   Searching for nodes whose `content` property matches keywords from the user query.
            *   Leveraging the relationships (both hierarchical and semantic) to find connected/relevant information.
            *   (Optional, more advanced) If implementing text similarity for Task T3, you could embed the user query and find nodes with similar content embeddings.
        *   The method should retrieve the `content` of the Neo4j nodes that are deemed most relevant to the user's query.
        *   Consider how to rank or score the retrieved nodes/documents by relevance, if multiple results are found.
    *   The deliverable is the `GraphRAG` class, with clear documentation on how to use it and examples.
*   **Assigned to:** Aastha
*   **Expected Delivery Date:** 3rd July (Thursday)
*   **Status:** working on chat interface
---

### Task 5: Streamlit UI for Demonstration
*   **Task ID:** T5
*   **Task Description:**
    *   Develop a user-friendly web interface using Streamlit to showcase the capabilities of the knowledge graph and retriever.
    *   The UI should allow an end-user to:
        *   Enter a natural language query related to the product documentation.
        *   View the search results retrieved by the `GraphRAG` class (from Task T4).
        *   Display the content of the relevant document sections in a readable format.
    *   Consider adding features like:
        *   Displaying metadata about the retrieved documents (e.g., source path, related topics).
        *   Visualizing parts of the knowledge graph related to the query or results (optional, can be complex).
        *   Basic error handling and user feedback.
    *   Ensure the UI is intuitive and effectively demonstrates the project's value in navigating and understanding the product documentation.
    *   The UI should primarily interact with the `GraphRAG` class built in Task T4.
*   **Assigned to:** Jay
*   **Expected Delivery Date:** (To be filled by the intern)
*   **Status:** (To be filled by the intern)

--- 
