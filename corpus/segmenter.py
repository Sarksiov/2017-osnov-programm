import sys
text=''
for x in sys.stdin.read():
	if x in '.!?':
		text=text+x+'\n'
	else:
		text=text+x
print(text)
