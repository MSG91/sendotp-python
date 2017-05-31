import json
import requests
from random import randint


class sendotp:

        def __init__(self,key,msg) :

                self.baseUrl = "http://control.msg91.com"
                self.authkey = key

                try:
                    msg
                except NameError:
                    self.msg = "Your otp is {{otp}}. Please do not share it with anybody"
                else:
                    self.msg  = msg

        def actionURLBuilder(self,actionurl) :
                # print self.baseUrl + '/api/' +str(actionurl)
                print (actionurl)
                return self.baseUrl + '/api/' +str(actionurl)


        def generateOtp(self) :
                return randint(1000,9999)

        def send(self,contactNumber,senderId,otp) :
                values = {
          'authkey' : self.authkey,
          'mobile' : contactNumber,
          'message' : self.msg.replace("{{otp}}", str(otp)),
          'sender' : senderId,
          'otp' : otp
          }
                print (self.call('sendotp.php',values))
                return otp

        def retry(self,contactNumber,retrytype='voice') :
                values = {
          'authkey' : self.authkey,
          'mobile' : contactNumber,
          'retrytype' : retrytype
          }
                print (values)
                response = self.call('retryotp.php',values)
                return;


        def verify(self,contactNumber,otp) :
                values = {
          'authkey' : self.authkey,
          'mobile' : contactNumber,
          'otp' : otp
          }
                response = self.call('verifyRequestOTP.php',values)
                return response;

        def call(self,actionurl,args) :
                url = self.actionURLBuilder(actionurl)
                print (url)
                payload = (args)

                response = requests.post(url,data=payload, verify=False)
                print (response.text)
                return response.status_code
