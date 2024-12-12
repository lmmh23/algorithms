function numToRank(num) {
  switch (num) {
    case 6:
      return 1;
    case 5:
      return 2;
    case 4:
      return 3;
    case 3:
      return 4;
    case 2:
      return 5;
    default:
      return 6;
  }
}

function solution(lottos, win_nums) {
  const excludeDirty = lottos.filter((a) => a !== 0);
  const numOfDirty = lottos.length - excludeDirty.length;

  let correct = 0;
  for (let i = 0; i < win_nums.length; i++) {
    for (let j = 0; j < excludeDirty.length; j++) {
      if (win_nums[i] === excludeDirty[j]) {
        correct++;
      }
    }
  }

  return [numToRank(correct + numOfDirty), numToRank(correct)];
}