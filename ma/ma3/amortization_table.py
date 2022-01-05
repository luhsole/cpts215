
# MA 3: Amortization Table
# Version: 1.0
# Date September 19, 2021
#
# This program prompts user for input values of loan and creates amortization tables.

class Loan:
    '''
    Calculates monthly, principal, and interest payments
    '''

    def __init__(self, principal, yrate, ynum):
        '''
        initializes values to use in calculation
        :param principal: the cost of the objective
        :param yrate: the yearly interest rate
        :param ynum: the number of years for the loan
        '''
        self.p = principal
        self.r = yrate / 100 / 12
        self.n = ynum * 12

    # class methods
    def regular_schedule(self):
        '''
        calculates payments without additional monthly amount and puts them into a list of tuples
        :return:
        '''
        regular = []
        mpymt = (self.r * self.p) / (1 - (1 + self.r) ** (self.n * -1))
        starting_balance = self.p
        m = 1
        while m < self.n + 1:
            i = self.r * starting_balance
            pymt = mpymt - i
            ending_balance = starting_balance - pymt
            monthly = tuple([m, "{:.2f}".format(starting_balance), "{:.2f}".format(mpymt), "{:.2f}".format(pymt),
                             "{:.2f}".format(i), "{:.2f}".format(ending_balance)])
            regular.append(monthly)
            m += 1
            starting_balance = ending_balance
        return regular

    def accelerated_schedule(self, amount):
        '''
        calculates payments with additional monthly amount and puts them into a list of tuples
        :param amount: additional monthly amount towards the loan
        :return:
        '''
        accelerated = []
        mpymt = ((self.r * self.p) / (1 - (1 + self.r) ** (self.n * -1))) + amount
        starting_balance = self.p
        m = 1
        while m < self.n + 1:
            i = self.r * starting_balance
            pymt = mpymt - i
            ending_balance = starting_balance - pymt
            if starting_balance > 0:
                monthly = tuple([m, "{:.2f}".format(starting_balance), "{:.2f}".format(mpymt), "{:.2f}".format(pymt),
                                 "{:.2f}".format(i), "{:.2f}".format(ending_balance)])
                accelerated.append(monthly)
            m += 1
            starting_balance = ending_balance
        return accelerated


def main():
    # prompts user for information
    objective = input("What is this loan for? ")
    principal = int(input("Please enter the principal amount for the loan: "))
    yrate = float(input("Please enter the yearly interest rate (as a percent) for the loan: "))
    ynum = int(input("Please enter the number of years for the loan: "))
    amount = int(input("Additional monthly amount towards accelerated amount: "))

    # instantiates calculation
    loan1 = Loan(principal, yrate, ynum)
    regular = loan1.regular_schedule()
    accelerated = loan1.accelerated_schedule(amount)

    # creates table for regular schedule
    r_file = open("regular_schedule.csv", mode='w+')
    r_file.write("Month \t String_Balance \t Monthly_Payment \t Principal_Payment \t Interest_Payment \t Ending_Balance \n")
    for month in regular:
        each_month = month
        x = 0
        while x < len(each_month):
            if (x == 0):
                r_file.write("{}\t".format(each_month[x]))
            else:
                r_file.write("${}\t".format(each_month[x]))
            x += 1
        r_file.write("\n")
    r_file.close()

    # creates table for accelerated schedule
    a_file = open("accelerated_schedule.csv", mode='w+')
    a_file.write("Month \t String_Balance \t Monthly_Payment \t Principal_Payment \t Interest_Payment \t Ending_Balance \n")
    for month in accelerated:
        each_month = month
        x = 0
        while x < len(each_month):
            if (x == 0):
                a_file.write("{}\t".format(each_month[x]))
            else:
                a_file.write("${}\t".format(each_month[x]))
            x += 1
        a_file.write("\n")
    a_file.close()


if __name__ == '__main__':
    main()
