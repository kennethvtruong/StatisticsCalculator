import math


class Statistics_Calculator:
    def __init__(self, lst, prompt, sum_of_list, avg, var, stand_dev, check_input):
        self.lst = lst
        self.prompt = prompt
        self.sum_of_list = sum_of_list
        self.avg = avg
        self.var = var
        self.stand_dev = stand_dev
        self.check_input = check_input

    def choose_stat(self):
        self.check_input = True
        my_stat.get_data()
        while self.check_input:
            self.prompt = input("What kind of stat did you want to do today?: ")
            if self.prompt == "mean":
                self.check_input = False
                my_stat.mean()
                print("The mean is %s" % str(self.avg))
            elif self.prompt == "variance":
                self.check_input = False
                my_stat.variance()
                print(self.var)
            elif self.prompt == "standard deviation":
                self.check_input = False
                my_stat.standard_deviation()
            else:
                print("Error. Try again.")

    def get_data(self):
        self.lst = list(map(float, input("Enter the numbers separated by a comma :").strip().split(",")))
        print(self.lst)

    def mean(self):
        self.sum_of_list = 0.0
        for i in self.lst:
            self.sum_of_list += i
        self.avg = float(self.sum_of_list) / float(len(self.lst))

    def variance(self):
        raw_sum = 0
        my_stat.mean()
        for v in self.lst:
            raw_sum += (v - float(self.avg)) ** 2
        self.var = raw_sum / (len(self.lst))

    def standard_deviation(self):
        my_stat.variance()
        self.stand_dev = math.sqrt(self.var)
        print(self.stand_dev)


my_stat = Statistics_Calculator([], "", 2, 2.0, 2.0, 2.0, True)
my_stat.choose_stat()
