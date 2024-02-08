Dim ObjShell
Set ObjShell= CreateObject("WScript.Shell")

'Run the WarThunder Launcher (Steam or Normal)
ObjShell.Run chr(34) & "steam://rungameid/236390" & chr(34)
'select Window War Thunder
ObjShell.AppActivate "War Thunder"
'run Python bot script WTLogin.py
ObjShell.Run "python C:\Users\danie\Desktop\school\Python\Bot\WTLogin.py", 0, True
