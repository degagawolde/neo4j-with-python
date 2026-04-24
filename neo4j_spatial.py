from neo4j.spatial import WGS84Point

longitude = 55.296233
latitude = 25.276987
height = 828

point = WGS84Point(
    point = WGS84Point((longitude, latitude, height))
    )