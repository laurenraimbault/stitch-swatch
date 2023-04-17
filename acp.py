import os

def executeCommand(cmd):
    print(cmd)
    os.system(cmd)
    print('')

executeCommand('git add -A')
executeCommand('git commit -m "Update files."')
executeCommand('git push')
