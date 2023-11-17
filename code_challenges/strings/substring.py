def count_substring(string, sub_string):
    counter = 0
    
    for i in range(len(string)):
        print(string[i:len(sub_string) + i])
        if (sub_string == string[i:len(sub_string) + i]):
            counter = counter + 1
    return counter

print(count_substring("ABCDCDC", "CDC"))