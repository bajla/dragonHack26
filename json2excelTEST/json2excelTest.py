import json
import pandas

with open('inputTest1.json', 'r') as f:
    jsonData = json.load(f)

structuredJSON = []

for recieptTransaction in jsonData["receipt_transactions"]:
    for itemTransaction in recieptTransaction["item_transactions"]:
        newItem = {
            "user": itemTransaction["user"],
            "date": itemTransaction["date"],
            "cost": itemTransaction["cost"],
            "quantity": itemTransaction["quantity"],
            "category": itemTransaction["category"]["title"],
        }
        structuredJSON.append(newItem)

print(structuredJSON)

dataFrame = pandas.json_normalize(structuredJSON)
dataFrame.to_excel("outputTest1.xlsx")