// Return true if the string in the first element of the array
// contains all of the letters of the string in the second element of the array.
// Not very elegant

function mutation(arr) {
  arr[0] = arr[0].toLowerCase();
  arr[1] = arr[1].toLowerCase();

  var smaller = 0;
  var larger = 1;

  if (arr[0].length >= arr[1].length) {
    smaller = 1;
    larger = 0;
  }
  for (var i = 0; i < arr[smaller].length; i++) {
    if (!arr[larger].includes(arr[smaller][i])){
      return false;
    }
  } return true;
}

mutation(["hello", "hey"]) // should return false.
mutation(["hello", "Hello"]) // should return true.
mutation(["zyxwvutsrqponmlkjihgfedcba", "qrstu"]) // should return true.
mutation(["Mary", "Army"])  // should return true.
mutation(["Mary", "Aarmy"]) // should return true.
mutation(["Alien", "line"]) // should return true.
mutation(["floor", "for"]) // should return true.
mutation(["hello", "neo"]) // should return false.
mutation(["voodoo", "no"]) // should return false.

// Remove all falsy values from an array.

function bouncer(arr) {
  // Don't show a false ID to this bouncer.
  return arr.filter(arr => Boolean(arr) === true);
}

bouncer([7, "ate", "", false, 9])                  // should return [7, "ate", 9].
bouncer(["a", "b", "c"])                          // should return ["a", "b", "c"].
bouncer([false, null, 0, NaN, undefined, ""])    // should return [].
bouncer([1, null, NaN, 2, undefined])           // should return [1, 2].


// You will be provided with an initial array (the first argument in the destroyer function),
// followed by one or more arguments. Remove all elements from the initial array that are of
// the same value as these arguments.

function destroyer(arr) {
  var args = [].slice.call(arguments);
  var filtered = [];

  for (var i = 0; i < args[0].length; i++){
     if (!args.slice(1).includes(args[0][i])){
       filtered.push(args[0][i]);
    }
  }
  return filtered;
}

destroyer([1, 2, 3, 1, 2, 3], 2, 3) // should return [1, 1].
destroyer([1, 2, 3, 5, 1, 2, 3], 2, 3) // should return [1, 5, 1].
destroyer([3, 5, 1, 2, 2], 2, 3, 5) // should return [1].
destroyer([2, 3, 2, 3], 2, 3) // should return [].
destroyer(["tree", "hamburger", 53], "tree", 53) // should return ["hamburger"].

// Return the lowest index at which a value (second argument) should be inserted
// into an array (first argument) once it has been sorted. The returned value should be a number.

function compare(a, b){
  return a - b;
}

function getIndexToIns(arr, num) {
  arr.push(num);
  arr.sort(compare);
  return arr.indexOf(num);
}

getIndexToIns([10, 20, 30, 40, 50], 35) // should return 3.
getIndexToIns([10, 20, 30, 40, 50], 30) // should return 2.
getIndexToIns([40, 60], 50) // should return 1.
getIndexToIns([3, 10, 5], 3) // should return 0.
getIndexToIns([5, 3, 20, 3], 5) // should return 2.
getIndexToIns([2, 20, 10], 19) // should return 2.
getIndexToIns([2, 5, 10], 15) // should return 3.