#-------------------------------------------------------------------------------
# Name:        words
# Purpose:
#
# Author:      michael willows
#
# Created:     7/4/2017
# Copyright:   (c) michael willows 2017
# Licence:     GPL
#-------------------------------------------------------------------------------
import scanf
import parse
Vars = list()
VarValues = list()#parallel to vars
#---------------------------------
def printl(x):
    print x
__builtin__funcs = {'print':printl}
def NewVar(vname,vvalue):
    Vars.append(vname)
    VarValues.append(vvalue)
def GetValFromVar(vname):
    i = Vars.index(vname)
    return VarValues[i]
def SetValtoVar(vname,vvalue):
     loc = Vars.index(vname)
     del VarValues[loc]
     VarValues.insert(loc, vvalue)
     pass
def OutPutStack():
    for i in Vars:
        print i, GetValFromVar(i)
def is_number(s):
    try:
        complex(s) # for int, long, float and complex
    except ValueError:
        return False

    return True
def isVar(v):
    try:
     if v in Vars:
        return True
    except:
        return False
    return False
    pass
def GetDataFromLine(line):
    data = tuple()
    try:                               #try until proper capture from scanf
     data = scanf.sscanf(line,"%s = %s + %s")
    except:
     pass
    try:
     data = scanf.sscanf(line,"%s = %d + %s")
    except:
     pass
    try:
     data = scanf.sscanf(line,"%s = %s + %d")
    except:
     pass
    return data
    pass
def add_operation(data):
       if isVar(data[1]) == True:       #var = var + var
        if isVar(data[2]) == True:
         SetValtoVar(data[0],int(GetValFromVar(data[1])) + int(GetValFromVar(data[2])))
       if isVar(data[1]) == False:      #var = %d + %d
        if isVar(data[2]) == False:
         SetValtoVar(data[0],data[1] + data[2])
       if isVar(data[1]) == True:       #var = var + %d
        if isVar(data[2]) == False:
         SetValtoVar(data[0],GetValFromVar(data[1]) + data[2])
       if isVar(data[1]) == False:     #var = %d + var
        if isVar(data[2]) == True:
         SetValtoVar(data[0],data[1] + GetValFromVar(data[2]))
def CaptureFunctionParams(line):
    p2 = line.split('(',1)[0]
    p1 = line.split(',',1)[0].replace(p2 + '(',"").replace(')',"")
    np = line.count(',') + 1
    elems = list()
    for i in range(np):
        elems.append(line.split(',',1)[i].replace(p2 + '(',"").replace(')',""))
    for i in range(len(elems)):
        if isVar(elems[i]) == True:
            v = GetValFromVar(elems[i])
            del elems[i]
            elems.insert(i,v)
    return elems
    pass

def LineParser(line):
    cmd = line.split(' ', 1)[0]
    operator = ""
    rightOp = ""
    if cmd.rstrip('\n') in Vars and cmd == line:
        print VarValues[Vars.index(cmd.rstrip('\n'))]
    elif cmd == "string":
        data = scanf.sscanf(line,"string %s = %s")
        NewVar(data[0],data[1])
    elif cmd == "int":
        data = scanf.sscanf(line,"int %s = %d")
        NewVar(data[0],data[1])
    elif cmd.find("("):
        fcmd = ""
        try:
         fcmd = line.split('(', 1)[0]
        except:
         pass
        if fcmd in __builtin__funcs:
            data = CaptureFunctionParams(line)
            __builtin__funcs[fcmd](data)
        else:
            #user defined function
            pass

        pass
    try:
       if line.split(' ', 1)[1][0] == '=':
         data = GetDataFromLine(line)
         add_operation(data)
    except:
        pass


    pass
def main():
    file = "nlang.txt"
    for line in open(file,'r').readlines():
       LineParser(line)
    #OutPutStack()
    pass

if __name__ == '__main__':
    main() #main entry
