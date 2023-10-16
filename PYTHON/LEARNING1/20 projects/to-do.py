

def to_do():
    # to_do_list = list()
    print("NOTE!!... separate your schedules using a comma sign")
    print(


    )
    to_do_input = input("what are your schedules? : ")
    to_do_list = to_do_input.split(",")
    # to_do_list.append(to_do_input)
    print(f"HERE ARE YOUR SCHEDULES \n ")

    for i in to_do_list:
        print(i)

to_do()