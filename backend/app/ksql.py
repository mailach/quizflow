import requests
import json
import logging


#ksql_query = "SELECT * FROM YOUR_KSQL_TABLE EMIT CHANGES LIMIT 5;"

def load_table_from_response(response):
    res_data = []
    for line in response.iter_lines():
        if line:
            decoded_line = line.decode('utf-8')
            json_data = json.loads(decoded_line)
            res_data.append(json_data)

    colnames = [name.lower() for name in res_data[0]["columnNames"]]
    rows = res_data[1:]
    return [dict(zip(colnames, row)) for row in rows]



def query_ksql(ksql_query, ksql_url = "http://ksqldb-server:8088", headers=None,  payload=None):
    headers = {"Content-Type": "application/vnd.ksql.v1+json; charset=utf-8"} if not headers else headers
    payload = {"ksql": ksql_query, "streamsProperties": {}} if not payload else payload
    response = requests.post(f"{ksql_url}/query", headers=headers, data=json.dumps(payload), timeout=20)
    if response.status_code == 200:
        return load_table_from_response(response)
    else:
        print(f"Error: {response.status_code}")
        print(response.text)







# Execute the query

# Check response status and print results
