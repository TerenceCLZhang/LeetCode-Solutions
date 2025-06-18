function ListNode(key, val, next) {
  this.key = key === undefined ? 0 : key;
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}

var MyHashMap = function () {
  this.length = 1000;
  this.map = new Array(this.length).fill(0).map(() => new ListNode());
};

MyHashMap.prototype.hash = function (key) {
  return key % this.length;
};

/**
 * @param {number} key
 * @param {number} value
 * @return {void}
 */
MyHashMap.prototype.put = function (key, value) {
  let curr = this.map[this.hash(key)];
  while (curr.next) {
    if (curr.next.key === key) {
      curr.next.val = value;
      return;
    }
    curr = curr.next;
  }
  curr.next = new ListNode((key = key), (val = value));
};

/**
 * @param {number} key
 * @return {number}
 */
MyHashMap.prototype.get = function (key) {
  let curr = this.map[this.hash(key)];
  while (curr.next) {
    if (curr.next.key === key) return curr.next.val;
    curr = curr.next;
  }
  return -1;
};

/**
 * @param {number} key
 * @return {void}
 */
MyHashMap.prototype.remove = function (key) {
  let curr = this.map[this.hash(key)];
  while (curr.next) {
    if (curr.next.key === key) {
      curr.next = curr.next.next;
      return;
    }
    curr = curr.next;
  }
};

/**
 * Your MyHashMap object will be instantiated and called as such:
 * var obj = new MyHashMap()
 * obj.put(key,value)
 * var param_2 = obj.get(key)
 * obj.remove(key)
 */
