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

    if line[0] == '#' or line[0\ =='/':
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
                else
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

file = open("./code_change.txt",'r')
for line in file.readlines():
    func_name = extract_func_name(line)
    if func_name != None:
        printf(func_name)
                    
    
