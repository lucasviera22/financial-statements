import requests
import matplotlib as plt

api_key = open('api-key', 'r').read()

company = "FB"
years = 2

income_statement = request.get(f"https://financialmodelingprep.com/api/v3/income-statement/{company}?limit={years}(&apikey={api_key}")

income_statement = income_statement.json()

print(income_statement[0]['revenue'])
print(income_statement[0]['grossProfit'])
print(income_statement[0]['eps'])
print(income_statement[0]['ebitda'])