from openpyxl import load_workbook
from datetime import datetime


def write_login_status(
        file_path,
        row,
        status,
        sheet_name="Sheet1",
        flag="N"
):

    workbook = load_workbook(
        file_path,
        keep_vba=True
    )

    sheet = workbook[sheet_name]

    now = datetime.now()

    sheet[f"E{row}"] = now.strftime("%Y-%m-%d")
    sheet[f"F{row}"] = now.strftime("%H:%M:%S")
    sheet[f"G{row}"] = status
    sheet[f"H{row}"] = flag

    workbook.save(file_path)