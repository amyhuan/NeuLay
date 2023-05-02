# visualize the resulting graph using Matplotlib
import matplotlib.pyplot as plt
import json

# read the JSON data from a file
with open('data-pdx-mwh-co.json', 'r') as f:
    json_data = f.read()

    # parse the JSON data and convert it to a dictionary
    data = json.loads(json_data)

# read the file containing the X and Y coordinates of the nodes
with open('coords-pdx-mwh-co.csv', 'r') as f:
    lines = f.readlines()
    coords = [list(map(float, line.strip().split(','))) for line in lines]

# create a dictionary to map node IDs to coordinates
node_coords = {i: (x, y) for i, (x, y) in enumerate(coords)}

# create a scatter plot of the nodes with their labels
fig, ax = plt.subplots()
for i, node in enumerate(data['nodes']):
    x, y = node_coords[i]
    newX = x * 100
    newY = y * 100
    ax.scatter(newX, newY)
    ax.annotate(str(node['id']), (newX, newY))

# set the plot title and show the plot
ax.set_title('All links between devices matching regex (icr|ibr|sw|ier|cbe|rwa|ter|96c)')
plt.savefig("network-pdx-mwh-co.pdf", format="pdf", bbox_inches="tight")
