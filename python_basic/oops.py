class Trade:
    def __init__(self,ticker,buy_price,sell_price):
        self.ticker=ticker
        self.buy_price=buy_price
        self.sell_price=sell_price

    def calculate_profit(self):
        n=self.sell_price-self.buy_price
        return n
    
    def get_outcome(self):
        n=self.calculate_profit()
        if(n>0):
            return "Win"
        else:
            return "Loss"
        

trade_1=Trade("AAPL",150,175)

print(f"The outcome of the first trade :{trade_1.get_outcome()}")


class MarginTrade(Trade):

    def __init__(self,ticker,buy_price,sell_price,leverage):
        super().__init__(ticker,buy_price,sell_price)
        self.leverage=leverage

    def calculate_profit(self):
        return (self.sell_price-self.buy_price)*self.leverage
    

MT=MarginTrade("NVDA",100,110,5)
print(MT.calculate_profit())