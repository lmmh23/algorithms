function solution(keymap, targets) {
  var answer = Array(targets.length).fill(0);

  targets.forEach((target, index) => {
    let numofTouch = [];

    for (let i = 0; i < target.length; i++) {
      numofTouch = [];  // 초기화
      keymap.forEach(key => {
        
        key.indexOf(target[i]) !== -1
          && numofTouch.push(key.indexOf(target[i]) + 1);
      });
      if (numofTouch.length !== 0) {
        answer[index] += Math.min(...numofTouch);
      } else {
        answer[index] = -1;
        break;
      }
      
    }
  });
  return answer;
}


// solution(["ABACD", "BCEFD"], ["ABCD", "AABB"]); // [9, 4]
// solution(["AA"], ["B"]); // [-1]
// solution(["AGZ", "BSSS"], ["ASA", "BGZ"]) // [4, 6]
solution(["AAAAAAA", "AAAAAA"], ["ASA", "ASTT"]); // [-1, -1]


function solution2(keymap, targets) {
  const answer = [];
  const map = {};
  

  for (const items of keymap) {
    items.split('').map((item, index) => {
      map[item] = (map[item] < index+1 ? map[item] : index + 1)
    })
  }
  for (const items of targets) {
    answer.push(items.split('').reduce((cur, item) => {
      console.log("cur, map[item]", cur, map[item]);
      return cur += map[item];
    }, 0) || -1)
  }

  console.log(answer);
  
}

solution2(["ABACD", "BCEFD"], ["ABCD", "AABB"]); // [9, 4]
