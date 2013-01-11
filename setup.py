__author__ = 'phil'
from distutils.core import setup

setup(
	name='smallinvoice',
	version='0.1.1',
	author='dreipol GmbH: Philipp Laeubli, Etienne Wild',
	author_email='dev@dreipol.ch',
	packages=['smallinvoice', 'smallinvoice.tests'],
	url='http://pypi.python.org/pypi/Smallinvoice/',
	license='LICENSE.txt',
	description='A simple client wrapper for the smallinvoice.ch web api',
	long_description=open('README.txt').read(),
	install_requires=[
		"requests",
		],
)