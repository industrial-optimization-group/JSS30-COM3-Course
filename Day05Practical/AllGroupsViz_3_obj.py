import pandas as pd
import plotly.express as ex
from desdeo_tools.utilities import non_dominated

room1obj = pd.read_csv("Day05Practical/room1/objective_vectors_3.csv", index_col=0)
room2obj = pd.read_csv("Day05Practical/room2/objective_vectors_3.csv", index_col=0)
room3obj = pd.read_csv("Day05Practical/room3/objective_vectors_3.csv", index_col=0)

room1obj["Group"] = "Room 1"
room2obj["Group"] = "Room 2"
room3obj["Group"] = "Room 3"

room1obj.rename(columns={"0": "Weight", "1":"Stress", "2":"Deflection"}, inplace=True)
room2obj.rename(columns={"0": "Weight", "1":"Stress", "2":"Deflection"}, inplace=True)
room3obj.rename(columns={"0": "Weight", "1":"Stress", "2":"Deflection"}, inplace=True)


all_rooms_obj = pd.concat([room1obj, room2obj, room3obj])
all_rooms_obj["Non-dominated"] = non_dominated(all_rooms_obj[["Weight", "Stress", "Deflection"]].values)


all_rooms_obj.describe()


fig = ex.scatter_3d(
    all_rooms_obj,
    x="Weight",
    y="Stress",
    z="Deflection",
    color="Group",
    symbol="Non-dominated",
    size=[1]*len(all_rooms_obj),
    size_max = 12
)

fig.show()
