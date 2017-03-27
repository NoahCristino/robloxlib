import robloxlib

USERNAME = raw_input("Username? ")
PASSWORD = raw_input("Password? ")
GROUPID = raw_input("GroupId? ")

robloxlib.postJoinGroup(USERNAME, GROUPID, PASSWORD) # The password field is optional, it will ask later if not specified.

