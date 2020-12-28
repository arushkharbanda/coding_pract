from util import check
from collections import deque
class Solution:
    def createTrie(self, wordList):
        t={}
        self.END='__END__'
        for word in wordList:
            current=t
            for letter in word:
                if letter not  in current:
                    current[letter]={}
                current=current[letter]
            current[self.END]=word
        return t

    def hasWord(self, t, word):
        current=t
        for letter in word:
            if letter in current:
                current=current[letter]
            else:
                return False
        if self.END in current:
            return True
        return False


    def getSimilar(self,t, word):
        if word in self.cache:
            return self.cache[word]
        else:
            result=self.getSimilar_rec(t,word)
            self.cache[word]=result
            return result

    def getSimilar_rec(self,t, word):
        self.wildchar='*'
        result=[]
        current=t
        for i,letter in enumerate(word):
            if letter==self.wildchar:
                for key in current.keys():
                    result.extend(self.getSimilar_rec(current[key], word[i+1:] ))
            elif letter in current:
                current=current[letter]
            else:
                return result
        if self.END in current:
            result.append(current[self.END])
            del current[self.END]
        return result

    def ladderLength(self, beginWord: str, endWord: str, wordList):
        self.t=self.createTrie(wordList)
        self.cache={}
        s=deque()
        s.append((1, beginWord))
        traversed={}
        while s:
            depth, ele=s.popleft()
            for i,letter in enumerate(ele):
                newWord=ele[:i]+"*"+ele[i+1:]
                children=self.getSimilar(self.t,newWord)
                for child in children:
                    if child==endWord:
                        return depth+1
                    if child not in traversed:
                        traversed[child] = True
                        s.append((depth+1,child))
        return 0

sol=Solution()
check(["hit","cog",["hot","dot","dog","lot","log","cog"]],[5],sol.ladderLength)
check(["hit","cog",["hot","dot","dog","lot","log"]],[0],sol.ladderLength)