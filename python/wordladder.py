from util import check
from collections import defaultdict
import re
from collections import deque
import collections
class Solution:

    def compileMapping(self, wordList):
        for word in wordList:
            for i in range(len(word)):
                before=word[:i]
                after=word[i+1:]
                key=before+'*'+after
                if key in self.mapping.keys():
                    self.mapping[key].append(word)
                else:
                    self.mapping[key]=[word]

    def getNeighbours(self, word):
        if word in self.m.keys():
            return self.m[word]
        else:
            self.m[word]=[]
            for i in range(len(word)):
                before=word[0:i]
                after=word[i+1:]
                key=before+"*"+after
                self.m[word].extend(self.mapping[key])

            return self.m[word]

    def ladderLength(self, beginWord: str, endWord: str, wordList):
        q=deque()
        result=[]
        self.mapping={}
        self.m={}
        if beginWord not in wordList:
            wordList.append(beginWord)
        traversed={word:0 for word in wordList}
        self.compileMapping(wordList)

        q.append((1,beginWord,[beginWord]))
        while len(q)>0:
            distance,ele, path=q.popleft();
            traversed[ele]=1

            neighbours=self.getNeighbours(ele)
            if endWord in neighbours:
                path.append(endWord)
                if len(result)==0 or (len(result)>0 and len(result[0])==len(path)):
                    result.append(path)
            else:
                for neighbour in neighbours:
                    if traversed[neighbour]!=1:
                        new_path=path.copy()
                        new_path.append(neighbour)
                        q.append((distance+1,neighbour, new_path))
        return result

sol=Solution()
check(["hit","cog",["hot","dot","dog","lot","log","cog"]],[[["hit","hot","dot","dog","cog"],
                                                            ["hit","hot","lot","log","cog"]]],sol.ladderLength)
check(["hit","cog",["hot","dot","dog","lot","log"]],[[]],sol.ladderLength)