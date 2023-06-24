# Question 1
def hello_name(user_name):
    print("hello_" + user_name + '!')

hello_name("John")

    
# # Question 2
def first_odds():
    for num in range(1, 101):
        if num % 2 != 0:
            print(num)


# Question 3
def max_num_in_list(a_list):
    if len(a_list) == 0:
        return None
    max_num = a_list[0]
    for num in a_list:
        if num > max_num:
            max_num = num
    return max_num

numbers = [5, 6, 7, 8, 9, 10]
max_number = max_num_in_list(numbers)
print(max_number)


# Question 4
def is_leap_year(a_year):
    if a_year % 4 == 0:
        if a_year % 100 == 0:
            if a_year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
year = 2024
is_leap = is_leap_year(year)
print(is_leap)


# Question 5
def is_consecutive(a_list):
    if len(a_list) < 2:
        return True
    sorted_list = sorted(a_list)
    for i in range(len(sorted_list) - 1):
        if sorted_list[i] + 1 != sorted_list[i + 1]:
            return False
    return True

numbers = [8, 9, 10, 11, 12, 13]
is_consecutive_list = is_consecutive(numbers)
print(is_consecutive_list)