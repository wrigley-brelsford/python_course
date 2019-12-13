# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pycroscopy as scope
import matplotlib.pyplot as plt 
import scipy as sci
import h5py
import pyUSID

#Create an object capable of translating .ibw files
TranslateObj=scope.io.translators.IgorIBWTranslator(max_mem_mb=1024)

#Translate the requisite file
Output=TranslateObj.translate(file_path=r'C:\Users\ppxjbw\Documents\AFM\November\01112019_JW\BN228_Reg1_0005.ibw', verbose=True)

print(Output)

#Opening this file to read in sections as a numpy array 
Read_Path=Output
h5_File=h5py.File(Output, mode='r')

#pyUSID.hdf_utils.print_tree(h5_File)
for key, val in pyUSID.hdf_utils.get_attributes(h5_File).items():
    print('{} : {}'.format(key, val))
    

h5_File.close()