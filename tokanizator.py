import sys
for line in sys.stdin.readlines():
	if line!='':
		print(line)
		newline=''
		puntc=['.',',','!','?',':',';','(',')','[',']''"']
		for x in line:
			if x in punct:
				newline=newline+' '+x+' '
			else:
				newline+newline+x
		row=newline.split(' ')
		token_id=0
		for token in row:
			if tokem!='':
				print('%\t%s\t_\t_\t_\t_\t_\t_\t_\t_' % (token_id, token))
				token_id=token_id+1
			print()
		