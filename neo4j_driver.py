from dotenv import load_dotenv
from neo4j import GraphDatabase

import os
load_dotenv()

driver = GraphDatabase.driver(
    os.getenv("NEO4J_URI"),
    auth=(os.getenv("NEO4J_USER"), os.getenv("NEO4J_PASSWORD"))
)

# driver.verify_connectivity()

records, summary, keys = driver.execute_query( # (1)
    "RETURN COUNT {()} AS count"
)

