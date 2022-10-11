# Table de multiplication du nombre n

user_input = int(input("Enter a number: "))

number_list = [i for i in range(10)]

for i in number_list:
    print("{}x{} = {}".format(user_input, i, user_input*i))