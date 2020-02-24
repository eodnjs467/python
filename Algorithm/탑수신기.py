def solution(heights):
    answer = [0]*len(heights)
    while heights:
        right = heights.pop()
        for idx in range(len(heights)-1, -1, -1):
            if heights[idx] > right:
                answer[len(heights)] = idx+1        # 위에서 pop 하니 줄어들게 됨 해당 인덱스를 추가
                break
    return answer
data = [6, 9, 5, 7, 4]
solution(data)

# 다른코드 : https://geonlee.tistory.com/122 참고해서 zip, math 라이브러리 사용법 익히기