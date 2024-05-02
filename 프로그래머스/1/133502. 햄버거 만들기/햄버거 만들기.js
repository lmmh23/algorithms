function solution(ingredient) {
  const stk = [];
  let cnt = 0;

  ingredient.forEach((ing, idx) => {
    stk.push(ing);

    if (stk.length >= 4) {
      const find = stk.slice(-4).join('');
      if (find === '1231') {
        stk.splice(-4)
        cnt++;
      }
    }
  })
  return cnt;
}