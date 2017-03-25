import requests
import json
global data
import sys
import re
import urllib
import os
import getpass

def checkFriends(userid1, userid2):
    r = requests.get("https://www.roblox.com/Game/LuaWebService/HandleSocialRequest.ashx?method=IsFriendsWith&playerId="+str(userid1)+"&userId="+str(userid2))
    if "true" in r.text:
        return True
    else:
        return False
def userInGroup(mode, userid, groupid):
    #modes: GetGroupRank (number of rank), IsInGroup, GetGroupRole (rank name)
    r = requests.get("https://www.roblox.com/Game/LuaWebService/HandleSocialRequest.ashx?method="+str(mode)+"&playerid="+str(userid)+"&groupid="+str(groupid))
    if mode == "GetGroupRank":
        r2 = r.text[22:]
        r3 = r2.split("<")
        r4 = r3[0]
        return str(r4)
    if mode == "IsInGroup":
        if "true" in r.text:
            return True
        else:
            return False
    if mode == "GetGroupRole":
        return r.text
def userOwnsAsset(userid, assetid):
    r = requests.get("https://api.roblox.com/Ownership/HasAsset?userId="+str(userid)+"&assetId="+str(assetid))
    if "false" in r.text:
        return False
    else:
        return True
def usernameTaken(username):
    r = requests.get("https://www.roblox.com/UserCheck/DoesUsernameExist?username="+str(username))
    if "true" in r.text:
        return True
    else:
        return False
def getPrimaryGroupInfo(mode, username):
    try:
        r = requests.get("https://www.roblox.com/Groups/GetPrimaryGroupInfo.ashx?users="+str(username))
    except requests.exceptions.RequestException as e:
        print("")
        print("An connection error has occured, details below.")
        print("")
        print(e)
        print("")
        sys.exit(1)
    if mode == "GroupId":
        data = r.json()
        username1 = str(username)
        print(data[username1]['GroupId'])
    if mode == "GroupName":
        data = r.json()
        username1 = str(username)
        print(data[username1]['GroupName'])
    if mode == "GroupRole":
        data = r.json()
        username1 = str(username)
        print(data[username1]['RoleSetName'])
    else:
        print("An error has occured, please check spelling.")
def getPackageIds(packageid):
    try:
        r = requests.get("https://web.roblox.com/Game/GetAssetIdsForPackageId?packageId="+str(packageid))
        a = r.text
        print(a)
    except Exception as e:
        print("")
        print("A error has occured, please see below.")
        print("")
        print(e)
def postLogin(username):
    password = getpass.getpass('Password: ')
    try:
        r = requests.post("https://www.roblox.com/NewLogin", data={"username":str(username),"password":password})
        print("Logged in.")
    except Exception as e:
        print("")
        print("A error has occured, please see below.")
        print("")
        print(e)
