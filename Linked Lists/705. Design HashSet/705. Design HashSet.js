function ListNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}

var MyHashSet = function () {
  this.size = 10 ** 4;
  this.set = new Array(this.size).fill(null).map(() => new ListNode());
};

/**
 * @param {number} key
 * @return {void}
 */
MyHashSet.prototype.add = function (key) {
  const index = key % this.size;
  let curr = this.set[index];
  while (curr.next) {
    if (curr.next.val === key) return;
    curr = curr.next;
  }
  curr.next = new ListNode(key);
};

/**
 * @param {number} key
 * @return {void}
 */
MyHashSet.prototype.remove = function (key) {
  const index = key % this.size;
  let curr = this.set[index];
  while (curr.next) {
    if (curr.next.val === key) {
      curr.next = curr.next.next;
      return;
    }
    curr = curr.next;
  }
};

/**
 * @param {number} key
 * @return {boolean}
 */
MyHashSet.prototype.contains = function (key) {
  const index = key % this.size;
  let curr = this.set[index];
  while (curr.next) {
    if (curr.next.val === key) {
      return true;
    }
    curr = curr.next;
  }
  return false;
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * var obj = new MyHashSet()
 * obj.add(key)
 * obj.remove(key)
 * var param_3 = obj.contains(key)
 */
