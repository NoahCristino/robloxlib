# robloxlib
A python library for ROBLOX!
# Prerequisites
Before using the library you need to install the requests library.
If you have pip then do: `pip install requests`

If not: http://docs.python-guide.org/en/latest/starting/installation/
# How to install
Place the robloxlib.py file in your python directory ex. C:\Python27. Done.

If you want to install using `python setup.py install` (experimental) then look in the testing folder.

# Examples
Check the examples directory for examples
# Documentation
# checkFriends(userid1, userid2)

Description: Checks if two users are friends. 

Example: https://github.com/NoahCristino/Python-Roblox-Library/blob/master/examples/friendcheck.py

# userInGroup(mode, userid, groupid):

Description: GetGroupRank/Role: Gets the number/name of the users rank IsInGroup: Check if user is in group. 

Example: https://github.com/NoahCristino/Python-Roblox-Library/blob/master/examples/rankcheck.py
# userOwnsAsset(userid, assetid)

Description: Checks to see if user owns a asset.

Example: https://github.com/dogesum/robloxlib-fork/blob/master/examples/userOwnsAsset.py

# usernameTaken(username)

Description: Checks to see if username is taken.

Example: https://github.com/dogesum/robloxlib-fork/blob/master/examples/usernameTaken.py

# getPrimaryGroupInfo(mode, username)

Description: Gets primary group's GroupID/GroupName/GroupRole

Example: https://github.com/dogesum/robloxlib-fork/blob/master/examples/getPrimaryGroupInfo.py

# postLogin(username)

Description: Gets username and password and sends a POST request to https://www.roblox.com/Newlogin. (Trying to work on a way with users w/ 2-Step Verification.)

Example: https://github.com/dogesum/robloxlib-fork/blob/master/examples/postLogin.py

# getPackageIDs(packageid)

Description: Gets all IDs in a package

Example: https://github.com/dogesum/robloxlib-fork/blob/master/examples/getPackageIds.py
