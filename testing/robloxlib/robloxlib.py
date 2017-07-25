import requests
import json
import sys
import re
import os
import getpass
import datefinder

from bs4 import BeautifulSoup
from re import findall

global data

def check_friends(uid_one, uid_two):
    """
    uid_one: str
    uid_two: str
    """
    
    r = requests.get("https://www.roblox.com/Game/LuaWebService/HandleSocialRequest.ashx?method=IsFriendsWith&playerId=%s&userId=%s" %\
                     (uid_one, uid_two))
    return r.text.rstrip() == "true"


def user_in_group(mode, uid, gid):
    """
    modes: GetGroupRank (number of rank), IsInGroup, GetGroupRole (rank name)
    uid: str
    gid: str (group ID)
    """
                    
    r = requests.get("https://www.roblox.com/Game/LuaWebService/HandleSocialRequest.ashx?method=%s&playerid=%s&groupid=%s" %\
                    (mode, uid, gid))
    if mode == "GetGroupRank":              
        return r.text
    if mode == "IsInGroup":
        return r.text.rstrip() == "true"
    if mode == "GetGroupRole":
        return r.text
    
    
def user_owns_asset(uid, aid):
    """
    uid: str
    aid: str
    """
    
    r = requests.get("https://api.roblox.com/Ownership/HasAsset?userId=%s&assetId=%s" % (uid, aid))
    return r.text.rstrip() == "true"


def username_taken(uname):
    r = requests.get("https://www.roblox.com/UserCheck/DoesUsernameExist?username=%s" % uname)
    return r.text.rstrip() == "true"


def get_primary_group_info(mode, uname):
    r = requests.get("https://www.roblox.com/Groups/GetPrimaryGroupInfo.ashx?users=%s" % uname).json()
    
    try:
        if mode == "GroupId":
            return r[uname]['GroupId']
        elif mode == "GroupName":
            return r[uname]['GroupName']
        elif mode == "GroupRole":
            return r[uname]['RoleSetName']
    except KeyError:
        return ''  # should return NoneType instead
    
    
def get_package_ids(pid):
    return requests.get("https://web.roblox.com/Game/GetAssetIdsForPackageId?packageId=%s" % pid).text
    
    
def post_login(uname, pwd):
    r = requests.post("https://api.roblox.com/v2/login", data={"username": uname,"password":pwd})
    return r.status_code == 200

    
def get_recommended_username(uname):
    return requests.get("https://web.roblox.com/UserCheck/GetRecommendedUsername?usernameToTry=%s" % uname).text

    
def post_join_group(uname, gid, pwd):
    session = requests.session()
    page = session.get('http://www.roblox.com/groups/group.aspx?gid=%s' % groupid)
    soup = BeautifulSoup(page.content, "lxml")
    VSTATE = soup.find(id="__VIEWSTATE")['value']
    VSTATE_GEN = soup.find(id="__VIEWSTATEGENERATOR")['value']
    EVNTVALID = soup.find(id="__EVENTVALIDATION")['value']
    join = session.get('http://www.roblox.com/groups/group.aspx?gid=%s' % groupid,
                       data=dict(__EVENTTARGET="JoinGroupDiv", __EVENTARGUMENT="Click",
                       __LASTFOCUS="", __VIEWSTATE=VSTATE, __VIEWSTATEGENERATOR=VSTATE_GEN,
                       __EVENTVALIDATION=EVNTVALID), allow_redirects=True)
    session.close() 
    
    return join.status_code
            
def user_join_date(uid):
    r = requests.get("https://web.roblox.com/users/%s/profile" % uid)
    return findall(r'\d+\/\d+\/\d+')[-1]
    
