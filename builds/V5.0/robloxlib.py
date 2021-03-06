import requests
import json
global data
import sys
import re
import os
import getpass
import datefinder
from bs4 import BeautifulSoup

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
        return data[username1]['GroupId']
    if mode == "GroupName":
        data = r.json()
        username1 = str(username)
        return data[username1]['GroupName']
    if mode == "GroupRole":
        data = r.json()
        username1 = str(username)
        return data[username1]['RoleSetName']
    else:
        print("An error has occured, please check spelling.")
def getPackageIds(packageid):
    try:
        r = requests.get("https://web.roblox.com/Game/GetAssetIdsForPackageId?packageId="+str(packageid))
        a = r.text
        return a
    except Exception as e:
        print("")
        print("A error has occured, please see below.")
        print("")
        print(e)
def postLogin(username):
    password = getpass.getpass('ROBLOX Account Password: ')
    try:
        r = requests.post("https://www.roblox.com/NewLogin", data={"username":str(username),"password":password})
        print("Logged in.")
        return r.status_code
    except requests.exceptions.RequestException as e:
        print("")
        print("A error has occured, please see below. Please note, this does not work with 2-Step Verification accounts yet.")
        print("")
        print(e)
def getRecommendedUsername(username):
    try:
        r = requests.get("https://web.roblox.com/UserCheck/GetRecommendedUsername?usernameToTry="+str(username))
        a = r.text
        return a
    except requests.exceptions.RequestException as e:
        print("")
        print("A error has occured, please see below.")
        print("")
        print(e)
def postJoinGroup(username, groupid, *password):
    try:
        if password:
            s = requests.session()
            r = s.post("https://www.roblox.com/NewLogin", data={"username":str(username),"password":password})

            page = s.get('http://www.roblox.com/groups/group.aspx?gid='+str(groupid))
            soup=BeautifulSoup(page.content, "lxml")
            VIEWSTATE=soup.find(id="__VIEWSTATE")['value']
            VIEWSTATEGENERATOR=soup.find(id="__VIEWSTATEGENERATOR")['value']
            EVENTVALIDATION=soup.find(id="__EVENTVALIDATION")['value']

            join = s.get('http://www.roblox.com/groups/group.aspx?gid='+str(groupid), data=dict(__EVENTTARGET="JoinGroupDiv", __EVENTARGUMENT="Click", __LASTFOCUS="", __VIEWSTATE=VIEWSTATE, __VIEWSTATEGENERATOR=VIEWSTATEGENERATOR, __EVENTVALIDATION=EVENTVALIDATION), allow_redirects=True)
            print("Sent group request.")
        else:
            password = getpass.getpass('ROBLOX Account Password: ')
            s = requests.session()
            r = s.post("https://www.roblox.com/NewLogin", data={"username":str(username),"password":password})

            page = s.get('http://www.roblox.com/groups/group.aspx?gid='+str(groupid))
            soup=BeautifulSoup(page.content, "lxml")
            VIEWSTATE=soup.find(id="__VIEWSTATE")['value']
            VIEWSTATEGENERATOR=soup.find(id="__VIEWSTATEGENERATOR")['value']
            EVENTVALIDATION=soup.find(id="__EVENTVALIDATION")['value']

            join = s.get('http://www.roblox.com/groups/group.aspx?gid='+str(groupid), data=dict(__EVENTTARGET="JoinGroupDiv", __EVENTARGUMENT="Click", __LASTFOCUS="", __VIEWSTATE=VIEWSTATE, __VIEWSTATEGENERATOR=VIEWSTATEGENERATOR, __EVENTVALIDATION=EVENTVALIDATION), allow_redirects=True)
            print("Sent group request.")
    except requests.exceptions.RequestException as e:
        print("")
        print("A error has occured, please see below. Please note, this does not work with 2-Step Verification accounts yet.")
        print("")
        print(e)
def userJoinDate(userid):
    r = requests.get("https://web.roblox.com/users/"+str(userid)+"/profile")
    text = r.text
    for item in text.split('</p>'):
        if '<p class="text-lead">' in item:
            userjoin = datefinder.find_dates(item [ item.find('<p class="text-lead">')+len('<p>') : ])
            for userdate in userjoin:
                return userdate
