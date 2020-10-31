from datetime import datetime
from math import floor
from util import check

class Solution:

    # . case
    def match(self,s,p):
        if p==".":
            return True
        if p==s:
            return True
        return False

    def isMatch_old(self, s: str, p: str) -> bool:
        s1=[]
        s2=[]
        s1.extend(s)
        s2.extend(p)
        while len(s1)>0 or len(s2)>0:
            if len(s2)>0:
                ele=s2.pop()
            elif len(s1)==0 or len(s2)==0:
                return False

            # * case
            if ele=='*':
                e=s2.pop()
                while True:
                    if len(s1)>0:
                        last=s1[-1]
                        if not self.match(last,e):
                            break
                        else:
                            s1.pop()
                    else:
                        break


            else:
                if len(s1)>0:
                    e2=s1.pop()
                else:
                    return False
                if not self.match(e2,ele):
                    return False
        return True

    def isMatch(self, s, p):
        if not s and not p:
            return True

        if not p and s:
            return False

        if p[-1] == '*':
            rep = p[-2]
            if s and (s[-1] == rep or rep == '.'):
                return self.isMatch(s[:-1], p) or self.isMatch(s, p[:-2])
            else:
                return self.isMatch(s, p[:-2])
        else:
            if s and (p[-1] == s[-1] or p[-1] == '.'):
                return self.isMatch(s[:-1], p[:-1])
            else:
                return False


sol=Solution()
check(["aa","a"],[False], sol.isMatch)
check(["aa","a*"],[True], sol.isMatch)
check(["ab",".*"],[True], sol.isMatch)
check(["aab","c*a*b"],[True], sol.isMatch)
check(["mississippi","mis*is*p*."],[False], sol.isMatch)
check(["mississippi","mis*is*ip*."],[True], sol.isMatch)
check(["abcd","d*"],[False], sol.isMatch)
check(["abc","0abc"],[False], sol.isMatch)
check(["a",".*..a*"],[False], sol.isMatch)
check(["aaa","ab*a*c*a"],[True], sol.isMatch)



