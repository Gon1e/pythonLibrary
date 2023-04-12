import pandas as pd

# DataFrame() 함수로 데이터프레임 변환. 변수 df에 저장
exam_data = {'이름' : ['서준', '우현', '인아'],
             '수학' : ['90', '80', '70'],
             '영어' : ['98', '89', '95'],
             '음악' : ['85', '95', '100'],
             '체육' : ['100', '90', '90']}
df = pd.DataFrame(exam_data)
print(df)
print(type(df))
print('\n')

# '수학' 점수 데이터만 선택. 변수 math1에 저장
math1 = df['수학']
print(math1)
print(type(math1))
print('\n')

# '영어' 점수 데이터만 선택. 변수 english에 저장
english = df.영어
print(english)
print(type(english))

# '음악', '체육' 점수 데이터를 선택. 변수 music_gym에 저장
music_gym = df[['음악', '체육']]
print(music_gym)
print(type(music_gym))
print('\n')

# '수학' 점수 데이터만 선택. 변수 math2에 저장
math2 = df[['수학']]
print(math2)
print(type(math2))

# 모든 데이터 프레임에 대하여 2행 간격으로 실행
print(df.iloc[::2])

# 데이터 프레임 df의 0행부터 2행까지 2행 간격으로 선택
print(df.iloc[:3:2])

# 모든 데이터 프레임에 대하여 역순으로 실행
print(df.iloc[::-1])
