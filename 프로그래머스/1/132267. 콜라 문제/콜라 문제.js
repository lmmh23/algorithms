function solution(a, b, n) {
    let answer = 0;
    while(n >= a) {
        const newBottles = Math.floor(n / a) * b;
        answer += newBottles;
        n = newBottles + (n % a);
    }
    return answer;
}

solution(2, 1, 20);
solution(3, 1, 20);