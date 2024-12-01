from lib.reader import *
from lib.OCR import *
from lib.matching import *
from lib.sendEmail import *
from lib.mock_db import *
"""
path = "C:\\Users\\raouf\\Desktop\\Hackathon\\Final Project\\test_sample.jpg"

process = process_image(path)

rip = extract_rip_from_image("./" + process['text'])

result = match_signature(process['signature'], mock_db[rip]['class'])

if result['Match'] == True:
	print(f'The check is genuine, Signature belongs to {mock_db[rip]['name']}')
else:
	print('The check is Fraudulent, its owner was notified')
	#notification_email(result['email'])
"""

def do(path):

	process = process_image(path)

	rip = extract_rip_from_image("./" + process['text'])

	result = match_signature(process['signature'], mock_db[rip]['class'])

	if result['Match'] == True:
		print(f'The check is genuine, Signature belongs to {mock_db[rip]['name']}')
		return 'success'
	else:
		print('The check is Fraudulent, its owner was notified')
		notification_email(mock_db[rip]['email'])
		return 'fail'