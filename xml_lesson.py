#0) Fine all records with dates in the year 2013
#	- display the date from the first record in that year
#	- display the date from the last record of that year
#	-from just the 2013 records:
#		- display the last names of all the users with an 'id' attribute of 'admin'

#1) **starting over with all the records**, this time, find all records with:
#	- A payload between 59500 to 60500:
#		- display **all** the payloads that meet this criteria
#	- for records with these payloads:
#		- display **all**  the 'to' or 'from' IP addresses that fall within a 48.0.0.0/5 network.


#import xml module
import xml.etree.ElementTree as ET
import ipaddress

# open the file
x = open('records.xml')


# read with an xml library
xp = ET.parse(x)
tags = xp.findall('record/datetime')
root = xp.getroot()

'''
date_2013 = []
for tag in tags:
	if tag.text[:4] == '2013':
		dates_2013.append(tag.text)
print(dates_2013[0], dates_2013[-1], sep='\n')
'''

names = set()
for child in root:
	tag = child.find('user')
	if text.startswith('2013'):
		tag = child.find('user')
		if tag.get('id') == 'admin':
			names.add(child.find('user/lname').text)

''' Setting up ipaddresses using the apaddress module
addr = ipaddress.ip_address('192.168.0.4')
netw = ipaddress.ip_network('192.168.0.0/24')
can test if ip is in network
addr in netw
>> True
'''

netw = ipaddress.ip_network('48.0.0.0/5')

for child in root:
	text = child.find('payload').text
	payload = int(text)
	if 59500 < payload < 60500:
		fmip = child.find('ipaddresses/fmip')
		toip = child.find('ipaddresses/toip')

		fmip = ipaddress.ip_address(fmip.text)
		toip = ipaddress.ip_address(toip.text)
		# print(fmip.text, toip.text)

		if fmip in netw: # or statement will short circuit and equate to True if the first option is True
			print('fmip: ', fmip)

		if toip in netw:
			print('toip: ', topip)
# info@pyhawaii
# mynewlist = [item * 3 for item in l if item == 2]
# names = [name.strip() for name in fin.readlines()]
# names = [name.strip() for name in fin]
# duck typing 'quacks like a list' inheritance for parent and child

