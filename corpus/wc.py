import sys
lines=0
letters=0
words=0
for x in sys.stdin.read():
	if x!='\n':
		letters=letters+1
	if x==' ' or x=='\n':
		words=words+1
	if x=='\n':
		lines=lines+1
print(lines)
print(words)
print(letters)
