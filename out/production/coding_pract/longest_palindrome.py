class Solution:
    def longestPalindrome(self,s) :
        longest=""
        longest_len=0

        ls=[]
        for  c in enumerate(s):
            ls.append(c)
        while len(ls)>0:
            i,c=ls.pop()
            if (len(c)>longest_len):
                self.debug("found new longer palindrome {}".format(c))
                longest_len=len(c)
                longest=c
            if (len(c)==1):
                if i-1>=0:
                    str=s[i-1:len(c)+i]
                    self.debug("created {} from  {} ".format(str, c))
                    if self.isPalindrome(str):
                        ls.append((i-1,str))
                if i+len(c)+1<len(s):
                    str=s[i:len(c)+i+1]
                    self.debug("created {} from  {} ".format(str, c))
                    if self.isPalindrome(str):
                        ls.append((i,str))
            if i+len(c)+1<=len(s) and i-1>=0:
                str=s[i-1:len(c)+1+i]
                self.debug("created {} from  {} ".format(str, c))
                if s[i-1]==s[len(c)+i]:
                    self.debug("{} is a planindrome from logic".format(str))
                    ls.append((i-1,str))
                else:
                    pass
                    self.debug("{} is not a planindrome from logic".format(str))
            self.debug("current list {}".format(ls))
        return longest

    def isPalindrome(self,s):
        l=len(s)
        for i,c in enumerate(s):
            if c!=s[l-i-1]:
                self.debug("{} is not a planindrome from function".format(s))
                return False
        self.debug("{} is a planindrome".format(s))
        return True

    verbose=False

    def debug(self,msg):
        if self.verbose:
            print(msg)

sol=Solution()


def check(a,b):
    print("output {} expected {}".format(a,b))
    assert(a==b)



check(sol.longestPalindrome("abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa"),"abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa")
#check(sol.longestPalindrome("zeusnilemacaronimaisanitratetartinasiaminoracamelinsuez"),"zeusnilemacaronimaisanitratetartinasiaminoracamelinsuez")
#check(sol.longestPalindrome("abcdcba"),"abcdcba")
#check(sol.longestPalindrome("babad"),"aba")
#check(sol.longestPalindrome("abcba"),"abcba")
#check(sol.longestPalindrome("cbbd"),"bb")
#check(sol.longestPalindrome("abcdefedcba"),"abcdefedcba")
#check(sol.longestPalindrome("abcdefedcbaasdadas"),"abcdefedcba")
#check(sol.longestPalindrome("aaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzzyyyyyyyyyyxxxxxxxxxxwwwwwwwwwwvvvvvvvvvvuuuuuuuuuuttttttttttssssssssssrrrrrrrrrrqqqqqqqqqqppppppppppoooooooooonnnnnnnnnnmmmmmmmmmmllllllllllkkkkkkkkkkjjjjjjjjjjiiiiiiiiiihhhhhhhhhhggggggggggffffffffffeeeeeeeeeeddddddddddccccccccccbbbbbbbbbbaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzzyyyyyyyyyyxxxxxxxxxxwwwwwwwwwwvvvvvvvvvvuuuuuuuuuuttttttttttssssssssssrrrrrrrrrrqqqqqqqqqqppppppppppoooooooooonnnnnnnnnnmmmmmmmmmmllllllllllkkkkkkkkkkjjjjjjjjjjiiiiiiiiiihhhhhhhhhhggggggggggffffffffffeeeeeeeeeeddddddddddccccccccccbbbbbbbbbbaaaa"),"aaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzzyyyyyyyyyyxxxxxxxxxxwwwwwwwwwwvvvvvvvvvvuuuuuuuuuuttttttttttssssssssssrrrrrrrrrrqqqqqqqqqqppppppppppoooooooooonnnnnnnnnnmmmmmmmmmmllllllllllkkkkkkkkkkjjjjjjjjjjiiiiiiiiiihhhhhhhhhhggggggggggffffffffffeeeeeeeeeeddddddddddccccccccccbbbbbbbbbbaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzzyyyyyyyyyyxxxxxxxxxxwwwwwwwwwwvvvvvvvvvvuuuuuuuuuuttttttttttssssssssssrrrrrrrrrrqqqqqqqqqqppppppppppoooooooooonnnnnnnnnnmmmmmmmmmmllllllllllkkkkkkkkkkjjjjjjjjjjiiiiiiiiiihhhhhhhhhhggggggggggffffffffffeeeeeeeeeeddddddddddccccccccccbbbbbbbbbbaaaa")

