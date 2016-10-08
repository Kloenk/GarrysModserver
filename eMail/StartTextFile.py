#!/usr/bin/env python3

import smtplib

import sys
from email.mime.text import MIMEText
from GModServer import Variables

def SendStartEMail(steamWorkshopId, serverGamemode, serverdefaultMap, serverMaxPlayer,serverIP, serverPort):
    text = '''
    The GCG Server Will now start.
    The steamWorkshopId from the pack is %s, the Gamode of the server is %s, the map is %s, there are %s players allowed,
    the server is runing on IP %s:%s.
    ''' % (steamWorkshopId, serverGamemode, serverdefaultMap, serverMaxPlayer, serverIP, serverPort)
    msg = MIMEText(text, 'plain')
    msg['Subject'] = "starting info"
    msg['to']      = '[GCG] Root Server Managment'
    msg['From']    = '[GCG] Root Server'
    try:
        conn = smtplib.SMTP_SSL(Variables.SMTPServerAddres)
        conn.set_debuglevel(True)
        conn.login(Variables.ServerEmailAddr, Variables.ServerEmailPwd)
        try:
            conn.sendmail(Variables.ServerEmailAddr, Variables.AdminEmailAddres, msg.as_string())
        finally:
            conn.close()
    except Exception as exc:
        print("critical Error: %s" % exc)



if __name__ == '__main__':
    from GModServer.Variables import *
    SendStartEMail(SteamWorkShopId, ServerGamemode, ServerDefaultMap, ServerMaxPlayer, ServerIp, ServerPort)
    from PythonServerKernel.Exceptions import RunnedFromFalseFile
    raise RunnedFromFalseFile('eMail_StartTextFile_py')
