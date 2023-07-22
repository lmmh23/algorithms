function solution(ingredient) {
  const stk = [];
  let cnt = 0;

  ingredient.forEach((ing, idx) => {
    stk.push(ing);

    if (stk.length >= 4) {
      const find = stk.slice(-4).join('');
      console.log(find);
      if (find === '1231') {
        stk.slice(-4);
        cnt++;
      }
    }
  })

  console.log(cnt);
  return cnt;
}

solution([2, 1, 1, 2, 3, 1, 2, 3, 1]);
solution([1, 3, 2, 1, 2, 1, 3, 1, 2]);