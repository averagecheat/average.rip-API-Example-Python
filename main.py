# This example requires the requests library be installed.
from requests import get
from os import system

system("title average.rip API Example Python") 

# replace this with your own informations
username = "anditv21"
uid = "1"

# saving api response data in string format.
injectcount = get(f"https://average.rip/panel/api.php?inject").text
user_pb = get(f"https://average.rip/panel/api.php?user_pb=" + username).text
sub = get(f"https://average.rip/panel/api.php?days=" + username).text
ban = get(f"https://average.rip/panel/api.php?bancheck=" + username).text
verify = get(f"https://average.rip/panel/api.php?verifystatus=" + username).text
staff = get(f"https://average.rip/panel/api.php?staffcheck=" + username).text
discordid = get(f"https://average.rip/panel/api.php?getid=" + username).text
touid = get(f"https://average.rip/panel/api.php?touid=" + username).text
toname = get(f"https://average.rip/panel/api.php?toname=" + uid).text

print("The total injection count of average is currently: " + injectcount)
print("Here is the avatar url of " + username + " : " + user_pb)
print(username + " has " + sub + " days sub left.")

if ban == "1":
    print(username + "is banned.")
else:
    print(username + " is not banned.")

if verify == "1":
    print(username + " is verified.")
else:
    print(username + " is not verified.")


if staff == "False":
    print(username + " is not a staff.")
else:
    print(username + " is an " + staff)

print("The Discord ID of " + username + " is " + discordid)
print(username + " has the UID " + touid)
print(toname + "is the UID of " + username)
