marks = {
    "Ali": {"Math": 15, "Python": 17, "Statistics": 14},
    "Sara": {"Math": 12, "Python": 16, "Statistics": 13},
    "Youssef": {"Math": 8, "Python": 10, "Statistics": 9},
    "Meryem": {"Math": 18, "Python": 19, "Statistics": 17}
}

# student's names
print("\n\nThe names of the students are: ", list(marks.keys()), end="\n\n")

# the mean of the marks for each student
values = list(marks.values())
mean = [{n: m} for n,m in zip(marks.keys(), [((values[i]["Math"]+values[i]["Python"]+values[i]["Statistics"] )/ 3) for i in range(4)])]
print("The marks are: ", mean, end="\n\n")

# the best mark of all
print("The best mark is: ", max([list(mean[i].values())[0] for i in range(4)]), end="\n\n")

# the mean mark of the whole class
s = 0
for j in [list(mean[i].values())[0] for i in range(4)]:
    s += j
print("The mean mark of the whole class is: ", s/4, end="\n\n")

# ajout d'un etudiant
marks["Amine"] = {"Math":18, "Python": 20, "Statistics": 19}
print(marks, end="\n\n")

# delete the student having the least marks