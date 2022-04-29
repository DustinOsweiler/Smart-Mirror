from urllib.request import urlopen
from bs4 import BeautifulSoup
import Info

login = {"email": Info.email, "password": Info.password}

url_to_open = "https://www.everydollar.com/app/budget"

request_page = urlopen(url_to_open)
page_html = request_page.read()
request_page.close()

html_soup = BeautifulSoup(page_html, 'html.parser')

print(html_soup)

budget_stuff = html_soup.find_all('div', class_="BudgetOverviewPlanned")
print(budget_stuff)

total_budget = 0

for budget in budget_stuff:
    budgeted = budget.find('div', class_="BudgetOverviewList-value")
    print(budgeted)
    total_budget = total_budget + int(budgeted)

print(total_budget)