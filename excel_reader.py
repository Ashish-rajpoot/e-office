from openpyxl import load_workbook

def get_user_id(file_path):
    workbook = load_workbook(file_path, keep_vba=True)
    sheet = workbook.active

    user_id = sheet["C2"].value

    workbook.close()
    return str(user_id)