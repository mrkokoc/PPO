# coding: utf-8
"""Парсит исходный input_file в output.txt"""
import sys

txtparam = sys.argv[1]

input_file = open(txtparam, 'r')
contents_list = [i.strip() for i in input_file.readlines()]

mod_list = [i for i in contents_list if i != '0']

output_file = open('output.txt', 'w')
for i in mod_list:
    output_file.write('%s,' % i)
output_file.close()
