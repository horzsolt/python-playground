input = ["Krishna 67 68 69","Arjun 70 98 63","Malika 52 56 60"]
n = 3
student_marks = {}
for _ in range(n):
    name, *line = input[n-1].split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = "Malika"

for name, scores in student_marks.items():
    if (name == query_name):
        avg = sum(scores) / len(scores)
        print(format(avg,".2f"))

testString1 = "Hello World!"
print(type(testString1[7:]))