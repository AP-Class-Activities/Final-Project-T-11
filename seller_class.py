import datetime
import random


class Seller:
    sellers = dict()
    sellers_rates = dict.fromkeys(sellers.keys(), [])
    suspended_sellers = list()

    def __init__(self, name, last_name, distance_to_inventory, phone_number=None, email=None):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.rate = sum(Seller.sellers_rates[self.seller_id]) / len(Seller.sellers_rates[self.seller_id])
        random_id = random.randint(100000, 1000000)
        flag = True
        while flag is True:
            if random_id not in Seller.sellers.keys():
                self.seller_id = "CU" + str(random_id)
                flag = False
            else:
                random_id = random.randint(100000, 1000000)
                flag = True
        self.balance = 0
        self.distance_to_inventory = distance_to_inventory
        self.sales = dict()
        self.suspension = False
        self.list_of_orders = []
        self.products = []

    def historical_sales(self, item, date, costumer_id, buying_price, selling_price, cost):
        profit = selling_price - buying_price
        income = selling_price
        self.sales[date] = [item, costumer_id, buying_price, selling_price, profit, cost, income]

    def statistics(self):
        time_frame = input("please enter your time frame, enter All if you want your whole historical data: ")
        results = []
        for date in self.sales.keys():
            if time_frame.isdigit() is True:
                if date >= datetime.date.today() - datetime.timedelta(int(time_frame)):
                    results.append(self.sales[date])
            else:
                results.append(self.sales[date])
        time_frame_profits = 0
        time_frame_costs = 0
        time_frame_incomes = 0
        time_frame_sales_count = len(results)
        for i in results:
            time_frame_profits += i[4]
            time_frame_costs += i[5]
            time_frame_incomes += i[6]
        return [time_frame_profits, time_frame_incomes, time_frame_costs, time_frame_sales_count]

    def suspend(self, limit):
        count_of_negative_feedbacks = len(list(filter(lambda i: i < 0, Seller.sellers_rates)))
        if count_of_negative_feedbacks > limit:
            self.suspension = True
            Seller.suspended_sellers.append(self.seller_id)

    def list_of_orders(self, costumer_order):
        self.list_of_orders.append(costumer_order)

    def withdraw(self, amount):
        self.balance = self.balance + amount

    def seller_products(self, product, quantity):
        self.products.append((product, quantity))

