from dotenv import load_dotenv
from neo4j import GraphDatabase, Result, RoutingControl
import os

# --------------------------------------------------
# 1. Configuration & Connection
# --------------------------------------------------
load_dotenv()

URI = os.getenv("NEO4J_URI")
USER = os.getenv("NEO4J_USERNAME") or os.getenv("NEO4J_USER")
PASSWORD = os.getenv("NEO4J_PASSWORD")

def db_connection():
    if not all([URI, USER, PASSWORD]):
        raise ValueError("Missing Neo4j environment variables")

    driver = GraphDatabase.driver(URI, auth=(USER, PASSWORD))
    driver.verify_connectivity()

    print("✅ Connected to Neo4j")
    return driver