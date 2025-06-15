/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function (fn) {
  const groups = {};

  for (const item of this) {
    key = fn(item);
    groups[key] ||= [];
    groups[key].push(item);
  }

  return groups;
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */
