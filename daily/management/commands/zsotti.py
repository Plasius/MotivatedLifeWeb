inp= open('quotes.txt', 'r')
out= open('done.txt', 'w')

tomb= []
for line in inp:
	tomb.append(line[:-2])

out.write('\',\n \''.join(tomb))