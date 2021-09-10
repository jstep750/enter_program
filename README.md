# enter_program
https://www.bizinfo.go.kr/see/seea/selectSEEA100.do 에서 원하는 카테고리별로 검색하기

## Installation
The package needs excel file(지원사업조회.xls)
- Download excel file (https://www.bizinfo.go.kr/see/seea/selectSEEA100ExcelView.do)
- Download the repository
```
git clone https://github.com/enter_program
```

### Requirements
```
cd enter_program
pip install pandas
pip install xlrd
```

### Run Demo

![image](https://user-images.githubusercontent.com/48945057/132858948-a91eeac7-f3c8-4a3c-93db-d2f6c781a0bc.png)


```
cd enter_program
python program2.py 'C:\Users\user\enter_program\지원사업조회.xls' !예비 *서울,경기 *SW,테크,기술,IoT,스마트,과학
```
