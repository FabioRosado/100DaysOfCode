// Write a function called add7 that takes one number and returns that number + 7.
// Write a function called multiply that takes 2 numbers and returns their product.
// Write a function called capitalize that takes a string and returns that string with only the first letter capitalized. Make sure that it can take strings that are lowercase, UPPERCASE or BoTh.
// Write a function called lastLetter that takes a string and returns the very last letter of that string:
// lastLetter("abcd") should return "d"

let add7 = (number) => number + 7;

let multiply = (number1, number2) => number1 * number2;

function capitalize(str) {
  str = str.toLowerCase().split(' ');
  for (var i = 0; i < str.length; i++) {
    str[i] = str[i].charAt(0).toUpperCase() + str[i].substr(1);
  }
  return str.join(' ');
}

let lastLetter = (str) => str.substr(-1, 1);

