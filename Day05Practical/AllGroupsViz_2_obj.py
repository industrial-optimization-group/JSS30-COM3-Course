import pandas as pd
import plotly.express as ex
from desdeo_tools.utilities import non_dominated

room1obj = pd.read_csv("Day05Practical/room1/objective_vectors_2.csv", index_col=0)
room2obj = pd.read_csv("Day05Practical/room2/objective_vectors_2.csv", index_col=0)
room3obj = pd.read_csv("Day05Practical/room3/objective_vectors_2.csv", index_col=0)

room1obj["Group"] = "Room 1"
room2obj["Group"] = "Room 2"
room3obj["Group"] = "Room 3"

room1obj.rename(columns={"0": "Surface Area", "1":"Volume"}, inplace=True)
room2obj.rename(columns={"0": "Surface Area", "1":"Volume"}, inplace=True)
room3obj.rename(columns={"0": "Surface Area", "1":"Volume"}, inplace=True)


all_rooms_obj = pd.concat([room1obj, room2obj, room3obj])
all_rooms_obj["Non-dominated"] = non_dominated(all_rooms_obj[["Volume", "Surface Area"]].values)
all_rooms_obj["Volume"] = -all_rooms_obj["Volume"]

all_rooms_obj.describe()

fig = ex.scatter(
    all_rooms_obj,
    x="Volume",
    y="Surface Area",
    color="Group",
    symbol="Non-dominated",
    size=[1]*len(all_rooms_obj),
    size_max = 12
)

fig.show()


# In[ ]:




