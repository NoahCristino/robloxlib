import requests
import json
import sys
import re
import os
import getpass
import datetime
import ast

from requests import Session
from robobrowser import RoboBrowser
from bs4 import BeautifulSoup
from re import findall

global data

def check_friends(uid_one, uid_two):
    """
    uid_one: int
    uid_two: int
    """
    
    r = requests.get("https://www.roblox.com/Game/LuaWebService/HandleSocialRequest.ashx?method=IsFriendsWith&playerId=%s&userId=%s" %\
                     (str(uid_one), str(uid_two)))
    return r.text.rstrip() == '<Value Type="boolean">true</Value>'


def user_in_group(mode, uid, gid):
    """
    modes: str GetGroupRank (number of rank), str IsInGroup, str GetGroupRole (rank name)
    uid: int
    gid: int (group ID)
    """
                    
    r = requests.get("https://www.roblox.com/Game/LuaWebService/HandleSocialRequest.ashx?method=%s&playerid=%s&groupid=%s" %\
                    (mode, str(uid), str(gid)))
    if mode == "GetGroupRank":              
        return r.text
    elif mode == "IsInGroup":
        return r.text.rstrip() == '<Value Type="boolean">true</Value>'
    elif mode == "GetGroupRole":
        return r.text
    
    
def user_owns_asset(uid, aid):
    """
    uid: int
    aid: int
    """
    
    r = requests.get("https://api.roblox.com/Ownership/HasAsset?userId=%s&assetId=%s" % (str(uid), str(aid)))
    return r.text.rstrip() == 'true'


def username_taken(uname):
    """
	uname: str
	"""
    r = requests.get("https://www.roblox.com/UserCheck/DoesUsernameExist?username=%s" % uname)
    return r.text.rstrip() == '{"success":true}'


def get_primary_group_info(mode, uname):
    """
	mode: str GroupId (Primary Group's ID), str GroupName (Primary Group's Name), str RoleSetName (Rank in Primary Group)
	uname: str
	"""
    r = requests.get("https://www.roblox.com/Groups/GetPrimaryGroupInfo.ashx?users=%s" % uname).json()
    
    try:
        if mode == "GroupId":
            return r[uname]['GroupId']
        elif mode == "GroupName":
            return r[uname]['GroupName']
        elif mode == "GroupRole":
            return r[uname]['RoleSetName']
    except KeyError:
        return None
    
    
def get_package_ids(pid):
    """
	pid: int
	"""
    textlist = requests.get("https://web.roblox.com/Game/GetAssetIdsForPackageId?packageId=%s" % str(pid)).text
    return ast.literal_eval(textlist)
    
    
def valid_login(uname, pwd, proxies=False):
    """
	uname: str
	pwd: str
	proxies: dict ({'http': 'http://my.proxy.com/'})
	"""
    if proxies != False:
        session = Session()
        session.proxies = proxies
        browser = RoboBrowser(session=session, parser='lxml')
    else:
        browser = RoboBrowser(history=True,\
        user_agent='Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101  Firefox/40.1'\
        ,parser='lxml')
    login_url = 'https://www.roblox.com/account/signupredir'
    browser.open(login_url)
    form = browser.get_form(action='https://www.roblox.com/newlogin')
    form['username'].value = uname 
    form['password'].value = pwd
    browser.submit_form(form)
    source = str(browser.parsed())
    if "Hello, %s!" % uname in source:
        return True
    else:
        return False


def get_login_token(uname, pwd, proxy):
    """
	uname: str
	pwd: str
    proxies: str ip:port
	"""
    proxies = {}
    proxies['http'] = proxy
    if proxies != False:
        session = Session()
        session.proxies = proxies
        browser = RoboBrowser(session=session, parser='lxml')
    else:
        browser = RoboBrowser(history=True,\
        user_agent='Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101  Firefox/40.1'\
        ,parser='lxml')
    login_url = 'https://www.roblox.com/account/signupredir'
    browser.open(login_url)
    form = browser.get_form(action='https://www.roblox.com/newlogin')
    form['username'].value = uname 
    form['password'].value = pwd
    browser.submit_form(form)
    source = str(browser.parsed())
    return str(browser.session.cookies['.ROBLOSECURITY'])


def create_account(uname, pwd):
    pass
	

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
    r = requests.get("https://web.roblox.com/users/%s/profile" % str(uid))
    textdate = str(findall(r'\d+\/\d+\/\d+', r.text)[0])
    textdate = textdate.split("/")
    return datetime.date(int(textdate[2]), int(textdate[0]), int(textdate[1]))


def send_message(toid, subject, body):
    """
    toid: int
    subject: str
    body: str
    """
    #https://www.roblox.com/messages/send
    #{subject: "subject", body: "test", recipientid: "21628336", cacheBuster: 1501429626862}
    r = requests.post("https://www.roblox.com/messages/send", data={"subject": subject, "body": body, "recipientid": str(toid), "cacheBuster": 1501429626862})
    print r.status_code
	
