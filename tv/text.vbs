Function KillProc(strProcName)
On Error Resume Next
 Set objWMIService = GetObject("winmgmts:{impersonationLevel=impersonate}!\\.\root\cimv2")
 Set arrProcesses = objWMIService.ExecQuery( "select * from win32_process where Name like '%"&strProcName&"%'" )
 For Each proccess In arrProcesses
 proccess.Terminate 0
 Next
End Function
KillProc("python")
KillProc("python")
KillProc("python")
KillProc("python")

 Dim oShell
Set oShell = WScript.CreateObject ("WSCript.shell")
oShell.run "main.py"'打开一个记事本
set oshell = nothing