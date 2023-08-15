const set_a_to_z = (str) => {
  return ((str.charCodeAt() + 1 - 97) % 26 + 97)
}

function solution(s, skip, index) {
  return s.split('').map(str => {
    let s = str
    for (let i = 0; i < index; i++) {

      s = String.fromCharCode(set_a_to_z(s));
      skip.indexOf(s) !== -1 && i--
    }
    // console.log(s);
    return s
  }).join('')
}

// solution("aukks", "wbqd", 5);




solution("klmnopqrstuvwxyz", "abcdefghij", 20)


function otherSolution(s, skip, index) {
  const alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
    "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
    "u", "v", "w", "x", "y", "z"].filter(c => !skip.includes(c));
  
  return s.split("").map(c => {
    console.log(alphabet[(alphabet.indexOf(c) + index) % alphabet.length]);
    return alphabet[(alphabet.indexOf(c) + index) % alphabet.length]
  }).join("")
}

console.log(otherSolution("aukks", "wbqd", 5));
