'''
Given a array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock once. You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.
'''

# SOLUTION

def StockPicker(arr): 
  
  max_profit = -1
  buy_price = 0
  sell_price = 0
  
  # this allows our loop to keep iterating the buying
  # price until a cheap stock price is found
  change_buy_index = True
  
  # loop through list of stock prices once
  for i in range(0, len(arr)-1):
    
    # selling price is the next element in list
    sell_price = arr[i+1]
    
    # if we have not found a suitable cheap buying price yet
    # we set the buying price equal to the current element
    if change_buy_index: 
      buy_price = arr[i]
    
    # if the selling price is less than the buying price
    # we know we cannot make a profit so we continue to the 
    # next element in the list which will be the new buying price
    if sell_price < buy_price:
      change_buy_index = True 
      continue
    
    # if the selling price is greater than the buying price
    # we check to see if these two indices give us a better 
    # profit then what we currently have
    else:
      temp_profit = sell_price - buy_price
      if temp_profit > max_profit:
        max_profit = temp_profit
      change_buy_index = False
      
  return max_profit

print(StockPicker([9, 11, 8, 5, 7, 10])) # 5