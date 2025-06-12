# 엑셀 파일을 생성하기 위해서 openpyxl의 Workbook 클래스
from openpyxl import Workbook

# 테두리 스타일을 위한 클래스
from openpyxl.styles import Border, Side

# 폰트 스타일을 위한 클래스
from openpyxl.styles import Font

# 텍스트 정렬을 위한 클래스
from openpyxl.styles import Alignment

# 폰트 종류
# name-폰트 이름 / size-폰트 크기 / bold-굵기 / italic-기울기 / underline-밑줄
Title_font = Font(name='Pretendard', size=24, bold=True)
Pretendard = Font(name='Pretendard', size=12)

Thin_border = Border(
    left = Side(style = 'thin'),
    right = Side(style = 'thin'),
    top = Side(style = 'thin'),
    bottom = Side(style = 'thin')
)

# 새 Workbook(엑셀 파일) 생성
xlsx = Workbook()

# 첫번째 워크시트 활성화
x1 = xlsx.active

# 셀 병합
x1.merge_cells('B2:H3')

# 데이터 입력
x1['B2'] = "좌석 배정표" # A1에 "이름" 문자열을 입력
x1['B2'].font = Title_font

# 가로 세로 가운데 정렬
x1['B2'].alignment = Alignment(horizontal='center', vertical='center')

# 테두리
for row in x1['B2:H3']:
    for cell in row:
        cell.border = Thin_border  # 각 셀에 테두리 적용

# 엑셀 파일 저장
xlsx.save("자리 배치 결과.xlsx")