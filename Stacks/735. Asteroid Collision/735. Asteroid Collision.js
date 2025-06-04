/**
 * @param {number[]} asteroids
 * @return {number[]}
 */
var asteroidCollision = function (asteroids) {
  let stack = [];

  for (let a of asteroids) {
    while (stack && a < 0 && stack.at(-1) > 0) {
      if (Math.abs(a) === Math.abs(stack.at(-1))) {
        stack.pop();
        a = 0;
      } else if (Math.abs(a) > Math.abs(stack.at(-1))) {
        stack.pop();
      } else {
        a = 0;
      }
    }

    if (a !== 0) stack.push(a);
  }

  return stack;
};

// Time: O(n)
// Space: O(n)
