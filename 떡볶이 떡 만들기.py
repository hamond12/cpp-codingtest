n, m = map(int, input().split())  # 떡의 개수, 요청한 떡의 길이
d = list(map(int, input().split()))  # 떡의 길이가 나열된 리스트

# 이진 탐색의 시작위치와 종료위치
start = 0
end = max(d)

# 절단기의 높이
cutter = 0

# 시작점이 종료위치보다 커지면 종료
while start <= end:

    # 절단기 높이 지정
    mid = (start+end)//2

    # 남은 떡 길이의 합계
    sum = 0

    # 절단기로 모든 떡을 잘랐을 때 남은 떡길이 계산
    for i in d:
        # 떡의 높이가 더 절단기보다 높을 떄만 자를 수 있다
        if i > mid:
            sum += i-mid  # sum에 자르고 남은 떡길이 추가

    # 요청한 떡의 길이보다 남은 떡 길이의 합이 작으면
    if sum < m:
        end = mid-1  # 절단기의 높이를 낮춰야함

    # 요청한 떡의 길이보다 남은 떡 길이의 합이 크면
    else:
        cutter = mid  # 절단기 높이를 기록하고
        start = mid+1  # 절단기 높이를 높여야한다

print(cutter)
