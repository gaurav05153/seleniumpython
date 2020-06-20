# import openpyxl


class LoginPageData:
    test_LoginPage_correct_credentials_data = {"email_id": "gaurav05153@gmail.com", "password": "admin"}
    # we can add more elements of dictionary if we want to check with other data sets
    test_LoginPage_wrong_credentials_data = [{"email_id": "gaurav0505153@gmail.com", "password": "admin"},
                                             {"email_id": "gaurav05153@gmail.com", "password": "admin123"}]

    test_create_account_data = {"email_id": "gaurav051@gmail.com"}

    '''
    @staticmethod
    def getTestData(test_case_name):
        Dict = {}
        book = openpyxl.load_workbook("C:\\Users\\Owner\\Documents\\PythonDemo.xlsx")
        sheet = book.active
        for i in range(1, sheet.max_row + 1):  # to get rows
            if sheet.cell(row=i, column=1).value == test_case_name:

                for j in range(2, sheet.max_column + 1):  # to get columns
                    # Dict["lastname"]="shetty
                    Dict[sheet.cell(row=1, column=j).value] = sheet.cell(row=i, column=j).value
        return[Dict]
        '''
