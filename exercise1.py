import numpy as np
import math
import random
x = input("Δώσε διάσταση τετραγώνου:")
x = int(x)
#Πόσες θέσεις υπάρχουν στον πίνακα?
fields = x*x
fields = int(fields)
print("ΥπΑΡΧΟΥΝ", fields, "θέσεις.")
#Βρίσκω το μέσο mid των θέσεων 'fields' του πίνακα arr με στρογγυλοποίηση προς τα πάνω
mid = math.ceil(fields/2)
AV = 0
Q = 0
for i in range(101):
    print(i,'η επανάληψη')
    rows, cols = (x, x)
    arr=[] #Δημιουργώ τον πίνακα arr
    a = 0
    for j in range(cols): #Γεμίζω τον πίνακα arr με στοιχεία
        col = []
        for z in range(rows):
            a += 1  # Η μεταβλητη a μετράει τον αριθμό των θέσεων του πίνακα arr
            if a < mid:
                col.append(0)  # Γεμίζω το πρώτο μισό του πίνακα με 0
            else:
                col.append(1)  # Και το δεύτερο μισό με 1
        arr.append(col)
    #Μετατρέπω τον πίνακα σε μονοδιάστατο
    arr = np.ravel(arr)
    # Ανακατεύω τα στοιχεία του πίνακα
    random.shuffle(arr)
    #Μετατρέπω τον πίνακα σε δισδιάστατο
    arr = np.reshape(arr, (x, x))
    print(arr)
    Sum = 0
    b = 0 # Η μεταβλητή b αυξάνεται κάθε φορά που ο πίνακας arr περιέχει 1
    c = 0 # Η μεταβλητή c μετράει τις τετράδες από 1 που υπάρχουν οριζόντια, κάθετα και διαγώνια στον πίνακα arr
    for j in range(cols):
        for z in range(rows):
            if arr[j][z] == 1:
                b+=1
            else: b = 0
            if b == 4:
                c+=1
    b = 0
    for j in range(cols):
        for z in range(rows):
            if arr[z][j] == 1:
                 b+=1
            else: b = 0
            if b == 4:
                c+=1
    b = 0
    for j in range(cols):
        if arr[j][j] == 1:
             b+=1
        else: b = 0
        if b == 4:
             c+=1
    b = 0
    for j in range(cols):
        y = x-1-j
        if arr[y][j] == 1:
             b+=1
        else: b = 0
        if b == 4:
            c+=1
    Sum += c
    Q += Sum
    print('Yπάρχουν',Sum,'τετράδες στον πίνακα στην',i,'η επανάληψη.')
AV = Q/i
print('Ο μέσος όρος όλων των τετράδων είναι:',int(AV))
