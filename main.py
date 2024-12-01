from lib.reader import *
from lib.OCR import *
from lib.matching import *
from lib.sendEmail import *
from lib.mock_db import *

path = "C:\\Users\\Intellect\\Fraud_detection\\test_sample.jpg"

process = process_image(path)

rip = extract_rip_from_image("./" + process['text'])

result = match_signature(process['signature'], mock_db[rip]['class'])

if result['Match'] == True:
	print('The check is genuine')
else:
	print('The check is Fraudulent, its owner was notified')
	notification_email(result['email'])
