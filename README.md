# sendotp-python

Python package for the SendOTP API (https://sendotp.msg91.com/).


## Installation

    pip install sendotp


## Basic Usage

```python
import sendotp

otpobj =  sendotp.sendotp('Autk-Key','my message is {{otp}} keep otp with you.')


print otpobj.send(919981534313,'msgind')

print otpobj.verify(910000000000,3245)

print otpobj.retry(910000000000) OR
print otpobj.retry(910000000000,'text')
```