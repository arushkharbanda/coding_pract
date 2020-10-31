from functools import reduce
from collections import defaultdict
from util import check, debug
from datetime import datetime
from collections import deque

class Solution:
    def makeTrie(self, words):
        _end = '_end_'
        root = dict()
        for word in words:
            current_dict = root
            for letter in word:
                current_dict = current_dict.setdefault(letter, {})
            current_dict[_end] = word
        return root

    def findWords_rec(self,res,oldc,point, trie, board, l1,l2):

        if '_end_' in trie:
            res.add(trie['_end_'])
        lastpoint=point
        x,y=lastpoint
        board[x][y]=""
        neighbours=[(-1,0), (1,0),(0,-1),(0,1)]
        for ne in neighbours:
            xd,yd=ne
            newp=(x+xd,y+yd)
            if x+xd>-1 and y+yd>-1 and x+xd<l1 and y+yd<l2 :
                newc=board[x+xd][y+yd]
                if newc in trie:
                    self.findWords_rec(res,newc,newp,trie[newc], board, l1,l2)
        board[x][y]=oldc


    def findWords(self, board, words):
        res=set()
        trie=self.makeTrie(words)
        l1=len(board)

        if l1>0:
            l2=len(board[0])
        else:
            l2=0
        for i in range(l1):
            for j in range(l2):
                newc=board[i][j]
                if newc in trie:
                    self.findWords_rec(res,newc,(i,j),trie[newc],board, l1,l2)
        return res

sol=Solution()
check([[['o','a','a','n'],['e','t','a','e'],['i','h','k','r'],['i','f','l','v']],["oath","pea","eat","rain"]],[ {"eat","oath"}],sol.findWords)
check([[["a","a"]],["a"]],[{"a"}],sol.findWords)
check([[["b","b","a","a","b","a"],["b","b","a","b","a","a"],["b","b","b","b","b","b"],["a","a","a","b","a","a"],["a","b","a","a","b","b"]],["abbbababaa"]],[{"abbbababaa"}],sol.findWords)
check([[["a","b"],["a","a"]],["aba","baa","bab","aaab","aaa","aaaa","aaba"]],[{"aaab","aaa","aaba","aba","baa"}],sol.findWords)
check([[["a","a"]],["aaa"]],[set()],sol.findWords)