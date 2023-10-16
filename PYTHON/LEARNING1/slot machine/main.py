#constants 
MAX_LINE = 3 
MIN_LINE = 1
MAX_BET = 100
MIN_BET = 1
#print(f"helllo ${MIN_LINE} - {MAX_LINE}")   # a way to concatenate variables with words

# function for taking user input
def deposit(): 
    while True:
        amount = input("how much will you like to deposit? $")
        if amount.isdigit():
             amount = int(amount)
             if amount > 0:
                break
             else:
                 print("please enter a valid amount, amount should be greater than 0")
        else: 
            print("please enter a number")
    return amount


#getting lines we want to bet on 
def get_lines():
    while True:
        lines = input("enter number of lines (" + str(MIN_LINE) + " - " + str(MAX_LINE) + ")? ")
        if lines.isdigit:
            lines = int(lines)
            if MIN_LINE <= lines <= MAX_LINE:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("enter a number")
    return lines


def get_bet():
    while True:
        amount = input("how much will you like to bet(" + str(MIN_BET) + " - " + str(MAX_BET) + ")")
        if amount.isdigit:
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"enter an amount between {MIN_BET} - {MAX_BET} !!!!!")
        else:
            print("enter a Valid amount")
    return amount
#
def main():
    balance = deposit()
    lines = get_lines()
    # 
    while True:
        bet_amount = get_bet()
        total = lines * bet_amount
        if total > balance:
            print(f"YOUR BALANCE IS TOO LOW FOR THIS BET, YOUR BALANCE IS {balance}, YOU NEED TO DEPOSIT {total - balance} TO COMPLETE THIS BET")
        else:
            break
   
    print(f"You are betting ${bet_amount} on {lines} lines. Total is {total}")
    # 

main()