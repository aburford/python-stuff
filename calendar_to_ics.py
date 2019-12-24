#!/usr/bin/env python
import datetime
import re
mwf = {0,2,4}
tuth = {1,3}
# This script looks for a calendar.txt with a copy pasted plain text version of the google doc calendar and writes to calendar.ics a file to upload to the google calendar
with open('calendar.txt', 'r') as file:
	lines = [l for l in file.read().split('\n')]

ics = """BEGIN:VCALENDAR
PRODID:-//Google Inc//Google Calendar 70.9054//EN
VERSION:2.0
CALSCALE:GREGORIAN
METHOD:PUBLISH
X-WR-CALNAME:Schedule
X-WR-TIMEZONE:America/New_York
X-WR-CALDESC:Running Schedule
"""

def ics_date(date):
	formatted = date.strftime('%Y%m%dT%X').replace(':','')
	if date.hour == 0:
		formatted = formatted[:8]
	return formatted
i = 0
while i < len(lines):
	ics += "BEGIN:VEVENT\nCLASS:PUBLIC\n"
	date = datetime.datetime(2019, *[int(n) for n in lines[i].split('/')])
	i+=1
	if date.weekday() in mwf:
		date = date.replace(hour=16)
	elif date.weekday() in tuth:
		date = date.replace(hour=8)
	# date.hour is zero if this is a weekend event
	ics += "DTSTART;TZID=America/New_York:%s\n" % ics_date(date)
	if date.hour != 0:
		date = date.replace(hour=date.hour + 1, minute=30)
	ics += "DTEND;TZID=America/New_York:%s\n" % ics_date(date)
	ics += "LOCATION:Outdoor Track\nDESCRIPTION;LANGUAGE=en-us:"
	desc = ''
	while i < len(lines) and not re.fullmatch(r'\d\d?/\d\d?', lines[i]):
		desc += lines[i]+'\\n' if lines[i] else ''
		i += 1
	desc = desc.strip('\\n')
	if date.hour != 0:
		ics += desc
	ics += "\nTRANSP:TRANSPARENT\nSUMMARY:%s\nEND:VEVENT\n" % ('Running Practice' if date.hour != 0 else desc)
ics += "END:VCALENDAR\n"
with open('calendar.ics', 'w') as out:
	out.write(ics)
print('wrote to calendar.ics')