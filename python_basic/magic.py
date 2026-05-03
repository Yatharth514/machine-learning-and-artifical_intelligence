class Trade:
    def __init__(self, ticker, buy_price, sell_price):
        self.ticker = ticker
        self.buy_price = buy_price
        self.sell_price = sell_price

    def calculate_profit(self):
        return self.sell_price - self.buy_price
    
    def __str__(self):
        return f"Trade:{self.ticker}|Profit:${self.calculate_profit()}"
    
    def __gt__(self, other_trade):
       return self.calculate_profit()>other_trade.calculate_profit()

trade_A = Trade("AAPL", 100, 150)
trade_B = Trade("MSFT", 200, 220)  
print(trade_A)
print(trade_A>trade_B) 