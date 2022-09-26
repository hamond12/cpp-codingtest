# 부품 개수 및 부품 번호 입력받기

n = int(input())  # 가지고 있는 부품 수
goods = list(map(int, input().split()))  # 소유한 부품 번호 목록
m = int(input())  # 요청한 부품 수
wants = list(map(int, input().split()))  # 손님이 원하는 부품 번호 목록


# 가게 부품 번호 기록

# goods의 최대 크기 만큼 부품리스트 0으로 초기화
p_list = [0]*1000000  
# goods리스트의 요소에 해당하는 번지를 모두 1로 초기화
for part in goods:
    p_list[part] = 1


# 손님이 요청한 부품 번호 확인

for part in wants:  # part->wants 번호 목록
    if p_list[part] != 1:  # 손님이 원하는 부품번호가 goods에 없다면
        print("no", end=" ")  # 개행 대신 공백으로 'no'출력
    else:
        print("yes", end=" ")
