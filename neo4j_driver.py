from neo4j import GraphDatabase

driver = GraphDatabase.driver(
  "neo4j://127.0.0.1:7687",       # (1)
  auth=("neo4j", "neo4j@learning") # (2)
)
