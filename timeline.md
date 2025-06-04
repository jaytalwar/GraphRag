# Timeline: Knowledge Graph Construction

This document outlines the tasks for project focused on building a knowledge graph from product documentation using Python, Neo4j, and Streamlit.

## Tasks

---

### Task 1: Documentation Parsing and JSON Node Creation
*   **Task ID:** T1
*   **Task Description:**
    *   Understand the structure of the product documentation located in the `/docs` directory.
    *   Write Python scripts to recursively parse all Markdown (`.md`) files within the `/docs` directory and its subdirectories.
    *   For each Markdown file, extract its full content.
    *   Identify its hierarchical relationship (e.g., parent document, child documents) based on the directory structure. The file path can serve as a unique identifier.
    *   Generate a JSON representation for each parsed document. Each JSON object should represent a potential node in the knowledge graph.
    *   The JSON object should include at least:
        *   `id`: A unique identifier for the node (e.g., normalized file path).
        *   `source_path`: The original file path of the Markdown document.
        *   `content`: The full raw Markdown content of the document.
        *   `children_paths`: A list of file paths of immediate child documents (if any, based on subdirectories).
        *   `parent_path`: The file path of the parent document (if any).
    *   Store these JSON objects, perhaps as individual `.json` files in a new `output/json_nodes` directory, or as a single JSON array in one file.
*   **Assigned to:** Aastha
*   **Expected Delivery Date:** (To be filled by the intern)

---

### Task 2: Basic Knowledge Graph Construction in Neo4j
*   **Task ID:** T2
*   **Task Description:**
    *   Familiarize yourself with Neo4j graph database concepts: Nodes, Relationships, Properties, and the Cypher query language.
    *   Set up a local Neo4j instance or use a cloud-hosted one.
    *   Write Python scripts (e.g., using the `neo4j` Python driver) to read the JSON files/objects generated in Task T1.
    *   For each JSON object:
        *   Create a corresponding Node in Neo4j (e.g., with a label like `Document` or `DocSection`).
        *   Store key information from the JSON (like `id`, `source_path`, `content`) as properties of this Neo4j node.
    *   Establish relationships between these nodes based on the hierarchical structure identified in Task T1. For example, create a `HAS_CHILD` or `IS_PART_OF` relationship from a parent document node to its child document nodes.
    *   The primary deliverable is a Neo4j database populated with nodes representing each document and relationships representing their basic directory structure.
*   **Assigned to:** Jay
*   **Expected Delivery Date:** (To be filled by the intern)

---

### Task 3: Identifying and Creating Additional Semantic Links
*   **Task ID:** T3
*   **Task Description:**
    *   The goal of this task is to enrich the knowledge graph by adding non-hierarchical (semantic) links between document nodes.
    *   Re-parse the content of the documents (either from the JSON files or directly from the properties of nodes in Neo4j).
    *   Implement a strategy to identify potential relationships between different documentation sections that are not explicitly defined by the directory structure. Examples of strategies:
        *   **Keyword/Keyphrase Matching:** Identify common important terms across documents.
        *   **Named Entity Recognition (NER):** Extract entities (like product names, technologies, features) and see where they co-occur.
        *   **Hyperlink Analysis:** If Markdown files contain explicit links (`[text](./path)` or `[text](../path)`), these can be translated into relationships in Neo4j.
        *   **Simple Text Similarity:** (Optional, more advanced) Use basic TF-IDF or other simple vector similarity to find related documents.
    *   Define new relationship types in Neo4j to represent these discovered links (e.g., `MENTIONS_FEATURE`, `RELATED_TO`, `REFERENCES_API_ENDPOINT`, `EXPLAINS_CONCEPT`).
    *   Update your Python scripts to create these new relationships in the Neo4j graph.
    *   Document the types of new relationships identified and the methods/logic used to discover them.
*   **Assigned to:** Harshika
*   **Expected Delivery Date:** (To be filled by the intern)

---

### Task 4: Knowledge Graph Retriever Implementation
*   **Task ID:** T4
*   **Task Description:**
    *   Design and implement a Python `Retriever` class. This class will be responsible for querying the Neo4j knowledge graph.
    *   The `Retriever` class should:
        *   Establish a connection to the Neo4j database.
        *   Have a core method that accepts a user's natural language query (a string) as input.
        *   Implement logic to translate this user query into one or more Cypher queries to execute against the Neo4j graph. This might involve:
            *   Searching for nodes whose `content` property matches keywords from the user query.
            *   Leveraging the relationships (both hierarchical and semantic) to find connected/relevant information.
            *   (Optional, more advanced) If implementing text similarity for Task T3, you could embed the user query and find nodes with similar content embeddings.
        *   The method should retrieve the `content` (and potentially other properties like `source_path`) of the Neo4j nodes that are deemed most relevant to the user's query.
        *   Consider how to rank or score the retrieved nodes/documents by relevance, if multiple results are found.
    *   The deliverable is the `Retriever` class, with clear documentation on how to use it and examples.
    *   **(Stretch Goal for Week 5 / Further Work):** Begin developing a very simple User Interface (UI) using Streamlit. This UI should allow a user to type in a query, which then calls your `Retriever` class and displays the retrieved document snippets or their content.
*   **Assigned to:** Aastha
*   **Expected Delivery Date:** (To be filled by the intern)

---

### Task 5: Streamlit UI for Demonstration
*   **Task ID:** T5
*   **Task Description:**
    *   Develop a user-friendly web interface using Streamlit to showcase the capabilities of the knowledge graph and retriever.
    *   The UI should allow an end-user to:
        *   Enter a natural language query related to the product documentation.
        *   View the search results retrieved by the `Retriever` class (from Task T4).
        *   Display the content of the relevant document sections in a readable format.
    *   Consider adding features like:
        *   Displaying metadata about the retrieved documents (e.g., source path, related topics).
        *   Visualizing parts of the knowledge graph related to the query or results (optional, can be complex).
        *   Basic error handling and user feedback.
    *   Ensure the UI is intuitive and effectively demonstrates the project's value in navigating and understanding the product documentation.
    *   The UI should primarily interact with the `Retriever` class built in Task T4.
*   **Assigned to:** Jay
*   **Expected Delivery Date:** (To be filled by the intern)

--- 