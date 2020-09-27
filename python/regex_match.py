from datetime import datetime
from math import floor

#verbose=True
verbose=False
def debug(msg):
    if verbose:
        print(msg)

class Solution:

    # handles .
    def match(self,s,p):
        if p==".":
            return True
        if p==s:
            return True
        return False


    def isMatch(self, s: str, p: str) -> bool:
        strPos=len(s)-1;
        regexPos=len(p)-1;

        while(strPos>=0 or regexPos>=0 ):
            # Reverse Traversal over regex and on demand over string
            if(regexPos<0):
                return False;

            if(strPos<0):
                return False;
            regex=p[regexPos]
            str=s[strPos]


            # handles *
            if (regex=='*'):
                regexstringtoToMatch=p[regexPos-1]
                #debug("Matching string {} against regex {} result {}".format(str,regexstringtoToMatch, self.match(str,regexstringtoToMatch)))
                if self.match(str,regexstringtoToMatch):
                    debug("Matched string {} against regex {} result {}".format(str,regexstringtoToMatch, self.match(str,regexstringtoToMatch)))
                    strPos=strPos-1
                    if strPos==-1 and regexPos==1:
                        return True;
                    continue
                else:
                    regexPos=regexPos-2
                    continue
            else:
                regexPos=regexPos-1
            strPos=strPos-1

            debug("Matching string {} against regex {} result {}".format(str,regex, self.match(str, regex)))

            if not self.match(str, regex):
                return False
            if (regexPos==-1 ) ^ (strPos==-1 ):
                return False



        return True

sol=Solution()

def check(a,b,c):
    dt = datetime.now()
    start=dt.microsecond
    output=sol.isMatch(a, b)
    dt = datetime.now()
    end=dt.microsecond
    print("output {} for {}-{} expected {} took time {}".format(output,a,b,c,(end-start)))
    #assert(output==c)


#check("aa","a",False)
#check("aa","a*",True)
#check("ab",".*",True)
check("aab","c*a*b",True)
#check("mississippi","mis*is*p*.",False)
#check("mississippi","mis*is*ip*.",True)
#check("abcd","d*",False)
#check("abc","0abc",False)
#check("a",".*..a*",False)

