import datetime
import random
sellers = dict()
suspended_sellers = list()


class Seller:

    def __init__(self, name, last_name, distance_to_inventory, address, phone_number, email):

        # check if store approves this new seller or not
        try:
            # calling the store system admin to accept or reject this seller request
            if Store.approve_seller([name, last_name, distance_to_inventory, address, phone_number, email]) is True:
                self.name = name  # assigning it's first name
                self.last_name = last_name   # assigning it's last name
                self.phone_number = phone_number  # assigning it's phone number
                self.email = email  # assigning it's email address
                self.rates = dict()  # assigning empty dictionary of rates to be filled by costumers opinions
                random_id = random.randint(100000, 1000000)  # generating random 6 digit id number
                '''hence the generated id is random, it is possible that they may coincide, so to avoid such situations
                we use this while loop to check for existing duplicates'''
                flag = True  # a flag to keep while loop going until we have a unique seller id
                while flag is True:  # assigning a unique seller id to the new seller
                    if random_id not in sellers.keys():  # checking existing sellers to find duplicate seller id
                        self.seller_id = "SL" + str(random_id)  # no duplicates were found, so we assign seller id
                        flag = False  # now that the id is successfully assigned, we change the flag to stop while loop
                    else:  # duplicate id were found
                        random_id = random.randint(100000, 1000000)  # generating a new random seller id
                self.balance = 0  # seller initial account balance
                self.distance_to_inventory = distance_to_inventory  # time distance to store  from seller location
                self.sales = dict()  # all seller sales by date, the format of the dictionary is = {date: sale details}
                self.suspension = False  # the suspension status
                self.list_of_orders = []  # assigning empty list of orders to the newly added seller
                self.products = []  # empty product list to be filled by costumers, entries are tuples: (quantity, type)
                self.address = address  # assigning it's address
                self.profit = 0
                self.cost = 0
                self.income = 0
                self.total_sales_counts = 0
                # adding the new seller to the dictionary so that we can add them to database later
                sellers[self.seller_id] = [self.name, self.last_name, self.address, self.list_of_orders, self.balance,
                                           self.phone_number, self.email, self.rates, self.sales, self.suspension,
                                           self.distance_to_inventory, self.products, self.profit, self.income,
                                           self.cost]
        # if gets rejected
        except PermissionError:
            print("This seller was not approved by the system admin.")

    # method to generate sales records by time
    def historical_sales(self, item, quantity, date, costumer_id, buying_price, selling_price, cost):
        profits = (selling_price - buying_price) * quantity
        incomes = selling_price * quantity
        self.profit = profits  # updating profits amount
        self.income = incomes  # updating incomes amount
        self.cost += cost  # accumulating costs
        # records will be saved in a dictionary by below format:
        self.sales[date] = [item, quantity, costumer_id, buying_price, selling_price, profits, self.cost, incomes]

    # method to generate historical sale data in an arbitrary timeframe
    def statistics(self, time_frame):  # have in mind that time_frame should either be an integer or "all"
        results = []
        for date in self.sales.keys():
            if time_frame.isdigit() is True:  # check if time_frame is a number or the whole time is wanted
                # now we filter the sales which happened between today and time_frame days ago
                if date >= datetime.date.today() - datetime.timedelta(int(time_frame)):
                    results.append(self.sales[date])  # appending filtered sales
            else:  # time_frame was "all" so we enter every sale record
                results.append(self.sales[date])  # appending every sale record
        time_frame_profits = 0
        time_frame_costs = 0
        time_frame_incomes = 0
        time_frame_sales_count = len(results)
        for i in results:
            time_frame_profits += i[5]  # updating profits amount
            time_frame_costs += i[6]  # updating costs amount
            time_frame_incomes += i[7]  # updating incomes amount
        return [time_frame_profits, time_frame_incomes, time_frame_costs, time_frame_sales_count]

    # method to suspend a seller if it's negative feedbacks exceeds a certain amount, limit can be changed arbitrarily
    def suspend(self, limit):
        # filtering negative feedbacks from the seller's rating list
        count_of_negative_feedbacks = len(list(filter(lambda i: i < 0, sellers[self.seller_id][7])))
        if count_of_negative_feedbacks > limit:  # if negative feedbacks pass over a certain amount we suspend seller
            self.suspension = True  # seller suspended
            suspended_sellers.append(self.seller_id)

    # method to list the ongoing costumers orders for the seller
    def list_of_orders(self, costumer_order):
        self.list_of_orders.append(costumer_order)


    def withdraw(self, amount):
        self.balance = self.balance - amount




