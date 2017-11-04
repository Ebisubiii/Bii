# -*- coding: utf-8 -*-

Import LINETC.LINE
from LINETC.lib.curve.ttypes import *
from io import StringIO
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,sys
import re,string,os
import os.path,sys,urllib,shutil,subprocess

cl = LINETC.LINE()
cl.login(qr=True)
cl.loginResult()

ki = LINETC.LINE()
ki.login(qr=True)
ki.loginResult()

ka = LINETC.LINE()
ka.login(qr=True)
ka.loginResult()

ks = LINETC.LINE
ks.login(qr=True)
ks.loginResult()

kc = LINETC.LINE
kc.login(qr=True)
kc.loginResult()

kk = LINETC.LINE
kk.login(qr=True)
kk.loginResult()

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')
helpMessage ="""Creator BII
  
{Id}: ~Ã·~
{Mid}: ~Ã·~
{All mid}:
{Me}: ~Ã·~
{TC1/TC2/TC3}:"Contact"
{TC1/TC2/TC3 Say:}:"Kick kicker"
{Group Id}:"Id Me Group"
{TL : "Text"}:"Auto status TL"
{Clock :}:"Name Clock"
{Up clock}:"Up date Clock"
{Name }: 'text']:"Name me"
{MIC}: "mid"]:"Contact share"
{Reject}: " invite"}: "Reject invite"
{Massage add: "text"}: ~Ã·~
{Add confirmasi}: ~Ã·~
{Comment set : "Text"}
{Comment check}:”Check”
{Clock: on}:"Clock name on"
{clock: Off}:"Clock name off"

==COMMAND FOR SET==
{Contact: on/off}: 
{Auto join: on/off}: 
{Cancel Invite: 1 on/off}:
{Auto share: on/off}:
{Auto leave: on/off}: 
{Comment: on/off}: 
{Auto add: on/off}: 
{Auto like: on/off}: 
	
==COMMAND FOR BII GROUPS==
{Ban " @Tag}: 
{Unban " @Tag}: 
{Urlon]: "Open urL"
{Urloff}:"Closed urL
{Recheck}:" Check urL room"
{Ginfo}:"~Ã·~ data room"
{Invite}:"mid"]: 
{Say}:"Text": "Kicker talk"
{Cancel}:"Cancel invite"
{Gn}:"name":"Change name Group"
{NK}:"Name":~Ã·~
{Dead}:"Kick Blacklist"
  

      {Creator Bye BII}
        {Myselft}
  
"""
helpMessage2 ="""+Protection+

{[Protect:on/off}: 
{Namelock:on/off}: 
{Block Url:on/off}: 
{Blockinvite:on/off}:

    {Creator Bye BII}
      {Mysel}
"""
KAC = [cl,ki,kk,ks,kc,ka]

mid = cl.getProfile().mid
Amid = ki.getProfile().mid
kimid = kk.getProfile().mid
ki2mid = ks.getProfile().mid
Cmid = kc.getProfile().mid
Emid = ka.getProfile().mid
admin["uc77fd25b59f6e563d84f1334f3fed10b"]
me = cl.getProfile().mid
bot1 = cl.getProfile().mid
main = cl.getProfile().mid
kicker1 = ki.getProfile().mid
bots = me + kicker1
protectname = []
protecturl = []
protection = []
autocancel = {}
autoinvite = []
autoleaveroom = []

admins["uc77fd25b59f6e563d84f1334f3fed10b","uc77fd25b59f6e563d84f1334f3fed10b"]
Rx5 = ["u6c5ace30c96692ea899f39aac346f29a"]
Rx4 = ["u2d9156b23fdd849c5e95f1c339a29493"]
Rx3 = ["udbdb9821f7717a9dc569d8247a84fed1"]
Rx2 = ["ua51ba06b0dd18c0bfe2cc6caa3458202"]
Rx1 = ["u2c7f708769a2eb35d9ae9f73cd366e0b"]
Administrator = admins + Rx5 + Rx4 + Rx3 + Rx2 + Rx1
AS = Rx2 + Rx1 + Rx3 + Rx4 + Rx5
adminsA = admins + Rx3 + Rx51111

wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':False,
    'timeline':False,
    'autoAdd':False,
    'message':"Thank For add me O_O",
    "lang":"JP",
    "comment":"Auto like Bye Bii ",
    "likeOn":False,
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "blacklist":{}, 
    "wblacklist":False,
    "pnharfbot":{},
    "pname":{},
    "pro_name":{},    
    "dblacklist":False
}

wait2 = {
	'readMember':{},
	'readPoint':{},
	'ROM':{},
	'setTime':{}
    }
	
setTime = {}
setTime = wait2["setTime"]

res = {
    'num':{},
    'us':{},
    'au':{},
}

def Cmd(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = [""]
    for texX in tex:
        for command in commands:
            if string ==texX + command:
                return True
    return False
