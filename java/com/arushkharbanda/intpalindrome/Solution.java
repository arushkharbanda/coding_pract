package com.arushkharbanda.intpalindrome;


import java.util.ArrayList;
import java.util.Date;
import java.lang.Math;
import java.util.LinkedList;

class Solution {
    private ArrayList list;
    Solution()
    {
        list=new ArrayList();
    }
    public boolean isPalindrome(int x) {
        if(x<0)
            return false;

        int i=0;
        while(x>0)
        {
            int last=x%10;
            list.add(last);
            x=(int)Math.floor(x/10);
            i++;
        }
        int s=list.size();
        for (int j=0; j<(s/2);j++)
        {
            if (list.get(s-j-1)!=list.get(j))
            {
                return false;
            }
        }
        return true;
    }


    public static void main(String args[]) {

        check(121,true);
        check(-121,false);
        check(10,false);
        check(Integer.MAX_VALUE,false);
        check(Integer.MIN_VALUE,false);




    }

    public static void check(int a, boolean b) {
        Solution sol = new Solution();
        long start = new Date().getTime();
        boolean output = sol.isPalindrome(a);
        long end = new Date().getTime();
        long time = end - start;
        print(String.format("output %s for '%s' expected %s in %d", output, a, b, time));
        assert (output == b);
    }

    public static void print(String s) {
        System.out.println(s);
    }
}