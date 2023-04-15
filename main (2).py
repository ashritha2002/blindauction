from replit import clear
#HINT: You can call clear() to clear the output in the console.
import art
print(art.logo)
#initialize multiple bidders as yes
mul = "yes"
auction_list=[]
while mul == "yes":
  name = input("Whats your name? ")
  bid = int(input("Whats your bid? $"))
  auction_list.append({name: bid,})
  mul = input("Are there any other bidders.Type 'yes' or 'no'?\n")
  clear()#clears the console as the auction is silent auction
# initilalizw max=0 this is higgest bid amount
max = 0
n = ""
for item in auction_list:#to traverse through the list
  for key in item:#to traverse through dictionary in list
    if max < item[key]:
      max=item[key]#current winning bid amount
      n = key#current winner


print(f"The winner is {key} with a bid of ${max}")