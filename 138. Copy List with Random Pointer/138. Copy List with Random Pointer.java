/*
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
*/

import java.util.HashMap;
import java.util.Map;

class Solution {

  public Node copyRandomList(Node head) {
    if (head == null) {
      return null;
    }

    Map<Node, Node> oldToNew =
      new HashMap<>();

    Node curr = head;
    while (curr != null) {
      Node newNode = new Node(curr.val);
      oldToNew.put(curr, newNode);
      curr = curr.next;
    }

    curr = head;
    while (curr != null) {
      Node newNode = oldToNew.get(curr);
      newNode.next = curr.next != null ? oldToNew.get(curr.next) : null;
      newNode.random = curr.random != null ? oldToNew.get(curr.random) : null;
      curr = curr.next;
    }

    return oldToNew.get(head);
  }
}
