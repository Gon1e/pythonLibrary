import pandas as pd

# DataFrame() 함수로 데이터프레임 변환. 변수 df에 저장
exam_data = {'이름' : ['서준', '우현', '인아'],
             '수학' : ['90', '80', '70'],
             '영어' : ['98', '89', '95'],
             '음악' : ['85', '95', '100'],
             '체육' : ['100', '90', '90']}
df = pd.DataFrame(exam_data)

# 데이터프레임 df의 특정 원소를 변경하는 방법: '서준'의 '체육' 점수
df.iloc[0] [3] = 80
print(df)
print('\n')

df.loc

