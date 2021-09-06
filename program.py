#pip install xlrd
#-*- encoding: utf8 -*-
import sys
import ast
import pandas as pd

# 검색어 입력 -> 예비, 경기, IT

# 반드시 포함(must) -> 예비, 경기 (!)
# 포함하면 좋음(has) -> IT, 기술 (*) 

print(sys.argv)
print(len(sys.argv))

filepath = sys.argv[1]
must = []
has = []

df = pd.read_excel(filepath, index_col='번호', header=2)
#print(df)

for i in range(2, len(sys.argv)):
    if(sys.argv[i].startswith('!')):
        #must.append(sys.argv[i][1:])
        must = [x.strip() for x in sys.argv[i][1:].split(',')]
    elif(sys.argv[i].startswith('*')):
        #has.append(sys.argv[i][1:])
        has = [x.strip() for x in sys.argv[i][1:].split(',')]
    else:
        print(sys.argv[i],'의 조건을 입력해주세요')

def containsAll(row, must):
    if(len(must) == 0): return True
    accept = True
    for word in must:
        if not row.str.contains(word).any():
            return False
    return accept

def containsSome(row, has):
    if(len(has) == 0): return True
    accept = False
    for word in has:
        if row.str.contains(word).any():
            return True
    return accept

def searchXLS(must, has):
    df['must'] = df.apply(lambda row: True if containsAll(row, must) else False, axis=1)
    df['has'] = df.apply(lambda row: True if containsSome(row, has) else False, axis=1)
    print(df)
    df.apply(lambda row: print(row['지원사업명'], row['상세 URL']) if row['must']==True and row['has']==True else False, axis=1)

searchXLS(must, has)
print('모두 포함:',must)
print('하나이상 포함:',has)
