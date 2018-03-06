import re
states ="Mississippi Alabama Texas Massachusetts Kansas\n"
print "\n\t",states
statesList=['0','0','0','0','0']
statesList[0]=re.findall(r'\w*xas',states)
statesList[1]=(re.findall(r'(?i)[k]{1}\w*[s]{1}',states))
statesList[2]=(re.findall(r'[M]{1}\w*[s]{1}[ ]+',states))
statesList[3]=(re.findall(r'\w*[a]{1}[ ]+',states))
statesList[4]=(re.findall(r'^[M]{1}\w*',states))
print statesList
