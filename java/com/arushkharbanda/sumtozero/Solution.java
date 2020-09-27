package com.arushkharbanda.sumtozero;

import java.util.Date;
import java.util.HashSet;
import java.util.List;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {

    }


    public static void main(String args[]) {

        check([-1,0,1,2,-1,-4],[[-1,-1,2],[-1,0,1]]);
        check("-2147483647",-2147483647);



    }

    public static void check(int [] a, List<List<Integer>> b) {
        Solution sol = new Solution();
        long start = new Date().getTime();
        List<List<Integer>> output = sol.threeSum(a);
        long end = new Date().getTime();
        long time = end - start;
        print(String.format("output %s for '%s' expected %s in %d", output, a, b, time));
        assert (output == b);
    }

    public static void print(String s) {
        System.out.println(s);
    }

}