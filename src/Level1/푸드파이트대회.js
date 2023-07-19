function solution(food) {
  console.log(food.reverse());
  return food.reverse().reduce((acc, cur, idx) => {
      const calorie = (food.length - idx - 1).toString();
      const repeatedFood = calorie.repeat(parseInt(cur / 2));
      return repeatedFood + acc + repeatedFood;
  }, '0');
}
solution([1, 3, 4, 6]);
// solution([1, 7, 1, 2]);