import json
def check(a):
    if(len(d) == 0):
        return 0
    return find_depth(a)

def find_depth(a):
    if(isinstance(a, dict)):
        return 1 + max(map(find_depth, a.values()))
    elif(isinstance(a, list)):
        return 1 + max(map(find_depth, a))
    else:
        return 0

filename = input("Δώσε ονομα αρχειου: ")
f = open(filename, "r")
content = f.read()
dictionary = json.loads(content)
print("To max βαθος είναι: ", check(dictionary))
