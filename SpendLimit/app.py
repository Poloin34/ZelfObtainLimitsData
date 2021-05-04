"""
	~ Gaëtan Poloin
	License ~ GNU GPLv3
"""
from datetime import datetime as dt, timedelta

print("""
~ This tool was made by Gaëtan Poloin under GNU GPLv3 License.

You will need to manually input transaction data.
First, tell me how many transactions you have for the last 32 days : """, end="")

try:
	TrLen = int(input(''))
  if TrLen < 1:
    thiswillraiseanerror
except:
	print("You need to input an integer, greater than 1")
	exit()

Latest30DaysTransactions = []

print("\n")

for i in range(TrLen):

	print('Tell me the transaction date in this format "03.11.21" (Exactly as in your statment): ', end="")
	date = input()
	print('')
	print('Tell me the transaction amount in this format "35.19" / "8.00" (Exactly as in your statment): ', end="")
	amount = input()

	print('\n')

	Latest30DaysTransactions.append( {'date': date, 'amount': amount} )

'''
#	~ It should look like this now

Latest30DaysTransactions = [
	{"date": "05.04.21" , "amount": 25.00},
	{"date": "10.04.21" , "amount": 25.00},
	{"date": "15.04.21" , "amount": 10.00},
	{"date": "25.04.21" , "amount": 10.00},
	{"date": "30.04.21" , "amount": 30.00},
	{"date": "05.05.21" , "amount": 50.00},
]
'''

# Str time to datetime object
for tr in Latest30DaysTransactions:
	date =  dt.strptime(tr['date'], "%d.%m.%y") 
	tr['date'] = date

  
Latest30DaysTransactions = sorted(Latest30DaysTransactions, key=lambda k: k['date']) 

Latest30DaysSpent = 0.0
OldestTransaction = Latest30DaysTransactions[0]

i = 0
for _ in range(len(Latest30DaysTransactions)):
	transaction = Latest30DaysTransactions[i]
  
  # Remove if the transaction is from more than 31 days ago
	if transaction['date'] < dt.now() - timedelta(days=31):
		Latest30DaysTransactions.remove(transaction)
	
	else:
		Latest30DaysSpent += float(transaction['amount'])
		if transaction['date'] < OldestTransaction['date']:
			OldestTransaction = transaction
		i+=1

if len(Latest30DaysTransactions) == 0:
	print('Hey! No transaction in previous 31 days.')
	exit()

msgs = []
AvailableMoney = Latest30DaysSpent

for tr in Latest30DaysTransactions:
	reset = tr['date'] + timedelta(days=31)
	AvailableMoney -= float(tr['amount'])
	spendable = 150 - AvailableMoney


	msgs.append(f"You will be able to spend {'%.2f' % spendable} after the {reset.strftime('%d %b %Y')}")

print('\n'.join(msgs))
