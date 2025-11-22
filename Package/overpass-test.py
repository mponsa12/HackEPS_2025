import overpy
api = overpy.Overpass()
result = api.query("""
    [out:json][timeout:25];
    area[name="Los Angeles"]->.searchArea;
    relation["boundary"="administrative"](area.searchArea);
    out geom;
""")

if not result:
    print("No se han encontrado resultados.")
else:
    print (result.relations)
    print(f"Se han encontrado {len(result.relations)} relaciones.")

    
    for rel in result.relations:
        print(f"\nID: {rel.id}, tags: {rel.tags}")
    