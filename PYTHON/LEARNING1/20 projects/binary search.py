# a function that takes a list and parameter value
# multiple varables: middle, start, end, steps
# recursion or while loop
# increase the step everytime it splits
# conditions to target target position

# all the variables specified are indexes of list
def binary_search(list,target):

    middle = 0
    start = 0
    end = len(list)
    steps = 0

    while start <= end:
        print(f"steps {steps} : {str(list[start:end+1])}")

        steps += 1
        middle = (start+end) // 2

        if target == list[middle]:
            return middle
        if target < list[middle]:
            end = middle-1
        else:
            start = middle+1

    return -1

# the_list = [1,2,3,4,5,6,7,8,9]
# target = 4

# binary_search(the_list, target)


def list_intake():

    # target = int(input("INPUT TARGET"))
    # the_list = list()
    # list_input = int(input("ENTER A LIST OF NUMBER TO ITERATE THROUGH : "))
    # the_list.append(list_input)

    # while True:
    the_list = list()
    list_input = int(input("ENTER A LIST OF NUMBER TO ITERATE THROUGH : "))
    for i in range(8):
        list_input = int(input("ENTER A LIST OF NUMBER TO ITERATE THROUGH : "))
        the_list.append(list_input)
        # if len(the_list) < 5:
    return the_list
        
# target = int(input("INPUT TARGET"))

def main():
    list1 = list_intake()
    target = int(input("INPUT TARGET"))
    binary_search(list1 , target)

main()


