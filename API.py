import requests
import pandas as pd


def run_query(query):
    headers = {"Content-Type": "application/json"}
    response = requests.post('https://api.tarkov.dev/graphql', headers=headers, json={'query': query})
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(response.status_code, query))


def get_items():
    new_query = """
    {
        items{
            name
        }
    }
    """

    result = run_query(new_query)
    return result


def save_json(data_requested):
    if data_requested.lower() == "itemnames":
        df = pd.DataFrame(data=get_items())
        df.to_json(f"Data/itemnames.json")
    else:
        print("Unknown Parameter")


# print(result)

save_json("itemnames")
