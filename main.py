# # colors = ["Red", "Green", "Blue", "Orange"]
# #
# # for i in colors:
# #     print(i)
#
# x =0
#
# # while not (1<= x <=100):
# #     x = int(input("Enter number betweeen 1 to 100: "))
# # print("valis number:", x)
#
# for i in range(4):
#     x = int(input("Enter number between  1 to 100: "))
#     if x <=x <= 100:
#         print("valid number", x)
#         break
#     else:
#         print("Enter valid number.Try again")

# def myfunction(n1 , n2):
#     result = n1 + n2
#     print(f"the sum is : {result}")
#
# number1 = 12.23
# number2 = 24.50
#
# myfunction(number1,number2)

# #FIND the avrage of makrs
#
# def find_average(marks):
#     sum_marks = sum(marks)
#     total_subject = len(marks)
#     average_marks = sum_marks / total_subject
#     return average_marks
# marks = [80,80,72,80,90]
# average_marks = find_average(marks)
# print(f"your avarage marks is: {average_marks}")
#
# # calculate grade
#
# def grade_cal(average_marks):
#     if average_marks >= 80:
#         grade = "A"
#     elif average_marks >=60:
#         grade = "B"
#     elif average_marks >= 50:
#         grade = "C"
#     else:
#         grade = "F"
#     return grade
#
# print(f"Your grade is : {grade_cal(average_marks)}")

# set1 = {10, 2, 5, "Rutul",2.5,2.5}
#
# print(set1.append("Beladiya"))


# number = []
# number.append(2)
# number.append(3)
# print(number)

#Oops concepts

#creating class and objects
# class Account:
#     def __init__(self, bal, acc):
#         self.balance = bal
#         self.account_no = acc
#     def debit(self, amount):
#         self.balance -= amount
#         print("Amount Debited", amount )
#         print("total balance is: ", self.balance)
#
#     def credit(self, amount):
#         self.balance += amount
#         print("Amount Credited", amount)
#         print("total balance is: ", self.balance)
#
#     def total(self):
#         return self.balance
#
#
# acc1 = Account(10000, 9040506070)
# acc1.debit(1000)
# acc1.credit(500)
# acc1.credit(50000)

class Car:
    @staticmethod
    def start():
        print("Car started..")

    @staticmethod
    def stop():
        print("car stoppped...")

class Toyota_car(Car):
    def __init__(self, name):
        self.name = name

car1 = Toyota_car("Fortuner")
car2 = Toyota_car("prius")

print(car1.stop())