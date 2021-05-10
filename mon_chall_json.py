# Put the following JSON data into a file called status.json
#
#    [
#      {
#        "state": "up",
#        "server": "001"
#      },
#      {
#        "state": "down",
#        "server": "002"
#      },
#      {
#        "state": "up",
#        "server": "003"
#      },
#      {
#        "state": "up",
#        "server": "004"
#      },
#      {
#        "state": "down",
#        "server": "005"
#      },
#      {
#        "state": "up",
#        "server": "006"
#      },
#      {
#        "state": "down",
#        "server": "007"
#      }
#    ]
#




#It is your job to take JSON data from status.json, sort out the server names that are "down", and put their names into a new file called downed_servers.txt
import json

with open("status.json", "r") as f:
    data = json.load(f)
    print(data)
    downed_servers =  []
    for serv in data:
        if serv["state"] == "down":
            downed_servers.append(serv)

print(f"The following is a list of all the servers in a 'down' state: {downed_servers}")

with open("downed_servers.txt", "w") as f2:
    spaced_servers = [f"{srv['server']}\n" for srv in downed_servers]
    # spaced_servers = []
    # for srv in downed_servers:
    #    spaced_servers.append(srv)
    f2.writelines(spaced_servers)

#ROCKET SCIENCE CHALLENGE: return the full json for only the downed servers into a file called downed_servers.json
with open("downed_servers.json", "w") as f3:
    json.dump(downed_servers, f3, indent=4)
