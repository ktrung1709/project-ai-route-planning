import xlrd
import json

def read_from_excel_file(filename):
    # To open Workbook
    wb = xlrd.open_workbook(filename)
    sheet = wb.sheet_by_index(0)
    city_map = {}
    row = 1
    while row < sheet.nrows:
        start_city = sheet.cell_value(row,0)
        city_map[start_city] = {}
        while sheet.cell_value(row,1) != '.':
            dest_city = sheet.cell_value(row,1)
            city_map[start_city][dest_city] = sheet.cell_value(row,2)
            row +=1
        row += 1
    return city_map
def read_from_json_file(filename):
    f = open(filename)
    data = json.load(f)
    for city in data:
        for neighbor in data[city]:
            data[city][neighbor] = float(data[city][neighbor])
    return data