import requests
import pandas as pd


def run_query(query):
    headers = {"Content-Type": "application/json"}
    response = requests.post('https://api.tarkov.dev/graphql', headers=headers, json={'query': query})
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(response.status_code, query))


def get_itemnames():
    new_query = """
    {
        items{
            id
            name
        }
    }
    """

    result = run_query(new_query)
    return result


def get_prices():
    new_query = """
{
  items {
    name
    avg24hPrice
    sellFor {
      vendor {
        name
      }
      price
    }
  }
}
        """

    result = run_query(new_query)
    return result


def save_json(data_requested):
    if data_requested.lower() == "itemnames":
        df = pd.DataFrame(data=get_itemnames())
        df.to_json(f"Data/itemnames.json")

    elif data_requested.lower() == "prices":
        df = pd.DataFrame(data=get_prices())
        df.to_json(f"Data/prices.json")

    else:
        print("Unknown Parameter")


# save_json("prices")
# save_json("itemnames")

