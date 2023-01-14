import json

with open("rooms.json","r")as f:
    data=json.load(f)
with open("rooms.json","w")as f:
    json.dump(data,f,indent=5,sort_keys=False)
print(data)
with open("rooms.json","r")as f:
    print(f.read())
