import overpy
api = overpy.Overpass()
result = api.query("""
    [out:json][timeout:25];
    {{geocodeArea:Los Angeles}}->.searchArea;
    // gather results
    relation["boundary"="administrative"](area.searchArea);
    // print results
    out geom;
""")
for node in result.nodes:
    print("Restaurant:", node.tags.get("name", "n/a"))
