import requests
import cgi
import Checksum
import requests
import base64
import json


def get_response(link, post_object):
	result = requests.post("https://pguat.paytm.com/oltp/HANDLER_INTERNAL/getTxnStatus?JsonData=%s" % post_object)
	print result.json()
	return get_values_from_response(result)

def get_values_from_response(result):
	MERCHANT_KEY = '%xnpkZ!oREvq_Id9'
	respons_dict = {}
	form = result
	print result.text
	return form
	for i in form.keys():
		respons_dict[i]=form[i].value
		if i=='CHECKSUMHASH':
			checksum = form[i].value
	if 'GATEWAYNAME' in respons_dict:
		if respons_dict['GATEWAYNAME'] == 'WALLET':
			respons_dict['BANKNAME'] = 'null';
	
	verify = Checksum.verify_checksum(respons_dict, MERCHANT_KEY, checksum)
	
	if verify:
		if respons_dict['RESPCODE'] == '01':
			return "order successful";
		else:
			return  "order unsuccessful because"+respons_dict['RESPMSG'];
	else:
		return "order unsuccessful because"+respons_dict['RESPMSG'];

