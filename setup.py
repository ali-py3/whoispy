#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io
from setuptools import setup, find_packages
setup(
    name='whopy',
    version='0.1',
    description='Do whois from Ips',
    long_description_content_type='text/markdown',
    author='ali-py3',
    author_email='man.pyyy@gmail.com',
    license='GNU General Public License v3 (GPLv3)',
    url='https://github.com/ali-py3/',
    download_url='https://github.com/ali-py3/whoispy',
    zip_safe=False,
    packages=find_packages(),
    install_requires=[
        'ipwhois',
        'argparse'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Bug Hunter',
        'Intended Audience :: Information Technology',
        'Operating System :: OS Independent',
        'Topic :: Security',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python',
    ],
    entry_points={
        'console_scripts': ['whopy = whoispy.whopy:IpWhois']
    },
    keywords=['whoispy', 'bug bounty', 'http', 'pentesting', 'security'],
)
