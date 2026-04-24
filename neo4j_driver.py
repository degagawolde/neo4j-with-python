from dotenv import load_dotenv
from neo4j import GraphDatabase
from neo4j import Result, RoutingControl
import os
load_dotenv()

driver = GraphDatabase.driver(
    os.getenv("NEO4J_URI"),
    auth=(
        os.getenv("NEO4J_USERNAME"), 
        os.getenv("NEO4J_PASSWORD"))
)

driver.verify_connectivity()

cypher = """
MATCH (p:Person {name: $name})-[r:ACTED_IN]->(m:Movie)
RETURN m.title AS title, r.role AS role
"""
name = "Tom Hanks"

records, summary, keys = driver.execute_query( # (1)
    cypher,    # (2)
    name=name  # (3)
)
print(keys)  # ['title', 'role']
print(summary)  # A summary of the query execution

# RETURN m.title AS title, r.role AS role

for record in records:
  print(f"{name} played {record['role']} in {record['title']}")
    
    
result = driver.execute_query(
    cypher,
    name=name,
    result_transformer_= lambda result: [
        f"Tom Hanks played {record['role']} in {record['title']}"
        for record in result
    ]
)

print(result)  # ['Tom Hanks played Woody in Toy Story', ...]


result = driver.execute_query(
    cypher,
    name=name,
    result_transformer_=Result.to_df
)
print(result)  # ['Tom Hanks played Woody in Toy Story', ...]


result = driver.execute_query(
    cypher,
    name=name,
    result_transformer_=Result.to_df,
    routing_=RoutingControl.READ  # or simply "r"
)
print(result)