// Return True if str is palindrome
function palindrome(str) {
  str = str.toLowerCase().replace(/\W+|_+/g, '');
  return str == str.split('').reverse().join('');
}

// Return the length of the longest word
function findLongestWord(str) {
  str = str.split(' ');
  var len = 0;
  for (i = 0; i < str.length; i++) {
    if (len < str[i].length) {
      len = str[i].length;
    }
  }
  return len;
}

findLongestWord("The quick brown fox jumped over the lazy dog");

// Title case a sentence
function titleCase(str) {
  str = str.toLowerCase().split(' ');
  for (var i = 0; i < str.length; i++) {
    str[i] = str[i].charAt(0).toUpperCase() + str[i].substr(1);
  }
  return str.join(' ');
}

titleCase("I'm a little tea pot");

// Get largest int of every subarray
function largestOfFour(arr) {
  var maxVals = [];
  for (var i = 0; i < arr.length; i++) {
    console.log(arr[i]);
    maxVals.push(Math.max(...arr[i]));
  }
  return maxVals;
}

largestOfFour([[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]]);

// Check if a string (first argument, str) ends with the given target string
function confirmEnding(str, target) {
  return target == str.substr(-target.length, target.length);
}

confirmEnding("Bastian", "n");
confirmEnding("Open sesame", "same");

// Repeat string x num of times
function repeatStringNumTimes(str, num) {
  if (num < 0) {
    return '';
  } else {
    return str.repeat(num);
  }
}

repeatStringNumTimes("abc", 3);


