package com.arushkharbanda.copyrandomlist;

// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}


class Solution {
    public Node copyRandomList(Node head) {
        Node curr_old=head;
        Node curr_new=null;
        Node newhead=null;
        while(true)
        {
            if (curr_old==null)
            {
                break;
            }
            Node newnode=new Node(curr_old.val);
            if (newhead==null)
            {
                newhead=newnode;
                curr_new=newhead;
            }
            else{
                curr_new.next=newnode;

            }
            curr_old=curr_old.next;
            curr_new=curr_new.next;
        }
        

        return newhead;
    }

    showList();
}