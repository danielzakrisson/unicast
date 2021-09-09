import requests
import json
import numpy as np

from datetime import datetime


def etherium_data():
    # TheGraph GraphQL queries
    # Subgraph ID: QmWTrJJ9W8h3JE19FhCzzPYsJ2tgXZCdUqnbyuo64ToTBN
    # Subgraph URL: https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2

    # Data generated from TheGraph Uniswap v2 public, hosted API at https://thegraph.com/explorer/subgraph/uniswap/uniswap-v2
    # Token ID for WETH: 0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2
    # Token ID for WBTC: 0x2260fac5e5542a773aa44fbcfedf7c193bc2c599

    # Sample GraphQL query:
    # Daily price data for WETH in USD. Change the token ID e.g. to WBTC above to test another token. The public,
    # hosted TheGraph APIs are limited to 1000 values in the reply.

    query = """query {
        tokenDayDatas(first:1000, where: {token: "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"}, orderBy: date, orderDirection: desc) {
          date
          priceUSD
        }
    }"""

    # Call the public hosted TheGraph endpoint
    url = 'https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2'
    r = requests.post(url, json={'query': query})

    # Transform the string into a json object
    json_data = json.loads(r.text)

    # Create an empty Numpy array
    arr = np.empty((0,2), int)

    # Populate the Numpy array, while converting Unix timestamps to datetime objects, and price to float numbers
    for l in json_data['data']['tokenDayDatas']:
        arr = np.append(arr, np.array([[datetime.fromtimestamp(l['date']), np.float(l['priceUSD'])]]), axis=0)

    sort_arr = arr[np.argsort(arr[:,0])]
    sort_arr.shape
    eth_time = sort_arr[:,0]
    eth_value = sort_arr[:,1]

    return eth_time, eth_value