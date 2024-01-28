import pandas as pd
import json

with open("Data/prices.json", "r") as f:
    data = json.load(f)

df = pd.json_normalize(data['data']['items'], 'sellFor', ['name', 'avg24hPrice'])

df.set_index('name', inplace=True)

df_pivoted = df.pivot_table(index=df.index, columns='vendor.name', values='price', aggfunc='first')

df_pivoted.reset_index(inplace=True)

df_pivoted.rename(columns={'name':'ItemName'}, inplace=True)

# print(df_pivoted.to_string())

# searchitem = input("What item would you like to see prices for? ")

# print(df_pivoted.loc[df['ItemName'] == 'Colt M4A1 5.56x45 assault rifle'])
# print(df_pivoted.loc[df_pivoted['ItemName'] == searchitem])

columns = ["Fence", "Mechanic", "Therapist", "Prapor", "Skier", "Flea Market", "Peacekeeper"]
data = df_pivoted.loc[df_pivoted['ItemName'] == "Colt M4A1 5.56x45 assault rifle", columns]

highest_value_column = data.iloc[0].idxmax()
highest_value = data.iloc[0].max()

second_highest_value_column = data.iloc[0].nlargest(2).idxmin()
second_highest_value = data.iloc[0].nlargest(2).iloc[1]

print(f"Best Value: {highest_value_column} \nPrice: {highest_value}\n\n"
      f"Second highest value: {second_highest_value_column}\nPrice: {second_highest_value}")
