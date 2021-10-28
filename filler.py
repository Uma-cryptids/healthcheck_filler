import openpyxl
import random


def btm(average):
    tmp = random.normalvariate(average, 0.1)
    while tmp < average - 1 or 37.5 <= tmp:
        tmp = random.normalvariate(average, 0.1)
    return tmp


ave = 0.0
while ave < 33.0 or 37.3 <= ave:
    ave = float(input(">>> 平均体温を入力してください。"))

book = openpyxl.load_workbook("healthcheck3_202109-202112.xlsx")
for sheet_title in book.sheetnames:
    sheet = book[sheet_title]
    for row in [3, 19]:
        for first_char in ["", "A"]:
            for second_char in range(65, 91):
                column = first_char+chr(second_char)
                column_for_check = first_char+chr(second_char+1)
                if column == "A":
                    continue
                if sheet[column+str(row)].value not in ["/", None]:
                    sheet[column+str(row+1)].value = round(btm(ave), 1)
                    sheet[column+str(row+2)].value = round(btm(ave), 1)
                    sheet[column_for_check+str(row+13)].value = "✓"
book.save("healthcheck3_202109-202112.xlsx")
print("Done!!")
