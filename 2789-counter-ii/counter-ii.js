/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
  let currVal = init

  return {
    increment: function() {
        return currVal += 1
    },
    decrement: function() {
        return currVal -= 1
    },
    reset: function() {
        return currVal = init
    }
  }  
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */