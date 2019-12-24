# import re
# filename = '/usr/share/dict/words'
# # filename = 'test'
# words = [w.strip() for w in open(filename)]
# words = [w.lower() for w in words]
# words = [w for w in words if re.match('^[a-z]+$', w)]
# file = open('words', 'w')
# for w in words:
# 	file.write(w+'\n')
# file.close()
# file = open('subs','w')
# subs = set()
# for w in words:
# 	for i in range(len(w)):
# 		subs.add(w[:i])
# for s in subs:
# 	file.write(s+'\n')
# file.close()

from http.server import BaseHTTPRequestHandler, HTTPServer
import logging

def valid(pos):
	return pos[0] > -1 and pos[0] < 4 and pos[1] > -1 and pos[1] < 4 and not visited[pos[0]][pos[1]]
# -- position and current substring
def solve(pos, sub):
	global visited
	global answer
	global board
	global stack
	global used_words
	visited[pos[0]][pos[1]] = True
	stack.append(pos)
	for x in range(-1,2):
		for y in range(-1,2):
			if x != 0 or y != 0:
				next_pos = [pos[0]+x, pos[1]+y]
				if valid(next_pos):
					sub += board[next_pos[0]][next_pos[1]]
					if sub in subs:
						solve(next_pos, sub)
					if sub in words and sub not in used_words:
						print(sub)
						used_words.add(sub)
						stack.append(next_pos)
						# add to answer
						answer.append(','.join(['-'.join([str(i+1) for i in pos]) for pos in stack]))
						stack.pop()
					sub = sub[:-1]
	visited[pos[0]][pos[1]] = False
	stack.pop()

def run_solver():
	# -- initialize recursive backtracking solution
	global visited
	global used_words
	global stack
	global board
	used_words = set()
	stack = []
	visited = [[False]*4 for _ in range(4)]
	print(visited)
	for i in range(4):
		for j in range(4):
			solve([i,j], board[i][j])
	# answer.sort(key=lambda x: len(x), reverse=True)

class S(BaseHTTPRequestHandler):
	def _set_response(self):
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()

	def do_GET(self):
		logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
		board_str = self.path.strip('/').lower()
		global board
		global answer
		board = [list(board_str[i:i+4]) for i in range(0,16,4)]
		print(board)
		answer = []
		run_solver()
		self._set_response()
		self.wfile.write('\n'.join(answer).encode('utf-8'))

	def do_POST(self):
		content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
		post_data = self.rfile.read(content_length) # <--- Gets the data itself
		logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n", str(self.path), str(self.headers), post_data.decode('utf-8'))

		self._set_response()
		self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=S, port=8080):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

print('loading dictionary')
words = set()
subs = set()
with open('words', 'r') as file:
	for line in file.read().split('\n'):
		if line:
			words.add(line)
with open('subs', 'r') as file:
	for line in file.read().split('\n'):
		if line:
			subs.add(line)

answer = []
board = []
stack = []
visited = []
used_words = set()

run()

