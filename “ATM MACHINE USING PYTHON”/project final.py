import time

print("Please Insert your Card")
time.sleep(5)
print("Reading chip data....")
print("--" *20)
time.sleep(5)

password = int(input("Please enter your 4 digit password: "))
pin = int(input("Please confirm your entered password: "))

print("Processing.........")

time.sleep(5)

balance = 10000
while pin != password:
    print("INVALID pin, Please try again!")
    pin = int(input("Please reenter pin: "))


if pin == password:
    print("Welcome")
    print("""
    1 == Balance Enquiry
    2 == Withdraw Amount
    3 == Deposit
    """)

    option = int(input("Please enter your choise: "))

    if option in range(4):

        if option == 1:
            print(f"Your current balance is {balance} ")

        elif option == 2:
            withdraw_amount = int(input("Please enter withdraw_amount: "))
            balance = balance - withdraw_amount
            print(f"{withdraw_amount} is debited from your account")
            print(f"Your current balance is {balance}")

        elif option == 3:
            deposit_amount = int(input("Please enter deposit_amount: "))
            balance = balance + deposit_amount
            print(f"{deposit_amount} is credited to your account")
            print(f"Your current balance is {balance}")

time.sleep(5)
print("Thank you for Banking with Us!!")