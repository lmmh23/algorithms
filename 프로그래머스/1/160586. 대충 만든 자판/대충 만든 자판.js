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
      // console.log("numofTouch", numofTouch, "target: ", target[i]);
      if (numofTouch.length !== 0) {
        answer[index] += Math.min(...numofTouch);
      } else {
        answer[index] = -1;
        break;
      }
      
    }
  });
  console.log(answer);
  return answer;
}
