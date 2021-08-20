import pandas as pd
import plotly.express as ex
from desdeo_tools.utilities import non_dominated


room1obj = pd.read_csv("Day05Practical/room1/objective_vectors_4.csv", index_col=0)
room2obj = pd.read_csv("Day05Practical/room2/objective_vectors_4.csv", index_col=0)
room3obj = pd.read_csv("Day05Practical/room3/objective_vectors_4.csv", index_col=0)

room1obj["Group"] = 1
room2obj["Group"] = 2
room3obj["Group"] = 3

room1obj.rename(columns={"0": "Surface Area", "1":"Volume", "2":"Min Height", "3":"Floor Area"}, inplace=True)
room2obj.rename(columns={"0": "Surface Area", "1":"Volume", "2":"Min Height", "3":"Floor Area"}, inplace=True)
room3obj.rename(columns={"0": "Surface Area", "1":"Volume", "2":"Min Height", "3":"Floor Area"}, inplace=True)


all_rooms_obj = pd.concat([room1obj, room2obj, room3obj])
all_rooms_obj["Non-dominated"] = non_dominated(
    all_rooms_obj[["Surface Area", "Volume", "Min Height", "Floor Area"]].values)
all_rooms_obj["Volume"] = -all_rooms_obj["Volume"]
all_rooms_obj["Min Height"] = -all_rooms_obj["Min Height"]
all_rooms_obj["Floor Area"] = -all_rooms_obj["Floor Area"]


all_rooms_obj.describe()

fig = ex.parallel_coordinates(
    all_rooms_obj[all_rooms_obj["Non-dominated"]==True],
    dimensions=["Surface Area", "Volume", "Min Height", "Floor Area", "Group"],
    color="Group",
    #symbol="Non-dominated",
    #size=[1]*len(all_rooms_obj),
    #size_max = 12
)

fig.show()

all_rooms_non_dom = all_rooms_obj[all_rooms_obj["Non-dominated"]==True][["Surface Area", "Volume", "Min Height", "Floor Area"]]

all_rooms_non_dom.to_csv("All_groups_tent_problem_4_obj.csv", index=False)
