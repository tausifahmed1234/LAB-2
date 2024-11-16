class TradingAgent:
    def __init__(self, average_price, critical_stock_level, standard_order_quantity):
        self.average_price = average_price
        self.critical_stock_level = critical_stock_level
        self.standard_order_quantity = standard_order_quantity

    def decide_order(self, current_price, amount_in_stock):
        
        threshold_price = self.average_price * 0.8

        if current_price < threshold_price:
            if amount_in_stock <= self.critical_stock_level:
                
                return f"Order {self.critical_stock_level} units (critical stock level)."
            else:
               
                return f"Order {self.standard_order_quantity} units."
        else:
            return "No order needed."

average_price = 600  
critical_stock_level = 10  
standard_order_quantity = 15  

agent = TradingAgent(average_price, critical_stock_level, standard_order_quantity)

current_price = 500  
amount_in_stock = 20  

decision = agent.decide_order(current_price, amount_in_stock)
print(decision)