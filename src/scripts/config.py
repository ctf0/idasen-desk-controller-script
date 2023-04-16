import os
import platform

DULL = "nul 2>&1 &"
os_name = platform.system()

def run_shell(cmnd):
    os.system(cmnd + DULL)

def os_is(platform):
    return os_name == platform

def not_supported():
    print(os_name + " (is not supported)")
