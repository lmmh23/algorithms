function solution(babbling) {
  const canSpeak = ["aya", "ye", "woo", "ma"];

  return babbling.reduce((possible, babbl, index) => {
    for (let i = 0; i < canSpeak.length; i += 1) {
      if (babbl.includes(canSpeak[i].repeat(2))) return possible;
    }

    for (let i = 0; i < canSpeak.length; i += 1) {
      // console.log(babbl.split(canSpeak[i]))
      // console.log(babbl.split(canSpeak[i]).join(' '))
      babbl = babbl.split(canSpeak[i]).join(' ').trim();
    }

    if (babbl) return possible;

    return possible += 1;
  }, 0)
}

// solution(["aya", "yee", "u", "maa"]);
// solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]);
// solution(["woowo"])
// solution(["yayae"]);
// solution(["mawoo"]);
solution(["ayayeaya"]);