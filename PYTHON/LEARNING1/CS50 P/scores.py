scores = [72, 40, 30,38,80]

average = sum(scores) / len(scores)
# print(average)

score1 = list()

for i in range(3):
    initial_score = int(input("score : "))
    # score1.append(initial_score)  #or
    score1 += [initial_score]

average = sum(score1) / len(score1)
print(f"average : {average}")
