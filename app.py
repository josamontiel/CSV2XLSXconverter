import pandas


pd = pandas.read_csv('emp.csv')
writer = pandas.ExcelWriter('emp.xlsx')
pd.to_excel(writer, index=False)
writer.save()