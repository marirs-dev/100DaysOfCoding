import pandas as pd

data = pd.read_csv("squirrel_data.csv")
grey_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(data[data["Primary Fur Color"] == "Red"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color":["Gray", "Cinnamon", "Black"],
    "Count":[grey_squirrel_count, red_squirrel_count, black_squirrel_count]
}

df = pd.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
