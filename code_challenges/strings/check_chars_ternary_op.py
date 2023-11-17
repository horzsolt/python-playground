s = "qA4"

dict = {"alphanum": 0, "alpha": 0, "digit": 0, "lower": 0, "upper": 0}
for i in s:
    if (i.isalnum()):
        dict["alphanum"] += 1
    if (i.isalpha()):
        dict["alpha"] += 1
    if (i.isdigit()):
        dict["digit"] += 1
    if (i.islower()):
        dict["lower"] += 1
    if (i.isupper()):
        dict["upper"] += 1

print("True") if dict["alphanum"] > 0 else print("False")
print("True") if dict["alpha"] > 0 else print("False")
print("True") if dict["digit"] > 0 else print("False")
print("True") if dict["lower"] > 0 else print("False")
print("True") if dict["upper"] > 0 else print("False")