from __future__ import print_function
from asyncio.subprocess import PIPE #for python 2.7

import os
import sys
import shutil
import argparse
import subprocess
from threading import Timer

def execute_aflpp(aflpp_path,executable_name,local_seeddir_path,file_mode):

    afl_fuzz_path = aflpp_path + "/afl-fuzz"
    cmd = [afl_fuzz_path,"-i",local_seeddir_path,"-o","local_out",executable_name]
    if file_mode == True:
        cmd.append("@@")

    env_var = os.environ.copy()
    env_var["AFL_SKIP_CPUFREQ"] = "1"
    env_var["AFL_I_DONT_CARE_ABOUT_MISSING_CRASHES"] = "1"

    if (sys.version_info < (3,3)):
       proc = subprocess.Popen(cmd,env=env_var)
       timer = Timer(5,proc.kill)
       try:
         timer.start()
         proc.wait()
       finally:
         timer.cancel()
    else:
       proc = subprocess.Popen(cmd, env=env_var)
       try:
         proc.wait(timeout=500)
       except subprocess.TimeoutExpired:
         proc.kill()

    return proc.returncode
 
def main () :
  
    parser = argparse.ArgumentParser()
    parser.add_argument("-w",help="path of working dir",required=True)
    parser.add_argument("-a",help="path of afl++",required=True)
    parser.add_argument("-x",help="name of executable",required=True)
    parser.add_argument("-p",help="path of per function seed dir",required=True)

    args = parser.parse_args()

    wkdir_path = args.w
    aflpp_path = args.a
    executable_name = args.x
    per_func_seed_dir = args.p

    return_code = execute_aflpp(aflpp_path,executable_name,per_func_seed_dir,False)
    print("RETURN CODE = " , return_code,type(return_code))

if __name__ == "__main__":
  main()
