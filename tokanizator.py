import sys
for line in sys.stdin.readlines():
	line=line.strip()
	if line!='':
		print('# text = %s' % (line))
		newline=''
		punct=['.',',','!','?',':',';','(',')','[',']''"']
		for x in line:
			if x in punct:
				newline=newline+' '+x+' '
			else:
				newline=newline+x
		row=newline.split(' ')
		token_id=1
		for token in row:
			token= token.strip()
			if token!='':
				print('%d\t%s\t_\t_\t_\t_\t_\t_\t_\t_' % (token_id, token))
				token_id=token_id+1
		print()
		