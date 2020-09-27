package com.arushkharbanda.atoi;


import java.util.Date;
class Solution {
    public int myAtoi(String str) {
        //Discard whitespaces at the start
        int sol = 0;
        boolean negative = false;
        while (str.length() > 0 && str.charAt(0) == ' ') {
            str = str.substring(1);
        }

        if (str.length() > 0) {
            char pop = str.charAt(0);
            if (pop == '-') {
                negative = true;
                str = str.substring(1);
            }
            if (pop == '+') {
                str = str.substring(1);
            }
        }
        //Check if a char is in range 0-9
        while (str.length() > 0 && str.charAt(0) >= '0' && str.charAt(0) <= '9') {
            if (str.length() > 0){
                //Check if int max and min are not exceeded
                if (sol == Math.floor(Integer.MAX_VALUE / 10)) {
                    if (negative) {

                        if (str.charAt(0) > '8') {
                            return Integer.MIN_VALUE;
                        }

                    } else {
                        if (str.charAt(0) > '7') {
                            return Integer.MAX_VALUE;
                        }
                    }

                } else if (sol > Math.floor(Integer.MAX_VALUE / 10)) {

                    if (negative) {
                        return Integer.MIN_VALUE;

                    } else {
                        return Integer.MAX_VALUE;
                    }
                }
            }

            //multiply sol by 10 and add the new character
            sol = sol * 10 + (str.charAt(0) - '0');

            //remove the first char from str
            str = str.substring(1);

        }
        if (negative) {sol = sol * -1; }

        return sol;
    }


    public static void main(String args[]) {

        /*check("42",42);
        check("+1",1);
        check("-+1",0);
        check("   -42",-42);
        check("4193 with words",4193);
        check("words and 987",0);
        check("-91283472332",-2147483648);
        check("",0);
        check("2147483646", 2147483646);
        check(" -1010023630o4", -1010023630);*/
        check("-2147483648",-2147483648);
        check("-2147483647",-2147483647);



    }

    public static void check(String a, int b) {
        Solution sol = new Solution();
        long start = new Date().getTime();
        int output = sol.myAtoi(a);
        long end = new Date().getTime();
        long time = end - start;
        print(String.format("output %s for '%s' expected %s in %d", output, a, b, time));
        assert (output == b);
    }

    public static void print(String s) {
        System.out.println(s);
    }
}