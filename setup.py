from distutils.core import setup

setup(name='seisk',
      version='0.1dev',
      description='Codes for downloading data and interacting with it using obspy',
      author='Kate Allstadt',
      author_email='kallstadt@usgs.gov',
      url='https://github.com/kallstadt-usgs/seisk/',
      packages=['reviewData', 'sigproc'],
      scripts=[])
