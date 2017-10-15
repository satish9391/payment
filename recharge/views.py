# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import json
import Checksum
import requests
import connectionutils
import base64
import random
from string import ascii_uppercase, ascii_lowercase, digits

# Create your views here.
def index(request):
	if request.method == 'POST':
		data = {}
		mob = request.POST['mob_no']
		amts = request.POST['amt']
		
		data['mob'] = mob
		data['amt'] = amts
		inv_len = 20
		special_char = '@-_.'
        	order_id = ''.join(random.choice(ascii_uppercase + digits + ascii_lowercase + special_char) for _ in range(inv_len))
		print order_id
		MERCHANT_KEY =  '%xnpkZ!oREvq_Id9'
		data_dict = {'REQUEST_TYPE':'DEFAULT','MID': 'rechar67895469891518', 'ORDER_ID': '%s' % order_id, 'TXN_AMOUNT': '%s' % amts, 'CUST_ID': 'satish@paytm.com', 'CHANNEL_ID': 'WEB', 'INDUSTRY_TYPE_ID': 'Retail', 'WEBSITE': 'WEB_STAGING', 'MOBILE_NO': '%s' % mob, 'EMAIL':'satish18pandey@gmail.com'}
		param_dict = data_dict
		link = 'https://pguat.paytm.com/oltp/HANDLER_INTERNAL/getTxnStatus?JsonData='
		param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(data_dict, MERCHANT_KEY)
		print param_dict
		result = connectionutils.get_response(link, param_dict)
		return HttpResponse(result)
	return render(request, "recharge/index.html")
