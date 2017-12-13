import sys
m={}
tagfreq={}
wordfreq={}
total=0
for line in sys.stdin.readlines():
	if line[0]=='#':
		continue
	if '\t' not in line:
		continue
	row=line.split('\t')
	tag=row[3]
	form=row[1]
	if form not in m:
		m[form]={}
	if tag not in m[form]:
		m[form][tag]=0
	if tag not in tagfreq:
		tagfreq[tag]=0
	tagfreq[tag]=tagfreq[tag]+1
	if form not in wordfreq:
		wordfreq[form]=0
	wordfreq[form]=wordfreq[form]+1
	m[form][tag]=m[form][tag]+1
	total=total+1
for tag in tagfreq:
	print(tagfreq[tag]/total,'\t',tagfreq[tag],'\t',tag,'_')
for x in m:
	for y in m[x]:
		print(m[x][y]/wordfreq[x],'\t',m[x][y],'\t',y,'\t',x)
		