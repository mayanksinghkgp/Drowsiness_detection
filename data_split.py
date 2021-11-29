# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 23:39:45 2021

@author: Mayank 
"""

import random,shutil,os

os.listdir('dataset/train')

if not os.path.exists('dataset/valid'):
    os.makedirs('dataset/valid')
    os.makedirs('dataset/valid/Closed_Eyes')
    os.makedirs('dataset/valid/Open_Eyes')
    
closed = os.listdir('dataset/train/Closed_Eyes')
opn = os.listdir('dataset/train/Open_Eyes')

for i in closed[:int(.2*len(closed))]:
    shutil.move(os.path.join('dataset/train/Closed_Eyes',i), os.path.join('dataset/valid/Closed_Eyes',i))
    
for i in opn[:int(.2*len(opn))]:
    shutil.move(os.path.join('dataset/train/Open_Eyes',i), os.path.join('dataset/valid/Open_Eyes',i))