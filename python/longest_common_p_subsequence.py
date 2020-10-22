from util import check

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        # fill array
        arr_sub=[0 for a in range(len(s))]
        arr=[arr_sub.copy() for b in range(len(s))]

        # fill diagonal
        for i in range(0, len(s)):
            arr[i][i]=1

        # calculate array values
        for length in range(2, len(s)+1):
            for start in range(0,len(s)-length+1):
                end=start+length-1
                if s[start]==s[end]:
                    arr[start][end]=arr[start+1][end-1]+2
                else:
                    arr[start][end]=max(arr[start+1][end], arr[start][end-1])
        return arr[0][len(s)-1]

sol=Solution()
check(["bbbab"],[4],sol.longestPalindromeSubseq)
check(["cbbd"],[2],sol.longestPalindromeSubseq)
check(["abdbca"],[5],sol.longestPalindromeSubseq)
