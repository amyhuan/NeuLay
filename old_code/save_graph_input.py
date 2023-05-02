import csv
import json

# read the CSV file and convert it to a dictionary
nodes = {}
links = {}
with open('links-pdx-mwh-co.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        source, target = row
        if "StartDevice" in source:
            continue
        if source not in links:
            links[source] = []
        links[source].append(target)

        if source not in nodes:
            nodes[source] = True
        if target not in nodes:
            nodes[target] = True

# create the input format for the Python script
data = {
    "directed": False,
    "multigraph": False,
    "graph": {},
    "nodes": [{"id": n} for n in nodes],
    "links": [{"source": source, "target": j} for i, source in enumerate(links) for j in links[source]]
}

json_data = json.dumps(data)

# write the JSON string to a file
with open('data-pdx-mwh-co.json', 'w') as f:
    f.write(json_data)
