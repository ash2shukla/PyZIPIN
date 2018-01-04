from setuptools import setup
setup(
  name = 'PyZIPIN',
  packages = ['PyZIPIN'], # this must be the same as the name above
  version = '0.1',
  description = 'A python3 library providing information of ZIP codes of India based on data from data.gov.in(2018)',
  license='MIT',
  author = 'Ashish Shukla',
  author_email = 'ash2shukla@gmail.com',
  url = 'https://github.com/ash2shukla/PyZIPIN', # use the URL to the github repo
  download_url = 'https://github.com/ash2shukla/RailIN/archive/0.1.tar.gz',
  keywords = ['zipcodes','pincode','india','data.gov.in'], # arbitrary keywords
  classifiers = [],
  include_package_data = True,
  install_requires=[
         'sqlalchemy'
          ]
)
