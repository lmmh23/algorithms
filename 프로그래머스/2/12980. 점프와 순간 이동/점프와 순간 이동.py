def solution(n):
    ans = 0
    dp = [0] * 10
    dp[0] = 1
    dp[1] = 1
    dp[2] = 1
    dp[3] = 2
    dp[4] = 1
    dp[5] = 2

    while n > 5:
        if n % 2 == 0:
            n //= 2  
        else:
            ans += 1
            n = (n - 1) // 2

    ans += dp[n]
    return ans