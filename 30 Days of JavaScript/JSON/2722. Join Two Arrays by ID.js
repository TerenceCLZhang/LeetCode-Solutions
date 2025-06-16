/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function (arr1, arr2) {
  joined = {};

  for (const obj of arr1) {
    joined[obj.id] = obj;
  }

  for (const obj of arr2) {
    joined[obj.id] = { ...joined[obj.id], ...obj };
  }

  return Object.values(joined);
};
