#Nested List
marks = [[45, 72], [48, 78]]
print(marks [1][1])

#Tarversing
for mark in marks:
    for m in mark:
        print(m)    

# list inside Dictonary
stu_info = {
             "name" : "Ravi",
             "marks" : [48, 78],
}
print(stu_info["marks"][1])

#Tarversing
for k, v in stu_info.items():
    print(k)
    for mark in v:
        print(mark)

# Nested Dictonaries
stu_info = { "asha" : { "cs" : 48,
                        "py" : 78,
                        },
            "ravi" : {"cs" : 48,
                    "py" : 78,
                        }    
            }
print(stu_info["asha"]["py"])

#Tarvering
for k, v in stu_info.items():
    print(k)
    for sub, mark in v.items():
        print(sub, mark)
           

# counter function
from collections import Counter
trainers = {"Divya", "Gamana", "salman", "Gamana", "Salman", "Gamana"}
trainer_count = Counter(trainers)
print(trainer_count)

freq = trainer_count.most_common(2)
print(freq)

