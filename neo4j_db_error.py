from neo4j.exceptions import ConstraintError

def create_user(tx, name, email):
    try:
        result = tx.run("""
            CREATE (u:User {name: $name, email: $email})
            RETURN u
        """, name=name, email=email)

    except ConstraintError as e:
        print(e.code)
        # Neo.ClientError.Schema.ConstraintValidationFailed
        print(e.message)
        # The value [email] for property [email] violates the constraint [unique_email]
        print(e.gql_status) # 22N41