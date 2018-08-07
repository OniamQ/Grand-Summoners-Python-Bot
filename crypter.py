# -*- coding: utf-8 -*-
from Crypto.Cipher import AES
import base64
import json
from pkcs7 import PKCS7Encoder

class Crypter(object):
	def __init__(self):
		self.encoder=PKCS7Encoder()
	
	def decrypt(self,input,key):
		return self.encoder.decode(AES.new(base64.b64decode(key), AES.MODE_CBC, '\x00'*16).decrypt(base64.b64decode(input)))

	def encrypt(self,input,key):
		padded_data=self.encoder.encode(json.dumps(input))
		return base64.b64encode(AES.new(base64.b64decode(key), AES.MODE_CBC, '\x00'*16).encrypt(padded_data))