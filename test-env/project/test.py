#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 13:47:03 2022

@author: qgf169
"""
#mangler cudamat
import numpy as np
import _pickle as cPickle
import matplotlib.pyplot as plt
import shutil
import scipy.io
import configparser
import argparse
import sklearn
import pickle
from PIL import Image



print("hello world")
print(2+2)

im = Image.open("luca.jpeg")
print("image loaded")
