def safe_to_df(result):
    try:
        from neo4j import Result
        return Result.to_df(result)
    except Exception as e:
        print("Falling back, pandas failed:", e)
        return list(result)