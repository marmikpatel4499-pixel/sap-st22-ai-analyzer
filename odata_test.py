import requests

url = "http://ztbtphana:8001/sap/opu/odata/sap/ZDUMP_AI_SRV_SRV/ZST_DUMP_INFOSet?$format=json"

response = requests.get(url)

print("Status:", response.status_code)

data = response.json()

print("Number of records:", len(data["d"]["results"]))

for row in data["d"]["results"][:5]:
    print(row["Seqno"], row["Flist"])