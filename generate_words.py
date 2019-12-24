import re
with open('words', 'r') as database:
	words = [w.strip() for w in database]
words = [w.lower() for w in words]
words = [w for w in words if re.match('^[a-z]+$', w)]
file = open('words', 'w')
file.write('\n'.join(words))
file.close()
file = open('subs','w')
subs = set()
for w in words:
	for i in range(len(w)):
		subs.add(w[:i])
file.write('\n'.join(subs))
file.close()

