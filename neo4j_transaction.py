
from neo4j_connect import db_connection


driver = db_connection()


def create_person(tx, name, age): # (1)
    result = tx.run("""
    CREATE (p:Person {name: $name, age: $age})
    RETURN p
    """, name=name, age=age) # (2)


def transfer_funds(tx, from_account, to_account, amount):
    # Deduct from first account
    tx.run(
        "MATCH (a:Account {id: $from_}) SET a.balance = a.balance - $amount",
        from_=from_account, amount=amount
    )

    # Add to second account
    tx.run(
        "MATCH (a:Account {id: $to}) SET a.balance = a.balance + $amount",
        to=to_account, amount=amount
    )



with driver.session() as session:
    def get_answer(tx, answer):
        result = tx.run("RETURN $answer AS answer", answer=answer)

        return result.consume()

    # Call the transaction function
    summary = session.execute_read(get_answer, answer=42)

    # Output the summary
    print(
        "Results available after", summary.result_available_after,
        "ms and consumed after", summary.result_consumed_after, "ms"
    )


def get_cheapest_flights(tx, date, origin, destination):
    """
    Return the cheapest flights between the origin and
    destination airports on a given date.
    """
    result = tx.run("""
        MATCH (origin:Airport)<-[:ORIGIN]-(f:Flight)-[:DESTINATION]->(destination:Airport),
            (f)-[:OPERATED_BY]->(operator:Airline)
        WHERE origin.name = $origin AND destination.name = $destination AND f.date = $date
        RETURN f.price AS price, operator.name AS operator
    """, date=date, origin=origin, destination=destination)
    return result.values()

from api import send_to_ui


with driver.session() as session:
    res = session.execute_read(

        get_cheapest_flights,
        date="2024-01-01",
        origin="LAX",
        destination="SFO"
    )

    for row in res:
        send_to_ui(row)
