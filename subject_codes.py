from lxml import html
import requests
tree = html.fromstring(requests.get('https://www.stonybrook.edu/sb/bulletin/current/courses/browse/byabbreviation/').content)
print('{',end='')
for course in tree.cssselect('#bulletin_course_search_table tr'):
	code, title = [a.text_content().strip().strip('()') for a in course.cssselect('a')]
	print(f'"{code}" => "{title}", ', end='')
print('}', end='')