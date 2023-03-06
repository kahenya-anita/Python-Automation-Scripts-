#Convert pdf to csv(comma separated values)
import tabula

filename = input("Enter File Path: ")
df = tabula.read_pdf(filename, encoding='utf-8', spreadsheet=True, pages='1')

df.to_csv('output.csv')