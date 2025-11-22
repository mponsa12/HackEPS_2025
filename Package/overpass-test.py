import overpy
api = overpy.Overpass()
result = api.query("""
    [out:json][timeout:25];
    area(112024)->.searchArea;
    // gather results
    relation["boundary"="administrative"](area.searchArea);
    // print results
    out geom;
""")
for rel in result.nodes:
    print(rel.tags.get("name"))
