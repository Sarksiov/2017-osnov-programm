import sys
text=sys.stdin.read()
text=text.replace('.','\n')
text=text.replace('!','\n')
text=text.replace('?','\n')
print(text)