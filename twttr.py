vokal = ("a","i","u","e","o","A","I","U","E","O")

pesan = input(" Apa pesan mu? ")
baru = ("")

for letter in pesan :
    if letter not in vokal:
        baru += letter

print(baru)