from setuptools import setup

setup(name='sendotp',
      version='0.0.1',
      description='For sending OTP via MSG91',
      url='https://github.com/MSG91/sendotp-python',
      author='Rahul Chordiya',
      author_email='rahul@walkover.in',
      license='MIT',
      packages=['sendotp'],
      install_requires=['requests']
      zip_safe=False)
