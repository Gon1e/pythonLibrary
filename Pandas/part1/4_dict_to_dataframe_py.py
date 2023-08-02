import pandas as pd

# 열이름을 key로 하고, 리스트를 values로 갖는 딕셔너리 정의(2차원 배열)
dict_data = {'c0' : [0,1,2], 'c1' : [3,4,5], 'c2' : [6,7,8], 'c3' : [9,10,11], 'c4' : [12, 13, 14]}

# 판다스 DataFrame() 함수로 딕셔너리를 데이터프레임으로 변환. 변수 df에 저장
df = pd.DataFrame(dict_data)

# df의 자료형 출력
print(type(df))
print('\n')
# 변수 df에 저장되어 있는 데이터프레임 객체를 출력
print(df)