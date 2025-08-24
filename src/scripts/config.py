import os
import platform

os_name = platform.system()

if os_name == "Windows":
    DULL = " > nul 2>&1 &"
else:
    DULL = " > /dev/null 2>&1 &"

def run_shell(cmnd):
    os.system(cmnd + DULL)

def os_is(platform):
    return os_name == platform

def not_supported():
    print(os_name + " (is not supported)")
