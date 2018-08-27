
function rot13(str) { // LBH QVQ VG!
  var decoded = [];
  for (var i = 0; i < str.length; i++) {
    var coded = str[i].charCodeAt(0);
    if (coded < 65) {
      decoded.push(String.fromCharCode(coded));
    } else if (coded + 13 > 90) {
      decoded.push(String.fromCharCode(coded - 13));
    } else {
      decoded.push(String.fromCharCode(coded + 13));
    }
  }
  return decoded.join('');
}

rot13("SERR PBQR PNZC") // should decode to "FREE CODE CAMP"
rot13("SERR CVMMN!") // should decode to "FREE PIZZA!"
rot13("SERR YBIR?") // should decode to "FREE LOVE?"
rot13("GUR DHVPX OEBJA QBT WHZCRQ BIRE GUR YNML SBK.") // should decode to "THE QUICK BROWN DOG JUMPED OVER THE LAZY FOX."
