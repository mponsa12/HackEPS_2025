import overpy
api = overpy.Overpass()
result = api.query("""
    node
      ["amenity"="restaurant"]
      (40.730610,-73.935242,40.741404,-73.921285);
    out;
""")
for node in result.nodes:
    print("Restaurant:", node.tags.get("name", "n/a"))
