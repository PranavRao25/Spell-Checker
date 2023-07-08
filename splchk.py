import re

class SpellChecker:
    text={}
    def __init__(self):
        with open('gutenberg.txt') as f:
            for line in f.readlines():
                for w in re.sub(r'^\W+|\W+$','',line.strip(),re.IGNORECASE).lower().split(' '):
                    w = re.sub(r'^\W+|\W+$','',w,re.IGNORECASE)
                    if(w!='' and w.isalpha()):
                        self.text[w] = (self.text[w]+1) if(w in self.text.keys()) else 0
    
    _valid = lambda self,word: (word in self.text.keys())
    _validW = lambda self,L: list({w for w in L if(self._valid(w))})
    _P = lambda self,w: self.text[w]/sum(self.text.values()) if self._valid(w) else 0

    _delW = lambda self,w: [w[:i]+w[i+1:] for i in range(len(w))]
    _cycle = lambda self,w: [w[i+1:]+w[:i+1] for i in range(len(w)-1)]

    def _perm(self,w):
        p=[]
        for i in range(len(w)-1):
            for j in range(i+1,len(w)):
                p.append(w[:i]+w[j]+w[i+1:j]+w[i]+w[j+1:])
        return p

    def _insW(self,w):
        ins=[]
        for ch in range(ord('a'),ord('z')+1):
            for i in range(-1,len(w)):
                ins.append(w[:i+1]+chr(ch)+w[i+1:])
        return ins

    def _repW(self,w):
        rep=[]
        for ch in range(ord('a'),ord('z')+1):
            for i in range(len(w)):
                rep.append(w[:i]+chr(ch)+w[i+1:])
        return rep

    _edit = lambda self,w: self._delW(w)+self._insW(w)+self._repW(w)+self._perm(w)+self._cycle(w)

    def _probab(self,w,c,Fw,Gw):
        a,b=1,0.9
        if(self._valid(w)):
            return a if(w==c) else 0
        else:
            if(len(Fw)):
                return b if(c in Fw) else 0
            else:
                return g if(c in Gw) else 0

    def spellCheck(self,w):
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

spl = SpellChecker()
