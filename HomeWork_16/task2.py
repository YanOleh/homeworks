'''
square_nums (takes a list of integers and returns the list of squares)
remove_positives (takes a list of integers and returns it without positive numbers
filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years
'''

class Mathematician:
    def square_nums(self, any_list):
        any_list = [i**2 for i in any_list]
        return any_list


    def remove_positives(self, list_number):
        list_number = [i for i in list_number if i < 0]
        return list_number

    def filter_leaps(self, list_of_years):
        new_list = []
        for i in list_of_years:
            if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
                new_list.append(i)
        return new_list





m = Mathematician()
print(m.square_nums([7, 11, 5, 4]))
print(m.remove_positives([26, -11, -8, 13, -90]))
print(m.filter_leaps([2001, 1884, 1995, 2003, 2020]))

