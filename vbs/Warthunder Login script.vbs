Dim ObjShell
Set ObjShell= CreateObject("WScript.Shell")
'Do
'Run the WarThunder Launcher (Steam or Normal)

ObjShell.Run chr(34) & "steam://rungameid/236390" & chr(34)
'Wait 10mins for updates (Time is in Milliseconds)
'Wscript.Sleep 600000
ObjShell.AppActivate "War Thunder"
ObjShell.Run "python C:\Users\danie\Desktop\school\Python\Bot\WTLogin.py", 0, True
