import requests
import json


#ksql_query = "SELECT * FROM YOUR_KSQL_TABLE EMIT CHANGES LIMIT 5;"


def query_ksql(ksql_query, ksql_url = "http://ksqldb-server:8088", headers=None,  payload=None):
    headers = {"Content-Type": "application/vnd.ksql.v1+json; charset=utf-8"} if not headers else headers
    payload = {"ksql": ksql_query, "streamsProperties": {}} if not payload else payload
    response = requests.post(f"{ksql_url}/query", headers=headers, data=json.dumps(payload), timeout=20)
    if response.status_code == 200:
        return response
    else:
        print(f"Error: {response.status_code}")
        print(response.text)







# Execute the query

# Check response status and print results
