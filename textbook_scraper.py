from lxml import html
import requests
print('code,number,title,author,link')
tree = html.fromstring(requests.get('https://sbutextbook.github.io').content)
for subject_header in tree.cssselect('h3'):
	subject = subject_header.text_content()
	courses = subject_header.xpath('following-sibling::ul')[0]
	for c in courses:
		number = c.text_content().split()[0]
		if number == 'A':
			continue
		for book in c.cssselect('a'):
			print('"', '","'.join([subject, number, book.text_content(), '', book.attrib['href']]), '"', sep='')
