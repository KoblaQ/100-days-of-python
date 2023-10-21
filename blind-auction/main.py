from replit import clear
#HINT: You can call clear() to clear the output in the console.
#Insert logo here
from art import logo
print(logo)
#Ask for name

bids = {}

bid_session = True
while bid_session == True:
  name = input("What is your name?: ")
  bid_price = float(input("What is your bid price?: $"))
  extra_bid = input("Are there any other bidders? Type 'yes' or 'no'. ")
  bids[name] = bid_price
  value = 0
  
  if extra_bid == 'yes':
    clear()
  else:
    bid_session = False
      
for key in bids:
  if value < bids[key]:
    value = bids[key]
    winner = key
    
print(f"The winner is {winner} with a bid of ${value}")


print(bids)