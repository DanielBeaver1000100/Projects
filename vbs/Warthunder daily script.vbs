Dim ObjShell
Set ObjShell= CreateObject("WScript.Shell")
Do

'Run the WarThunder Launcher (Steam or Normal)
ObjShell.Run chr(34) & "steam://rungameid/236390" & chr(34)

'might get rid of
'Wait 10mins for updates (Time is in Milliseconds)
'Wscript.Sleep 600000

'Select War thunder as the active window
ObjShell.AppActivate "War Thunder"
'Run python bot
ObjShell.Run "python C:\Users\danie\Desktop\school\Python\Bot\WTDaily.py", 0, True

'exit gracefully?
'Close War Thunder
'ObjShell.Run "TASKKILL /IM aces.exe /F"
'Wait for 24h
Wscript.Sleep 85700000
Loop