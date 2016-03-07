import sys

if len(sys.argv) != 2:
	print "ERROR: give valid arguments"
	sys.exit(0)

try:
	f = open(sys.argv[1]) 
except:
	print "ERROR: give valid filename"
	sys.exit(0)

if ".c" not in sys.argv[1]:
	print "WARNING: not a c source file" 

file_data = f.read() 

bracket = 0; commentMultiLine = 0; commentLine = 0; checkHeader = 0           
tempString = "" 

for i in range(0,len(file_data)):
	
	if file_data[i] == "{":                
		bracket += 1
	
	elif file_data[i] == "}":
		bracket -= 1

	elif file_data[i] == "#":               
		checkHeader += 1
	
	elif i < len(file_data)-1 and file_data[i] == "/":
		if file_data[i+1] == "/":
			commentLine += 1
		elif file_data[i+1] == "*":
			commentMultiLine += 1

	elif i < len(file_data)-1 and file_data[i] == "*" and file_data[i+1] == "/": 
		commentMultiLine -= 1

	elif file_data[i] == "\n" and (checkHeader > 0 or commentLine > 0):
		if checkHeader > 0:
			checkHeader -= 1
		elif commentLine > 0:
			commentLine -=1

	if commentMultiLine == 0 and checkHeader == 0 and bracket == 0 and commentLine == 0 and file_data[i] != "}" and file_data[i] != "/" and file_data[i] != "*":
		tempString += file_data[i]

functionsList = []
for i in tempString.split():
	if "(" in i :                  # to remove structs
		if i.split("(")[0].strip() not in functionsList:  
			functionsList.append(i.split("(")[0].strip())

print str(functionsList)