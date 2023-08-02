import pandas as pd

# 행 인데스/열 이름 지정하여 데이터프레임 만들기
df = pd.DataFrame([[15, '남', '덕양중'], [17, '여', '수리중']],
                   index = ['준서', '예은'],
                   columns = ['나이', '성별', '학교'])

# 데이터프레임 df 출력
print(df)
print('\n')

# 열 이름 중, '나이'를 '연령'으로, '성별'을 '남녀'로, '학교'를 '소속'으로 바꾸기
df.rename(columns={'나이':'연령', '성별':'남녀', '학교':'소속'}, inplace=True)

# df 출력 (변경 후)
print(df)