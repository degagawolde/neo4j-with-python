from neo4j import Result, RoutingControl

from neo4j_connect import db_connection

# --------------------------------------------------
# 1. Configuration & Connection
# --------------------------------------------------
driver = db_connection()
# --------------------------------------------------
# 2. Query Definition
# --------------------------------------------------
ACTOR_MOVIES_QUERY = """
MATCH (p:Person {name: $name})-[r:ACTED_IN]->(m:Movie)
RETURN m.title AS title, r.role AS role
"""

name = "Tom Hanks"

# --------------------------------------------------
# 3. Basic Query Execution
# --------------------------------------------------
records, summary, keys = driver.execute_query(
    ACTOR_MOVIES_QUERY,
    name=name
)

print("\n📌 Keys:", keys)
print("📊 Summary:", summary)

print("\n🎭 Actor Roles:")
for record in records:
    print(f"{name} played {record['role']} in {record['title']}")

# --------------------------------------------------
# 4. Custom Transformation (Safe, No Pandas)
# --------------------------------------------------
def transform_to_strings(result):
    return [
        f"{name} played {record['role']} in {record['title']}"
        for record in result
    ]

string_results = driver.execute_query(
    ACTOR_MOVIES_QUERY,
    name=name,
    result_transformer_=transform_to_strings
)

print("\n🧾 Transformed Output:")
print(string_results)

# --------------------------------------------------
# 5. Optional: Pandas Transformation (Guarded)
# --------------------------------------------------
def safe_to_df(result):
    try:
        return Result.to_df(result)
    except Exception as e:
        print("\n⚠️ Pandas transformation failed:", e)
        return list(result)

df_result = driver.execute_query(
    ACTOR_MOVIES_QUERY,
    name=name,
    result_transformer_=safe_to_df,
    routing_=RoutingControl.READ
)

print("\n📊 DataFrame Output:")
print(df_result)

# --------------------------------------------------
# 6. Graph Exploration (Nodes, Relationships, Paths)
# --------------------------------------------------
MOVIE_GRAPH_QUERY = """
MATCH path = (person:Person)-[actedIn:ACTED_IN]->(movie:Movie {title: $title})
RETURN path, person, actedIn, movie
"""

movie_title = "Toy Story"

records, _, _ = driver.execute_query(
    MOVIE_GRAPH_QUERY,
    title=movie_title
)

print("\n🎬 Graph Exploration:")

for record in records:
    person = record["person"]
    movie = record["movie"]
    acted_in = record["actedIn"]
    path = record["path"]

    # ------------------------------
    # Node (Movie)
    # ------------------------------
    print("\n🎥 Movie Node:")
    print("ID:", movie.element_id)
    print("Labels:", movie.labels)
    print("Properties:", dict(movie))

    print("Name (direct):", movie.get("name", "N/A"))

    # ------------------------------
    # Relationship
    # ------------------------------
    print("\n🔗 Relationship:")
    print("ID:", acted_in.id)
    print("Type:", acted_in.type)
    print("Properties:", dict(acted_in))

    print("Roles:", acted_in.get("roles", "(Unknown)"))

    print("Start Node:", acted_in.start_node)
    print("End Node:", acted_in.end_node)

    # ------------------------------
    # Path
    # ------------------------------
    print("\n🛣️ Path:")
    print("Start:", path.start_node)
    print("End:", path.end_node)
    print("Length:", len(path))
    print("Relationships:", path.relationships)

# --------------------------------------------------
# 7. Cleanup
# --------------------------------------------------
driver.close()
print("\n🔒 Connection closed")