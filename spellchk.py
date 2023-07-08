from collections import *
import csv
import json
import re
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
import math

def dataGen(): # creates the freq table of words with the given text corpus
    text={} # keys-words, values-freq
    with open('gutenberg.txt') as f: # text corpus used for valid words
        for line in f.readlines():
            for w in line.strip().strip('!?.,:;"@#%&*()').split(' '): # data formatting
                w = w.lstrip(r'"#[]').rstrip(r'!?.,:;"@#%&*()[]').lower()
                if(w!='' and w.isalpha()): # only lower alphabetic
                    text[w] = (text[w]+1) if(w in text.keys()) else 0
    return text 

valid = lambda word: (word in text.keys()) # if the given word is valid
validW = lambda L: list({w for w in L if(valid(w))}) # valid words from a list
P = lambda w: text[w]/sum(text.values()) if valid(w) else 0 # P(W=w)

delW = lambda w: [w[:i]+w[i+1:] for i in range(len(w))] # all words from deleting 1 char

def insW(w): # all words from inserting 1 char
    ins=[]
    for ch in range(ord('a'),ord('z')+1):
        for i in range(-1,len(w)):
            ins.append(w[:i+1]+chr(ch)+w[i+1:])
    return ins

def repW(w): # all words from replacing 1 char
    rep=[]
    for ch in range(ord('a'),ord('z')+1):
        for i in range(len(w)):
            rep.append(w[:i]+chr(ch)+w[i+1:])
    return rep

edit = lambda w: delW(w)+insW(w)+repW(w) # all 1 char variations/misspells of a word

def probab(w,c): # P(W=w|C=c)
    a,b=1,0.9
    if(valid(w)):
        return a if(w==c) else 0
    else:
        return b if(c in validW(edit(w))) else 0

def spellCheck(w): # Naive Bayesian Classifier
    max,cw,Cw=0,w,edit(w)
    for c in Cw:
        p = probab(w,c)*P(c)
        if(max<p):
            max,cw=p,c
    return cw

text = dataGen()