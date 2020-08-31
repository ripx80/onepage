#!/usr/bin/env python
#encoding:utf-8


#not working :-9

__author__="ripx80ler"
__date__="27.03.2013"
__copyright__="Copyright"
__version__="1.0"

import os
import argparse

struct=['apps','docs','libs','settings','templates','scripts','locale','confs']

parser = argparse.ArgumentParser(description='create django project templates')
parser.add_argument('--version', action='version', version='%(prog)s '+__version__)
parser.add_argument('-v','--verbose',help='set programm in debug mode',action='count',dest='verbose',default=False)
parser.add_argument('--template',help='copy from django template directory',default=False,dest='template',type=str)
parser.add_argument('project',help='set the root directory for structing files',type=str)
args = parser.parse_args()

try:
    os.system("script2.py 1")
    from django.core import management

try:
    os.mkdir(args.project)
except:
    print('canot create directory. already exsists?')
    exit(1)

if args.template:
    print('copy from tempalte path')

else:
    print('create project structure')


