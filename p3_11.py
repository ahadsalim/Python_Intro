num_country =int(input('How many countries voted :'))
votes=dict()
for i in range (num_country) :
    country=input('Enter the name of country: ')
    votes[country]= votes.get(country,0) +1

for country in list(votes.keys()) :
    print (country,' : ', votes[country])