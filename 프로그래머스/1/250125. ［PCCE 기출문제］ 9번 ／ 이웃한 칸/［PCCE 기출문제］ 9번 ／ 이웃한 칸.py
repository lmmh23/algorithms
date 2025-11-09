def solution(board, h, w):
    n = len(board)
    answer = 0
    
    dh = [0,1,-1,0]
    dw = [1,0,0,-1]
    
    color = board[h][w]
    
    for i in range(len(dh)):
        h_check = h + dh[i]
        w_check = w + dw[i]
        if ((0 <= h_check < n) and (0 <= w_check < n) and (color == board[h_check][w_check])):
            answer+=1
    return answer