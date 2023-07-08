import re

class SpellChecker: # Spell Checker Class
    text={} # freq table with keys as words, values as freq
    
    def __init__(self): # creating the dataset
        with open('gutenberg.txt') as f: # text corpus used for valid words
            for line in f.readlines(): # data formatting
                for w in re.sub(r'^\W+|\W+$','',line.strip(),re.IGNORECASE).lower().split(' '):
                    w = re.sub(r'^\W+|\W+$','',w,re.IGNORECASE)
                    if(w!='' and w.isalpha()): # only lower alphabetic
                        self.text[w] = (self.text[w]+1) if(w in self.text.keys()) else 0
    
    _valid = lambda self,word: (word in self.text.keys()) # if the given word is valid
    _validW = lambda self,L: list({w for w in L if(self._valid(w))}) # valid words from a list
    _P = lambda self,w: self.text[w]/sum(self.text.values()) if self._valid(w) else 0 # P(W=w)

    _delW = lambda self,w: [w[:i]+w[i+1:] for i in range(len(w))] # all words from deleting 1 char
    _cycle = lambda self,w: [w[i+1:]+w[:i+1] for i in range(len(w)-1)] # all cyclic permutations of a word

    def _swap(self,w): # all swaps of a word
        p=[]
        for i in range(len(w)-1):
            for j in range(i+1,len(w)):
                p.append(w[:i]+w[j]+w[i+1:j]+w[i]+w[j+1:])
        return p

    def _insW(self,w): # all words from inserting 1 char
        ins=[]
        for ch in range(ord('a'),ord('z')+1):
            for i in range(-1,len(w)):
                ins.append(w[:i+1]+chr(ch)+w[i+1:])
        return ins

    def _repW(self,w): # all words from replacing 1 char
        rep=[]
        for ch in range(ord('a'),ord('z')+1):
            for i in range(len(w)):
                rep.append(w[:i]+chr(ch)+w[i+1:])
        return rep

    # all 1 char variations/misspells of a word
    _edit = lambda self,w: self._delW(w)+self._insW(w)+self._repW(w)+self._swap(w)+self._cycle(w)

    def _probab(self,w,c,Fw,Gw): # P(W=w|C=c)
        a,b=1,0.9
        if(self._valid(w)):
            return a if(w==c) else 0
        else:
            if(len(Fw)):
                return b if(c in Fw) else 0
            else:
                return g if(c in Gw) else 0

    def spellCheck(self,w): # Naive Bayesian Classifier
        max,cw,Cw=0,w,self._edit(w)
        Fw,Gw=self._validW(Cw),set()

        for i in Cw:
            Gw.update(set(self._validW(self._edit(i))))
        Gw = list(Gw)

        for c in Cw:
            p = self._probab(w,c,Fw,Gw)*self._P(c)
            if(max<p):
                max,cw=p,c
        return cw

spl = SpellChecker() # creating a spellchecker object
