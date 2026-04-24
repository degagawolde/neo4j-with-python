# Neo4j with Python

A comprehensive collection of examples demonstrating how to interact with Neo4j graph database using Python. This project covers connection setup, querying, transactions, error handling, spatial data, and datetime operations.

## Features

- **Database Connection**: Secure connection using environment variables
- **Query Execution**: Basic and advanced Cypher queries with result transformation
- **Transaction Management**: Read/write operations with proper transaction handling
- **Error Handling**: Constraint validation and exception management
- **Spatial Data**: Working with geographical points using Neo4j's spatial types
- **DateTime Operations**: Handling temporal data with Neo4j's datetime functions
- **Graph Exploration**: Navigating nodes, relationships, and paths

## Prerequisites

- Python 3.8+
- Neo4j database (local or cloud instance)
- Required Python packages (see requirements.txt)

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd neo4j-with-python
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file with your Neo4j connection details:
```env
NEO4J_URI=neo4j://localhost:7687
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=your_password
```

## Project Structure

### Core Files

- **`neo4j_connect.py`**: Database connection setup and configuration
- **`neo4j_python_query.py`**: Comprehensive query examples including basic queries, result transformation, and graph exploration
- **`neo4j_transaction.py`**: Transaction management and read/write operations
- **`neo4j_db_error.py`**: Error handling for database constraints
- **`neo4j_spatial.py`**: Spatial data operations with WGS84Point
- **`neo4j_yeroo.py`**: DateTime operations and temporal data handling

## Usage Examples

### 1. Basic Connection

```python
from neo4j_connect import db_connection

driver = db_connection()
# Connection established and verified
```

### 2. Executing Queries

```python
from neo4j_python_query import ACTOR_MOVIES_QUERY

records, summary, keys = driver.execute_query(
    ACTOR_MOVIES_QUERY,
    name="Tom Hanks"
)

for record in records:
    print(f"Played {record['role']} in {record['title']}")
```

### 3. Transaction Management

```python
def create_person(tx, name, age):
    result = tx.run("""
        CREATE (p:Person {name: $name, age: $age})
        RETURN p
    """, name=name, age=age)
    return result.single()

with driver.session() as session:
    person = session.execute_write(create_person, "Alice", 30)
```

### 4. Error Handling

```python
from neo4j.exceptions import ConstraintError

def create_user(tx, name, email):
    try:
        result = tx.run("""
            CREATE (u:User {name: $name, email: $email})
            RETURN u
        """, name=name, email=email)
        return result.single()
    except ConstraintError as e:
        print(f"Constraint violation: {e.message}")
        return None
```

### 5. Spatial Data

```python
from neo4j.spatial import WGS84Point

point = WGS84Point((longitude, latitude, height))
# Use in queries for geographical operations
```

### 6. DateTime Operations

```python
from neo4j.time import DateTime
from datetime import timezone, timedelta

dt = DateTime(2024, 5, 15, 14, 30, 0, tzinfo=timezone(timedelta(hours=2)))
# Use in Cypher queries with datetime() function
```

## Key Concepts Demonstrated

### Query Execution Patterns

- **Basic Queries**: Simple MATCH and CREATE operations
- **Parameterized Queries**: Using parameters to prevent injection
- **Result Transformation**: Converting results to different formats (lists, DataFrames)
- **Graph Traversal**: Working with paths, nodes, and relationships

### Transaction Types

- **Read Transactions**: For data retrieval operations
- **Write Transactions**: For data modification operations
- **Batch Operations**: Multiple operations within a single transaction

### Error Handling

- **Constraint Violations**: Handling unique constraints and validation errors
- **Connection Issues**: Managing database connectivity problems
- **Query Errors**: Dealing with malformed Cypher queries

### Advanced Features

- **Spatial Indexing**: Geographical data and location-based queries
- **Temporal Data**: Date and time operations with timezone support
- **Result Processing**: Transforming query results for different use cases

## Best Practices

1. **Always use parameterized queries** to prevent Cypher injection
2. **Handle transactions appropriately** - use read transactions for queries, write for modifications
3. **Close connections** when done to free resources
4. **Use environment variables** for sensitive configuration
5. **Handle exceptions** gracefully with specific error types
6. **Transform results** as needed for your application requirements

## Running the Examples

Each Python file can be run independently:

```bash
python neo4j_connect.py
python neo4j_python_query.py
python neo4j_transaction.py
python neo4j_db_error.py
python neo4j_spatial.py
python neo4j_yeroo.py
```

Make sure your Neo4j instance is running and accessible before executing the scripts.

## Dependencies

- neo4j: Official Python driver for Neo4j
- python-dotenv: Environment variable management
- pandas (optional): DataFrame transformations

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add your examples or improvements
4. Test thoroughly with your Neo4j instance
5. Submit a pull request

## License

This project is open source. Please check the license file for details.

## Resources

- [Neo4j Python Driver Documentation](https://neo4j.com/docs/python-manual/current/)
- [Cypher Query Language Reference](https://neo4j.com/docs/cypher-manual/current/)
- [Neo4j Developer Guides](https://neo4j.com/developer/)</content>
<parameter name="filePath">README.md