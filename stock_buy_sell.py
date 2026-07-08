def stock(stock_rates):
    buy_price=stock_rates[0]#initially assume first day you bought stock
    profit=0 # initial profit
    for i in range(0,len(stock_rates)):
        if  stock_rates[i]<buy_price:  #if next day stock price is less then update it 
            buy_price=stock_rates[i]
        else :                          # else  the current profit after selling would be higher rate - buying price
            current_profit=stock_rates[i]-buy_price
            profit=max(current_profit,profit)   # gives max value between current profit and what profit i assumed initially
    return profit # indentation is important
    
stock_rates=[60,56,58,59,53,61,62,51,57,55,67]
result=(stock(stock_rates))
print(result)