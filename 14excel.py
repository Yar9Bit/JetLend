import pandas as pd


def read_excel_file(path_to_file):
    reader = pd.read_excel(path_to_file)
    return reader


def sum_amount_of_all_companies(func):
    dt = func[func['registration_date'] <= '2021']
    print(dt)
    dataframe_dict = {'amount': dt['amount']}
    dataframe = pd.DataFrame(dataframe_dict)
    agg_func = {'amount': 'sum'}
    return dataframe.agg(agg_func)


def sum_loans_for_rating(func):
    dataframe_dict = {'rating': [rating for rating in func['rating']],
                      'amount': [amount for amount in func['amount']],
                      }
    dataframe = pd.DataFrame(dataframe_dict)
    return dataframe.groupby('rating')['amount'].sum()


if __name__ == '__main__':
    file = 'csv/14excel.xlsx'
    func_read_excel_file = read_excel_file(file)
    print(sum_amount_of_all_companies(func_read_excel_file))
    print(sum_loans_for_rating(func_read_excel_file))
