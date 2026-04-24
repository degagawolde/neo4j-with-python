from neo4j.time import DateTime
from datetime import timezone, timedelta

from neo4j_connect import db_connection

driver = db_connection()

driver.execute_query("""
CREATE (e:Event {
  startsAt: $datetime,              // (1)
  createdAt: datetime($dtstring),   // (2)
  updatedAt: datetime()             // (3)
})
""",
    datetime=DateTime(
        2024, 5, 15, 14, 30, 0,
        tzinfo=timezone(timedelta(hours=2))
    ),  # (4)
    dtstring="2024-05-15T14:30:00+02:00"
)
