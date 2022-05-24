import os
import re
import sys

def is_valid_name(name):
    if re.match("[a-zA-Z_][a-zA-Z0-9]*",name) == None:
        return False
    return True

def is_not_ctl_statement(name):
    if name == "if" or name == "while" or name == "for" or name == "switch":
        return False
    return True

def trim_prefix(name):
    if name[0] == '+' or name[0] == '-':
        return name[1:]
    else:
        return name

def extract_func_name(line):
    line = line.strip()
    if len(line) < 2:
        return None

    if line[-1] != ')' and line[-1] != '{':
        return None
    
    if '(' not in line or ')' not in line:
        return None

    if line[0] == '#' or line[0] =='/':
        return None

    line = re.sub('\*',' ',line)
    line = re.sub('\&',' ',line)

    line = re.sub('\(',' \(',line)
    line_split = line.split()

    if len(line_split) < 2:
        return None

    bracket_num = 0
    for ch in line:
        if ch == '(':
            bracket_num += 1

    if bracket_num == 1:
        for index in range(len(line_split)):
            if '(' in line_split[index]:
                if is_not_ctl_statement(line_split[index-1]):
                    return trim_prefix(line_split[index - 1])
                else:
                    return None
    else:
        line = re.sub('\(',' ',line)
        line = re.sub('\)',' ',line)
        line_split = line.split()
        index = 0
        for one in line_split:
            if is_valid_name(one):
                index += 1
                if index == 2:
                    if is_not_ctl_statement(one):
                        return trim_prefix(one)
        return None
                              
def get_seeds_for_local_mode(origin_seed_dir,per_func_seed_dir,changed_funcs):
    new_seed_dir = "new_seed_dir"
    os.mkdir(new_seed_dir)
                              
    func_for_seed_lists = os.listdir(per_func_seed_dir)
    print(func_for_seed_lists)
    
    files_to_read = []
    for changed_func in changed_funcs:
        if changed_func in func_for_seed_lists:
            print("func: " + changed_func)
            files_to_read.append(os.path.join(per_func_seed_dir,changed_func))
    
    selected_names = set()
    for fname in files_to_read:
        f = open(fname)
        for line in f.readlines():
            print("line: "+line)
            selected_names.add(line.strip())
    
    selected_seeds = []
    copied_seeds= []
    
    for name in selected_names:
        selected_seeds.append(os.path.join(origin_seed_dir,name))
        copied_seeds.append(os.path.join(new_seed_dir,name))
    
    for i in range(len(selected_seeds)):
        shutill.copyfile(selected_seeds[i],copied_seeds[i])
    
    return new_seed_dir

path_for_codechange = os.path.realpath(sys.argv[1])
path_for_origin_seed = os.path.realpath(sys.argv[2])
path_for_per_func_seed_dir = os.path.realpath(sys.argv[3]);
                              
file = open(path_for_codechange,'r')
                              
func_names = set()
                              
for line in file.readlines():
    func_name = extract_func_name(line)
    if func_name != None and func_name != "main":
        func_names.add(func_name)
                              
test_seed_dir = get_seeds_for_local_mode(path_for_origin_seed,path_for_per_func_seed_dir,func_names)
print(test_seed_dir)
                          

    
