# Import JSON module
import json

# Open the existing JSON file for loading into a variable
with open("status.json", "r") as f:
  data = json.load(f)
  print (data)
  downed_servers = []
  for server in data:
      print(server)
      if server["state"] == "down":
          print("This one is down")
          down_servers.append(server)   

print(f"The following is a list of all the servers in a 'down' state: {downed_servers}")

with open("downed_servers.json", "w") as f2:
    spaced_servers = [f"{srv}\n" for srv in downed_servers]
    f2.writelines(spaced_servers)





 

