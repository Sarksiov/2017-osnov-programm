import sys
for line in sys.stdin.readlines():
	line=line.strip('\n')
	if line =='':
		print()
		continue 
	if line[0]=='#':
		print(line)
		continue
	row=line.split('\t')
	if len(row)>1:
		if len(row[1])>3:
			pl=row[1][-2]
			pl1=row[1][-3]
			if len(row[1])>4:
				pl2=row[1][-4]
			suffix = row[1][-2:]
			suffix1=row[1][-3:]
			row[9] = 'Suffix=' + suffix
			if pl=='т':
				if suffix=='тæ':
					row[5]='PL.NOM'
				if suffix=='ты':
					row[5]='PL.GEN' 
			if pl1=='т':
				if suffix =='æн':
					row[5] = 'PL.DAT';
				if suffix=='мæ':
					row[5]='PL.ALL'
				if suffix=='æй':
					row[5]='PL.ABL'
				if suffix=='ыл':
					row[5]='PL.SUPER'
				if suffix=='ау':
					row[5]='Can be EQU'
			if len(row[1])>4:
				if pl2!='' and pl2=='т':
					if suffix1=='имæ':
						row[5]='PL.COMIT'
				if pl!='т' and pl1!='т' and pl2!='т':
					if row[1][-1]=='ы':
						row[5]='It can be 3SG.PRES, if it is a verb, or GEN or IN, if it is a noun'
					if suffix =='æн':
						row[5] = 'DAT';
				if suffix=='мæ':
					row[5]='ALL'
				if suffix=='æй':
					row[5]='ABL'
				if suffix=='ыл':
					row[5]='SUPER'
				if suffix=='ау':
					row[5]='Can be EQU'
				if suffix1=='имæ':
					row[5]='COMIT'
		
	print(row)
		
	