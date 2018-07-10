import subprocess as sp

extProc = sp.Popen(['python', 'test.py'])  # runs myPyScript.py

print extProc

status = sp.Popen.poll(extProc)  # status should be 'None'

print status

sp.Popen.terminate(extProc)  # closes the process

status = sp.Popen.poll(extProc)  # status should now be something other than 'None' ('1' in my testing)

print status