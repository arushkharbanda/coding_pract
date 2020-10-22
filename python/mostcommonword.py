from util import check
import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned) -> str:
        # store banned words in set
        s=set(banned)
        count={}

        # loop for all words in para
        for x in re.split("[!?',;. ]", paragraph):
            if not x=='':
                # convert word to lower case
                x=x.lower()

                # remove punch from words Punc - !?',;.
                #x=re.sub("[!?',;.]","",x)

                # add to dict with counter
                if x in count.keys():
                    count[x]+=1
                else:
                    count[x]=1

        # find max
        max_count=0
        max_str=""
        for k in count.keys():
            v=count[k]
            # check against set
            if k not in s:
                if v>max_count:
                        max_count=v
                        max_str=k
        return max_str

sol=Solution()
check(['Bob hit a ball, the hit BALL flew far after it was hit.',['hit']],['ball'], sol.mostCommonWord)