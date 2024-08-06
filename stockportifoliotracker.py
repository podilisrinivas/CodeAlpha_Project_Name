import yfinance as yf
import pandas as pd
import yfinance as yf
import pandas as pd

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, ticker, quantity):
        if ticker in self.portfolio:
            self.portfolio[ticker]['quantity'] += quantity
        else:
            self.portfolio[ticker] = {'quantity': quantity, 'price': self.get_current_price(ticker)}

    def remove_stock(self, ticker, quantity):
        if ticker in self.portfolio:
            if self.portfolio[ticker]['quantity'] >= quantity:
                self.portfolio[ticker]['quantity'] -= quantity
                if self.portfolio[ticker]['quantity'] == 0:
                    del self.portfolio[ticker]
            else:
                print("Not enough shares to sell")
        else:
            print("Stock not found in portfolio")

    def get_current_price(self, ticker):
        ticker_data = yf.Ticker(ticker)
        return ticker_data.info['regularMarketPrice']

    def calculate_portfolio_value(self):
        total_value = 0
        for stock, info in self.portfolio.items():
            total_value += info['quantity'] * info['price']
        return total_value

    def display_portfolio(self):
        print("Stock Portfolio:")
        for stock, info in self.portfolio.items():
            print(f"{stock}: {info['quantity']} shares @ ${info['price']:.2f}")
        print(f"Total Portfolio Value: ${self.calculate_portfolio_value():.2f}")
def main():
    portfolio = StockPortfolio()

    while True:
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Display Portfolio")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            ticker = input("Enter stock ticker: ")
            quantity = int(input("Enter quantity: "))
            portfolio.add_stock(ticker, quantity)
        elif choice == "2":
            ticker = input("Enter stock ticker: ")
            quantity = int(input("Enter quantity: "))
            portfolio.remove_stock(ticker, quantity)
        elif choice == "3":
            portfolio.display_portfolio()
        elif choice == "4":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
