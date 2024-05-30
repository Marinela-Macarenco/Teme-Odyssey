# Aceasta este tema pentru lecția 8 legată de loops

# Creați o listă de numere de la 1 la 10 folosind un for loop și funcția range().

# CODUL TĂU VINE MAI JOS:
numbers = [i for i in range(1, 11)]
# CODUL TĂU VINE MAI SUS:

# Folosind un for loop, parcurgeți lista creată și afișați numai numerele pare.

# CODUL TĂU VINE MAI JOS:
for number in numbers:
    if number % 2 == 0:
        print(number)
# CODUL TĂU VINE MAI SUS:

# Folosind un while loop, creați o variabilă 'i' inițializată cu 1 și incrementați-o până când ajunge la 5. Afișați valoarea 'i' la fiecare pas.

# CODUL TĂU VINE MAI JOS:
i = 1
while i <= 5:
    print(i)
    i += 1
# CODUL TĂU VINE MAI SUS:

# Creați un dicționar person cu cheile 'name', 'age' și 'city' și iterați prin dicționar afișând perechile de cheie-valoare.

# CODUL TĂU VINE MAI JOS:
person = {'name': 'John', 'age': 30, 'city': 'New York'}
for key, value in person.items():
    print(f"{key}: {value}")
# CODUL TĂU VINE MAI SUS:

# Utilizați un for loop pentru a itera printr-o listă de liste (matrice) și afișați fiecare element.

# CODUL TĂU VINE MAI JOS:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for elem in row:
        print(elem, end=' ')
    print()
# CODUL TĂU VINE MAI SUS:

# Creați o secvență de numere folosind funcția range() și apoi iterați prin această secvență folosind un for loop pentru a afișa numerele.

# CODUL TĂU VINE MAI JOS:
for num in range(1, 11):
    print(num)
# CODUL TĂU VINE MAI SUS:

# Folosiți funcția enumerate() pentru a itera printr-o listă și a afișa indexul fiecărui element alături de valoarea sa.

# CODUL TĂU VINE MAI JOS:
for index, value in enumerate(numbers):
    print(f"Index: {index}, Value: {value}")
# CODUL TĂU VINE MAI SUS:

# Folosiți funcția zip() pentru a itera simultan prin două liste și a afișa elementele corespunzătoare.

# CODUL TĂU VINE MAI JOS:
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
for num, char in zip(list1, list2):
    print(f"Number: {num}, Character: {char}")
# CODUL TĂU VINE MAI SUS:

# Creați o listă de numere de la 1 la 10 folosind un for loop și funcția range().

# CODUL TĂU VINE MAI JOS:
numbers = [i for i in range(1, 11)]
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă while, dublează valorile listei până când primul element va deveni mai mare decât 50.

# CODUL TĂU VINE MAI JOS:
while numbers[0] <= 50:
    numbers = [x * 2 for x in numbers]
    print(numbers)
# CODUL TĂU VINE MAI SUS:

# Generează și printează o listă cu toate numerele pătrat perfect din intervalul [1, 100].

# CODUL TĂU VINE MAI JOS:
perfect_squares = [i**2 for i in range(1, 11)]
print(perfect_squares)
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă for , printează tabla înmulțirii pentru numărul 7.

# CODUL TĂU VINE MAI JOS:
for i in range(1, 11):
    print(f"7 x {i} = {7 * i}")
# CODUL TĂU VINE MAI SUS:

# Creează o listă de liste, unde fiecare sub-listă conține perechi (i, j) pentru i și j de la 1 la 5. Printează această listă de perechi.

# CODUL TĂU VINE MAI JOS:
pairs = [(i, j) for i in range(1, 6) for j in range(1, 6)]
print(pairs)
# CODUL TĂU VINE MAI SUS:

# Parcurge lista de la punctul anterior și printează doar perechile unde i < j .

# CODUL TĂU VINE MAI JOS:
for i, j in pairs:
    if i < j:
        print(f"({i}, {j})")
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă while , caută și printează prima valoare care este mai mare decât 10 dintr-o listă cu numere random creată de tine. Dacă nu există, printează "Nu există valori mai mari decât 10".

# CODUL TĂU VINE MAI JOS:
import random
random_numbers = [random.randint(1, 15) for _ in range(10)]
print("Random numbers:", random_numbers)

found = False
index = 0
while index < len(random_numbers):
    if random_numbers[index] > 10:
        print(f"First number greater than 10: {random_numbers[index]}")
        found = True
        break
    index += 1

if not found:
    print("Nu există valori mai mari decât 10")
# CODUL TĂU VINE MAI SUS:

# Folosind loop-uri Creează un pătrat de stele ( * ) folosind bucle încadrate. Dimensiunea pătratului va fi citită de la utilizator.

# CODUL TĂU VINE MAI JOS:
size = int(input("Dimensiunea pătratului: "))
for i in range(size):
    for j in range(size):
        print("*", end="")
    print()
# CODUL TĂU VINE MAI SUS:

# Folosind for sau while loops realizați afișările de mai jos

# Afișarea 1:
# 1
# 12
# 123
# 1234
# 12345
# 123456

# CODUL TĂU VINE MAI JOS:
for i in range(1, 7):
    for j in range(1, i + 1):
        print(j, end="")
    print()
# CODUL TĂU VINE MAI SUS:

# Afișarea 2:
# 54321
# 5432
# 543
# 54
# 5

# CODUL TĂU VINE MAI JOS:
for i in range(5, 0, -1):
    for j in range(5, 5 - i, -1):
        print(j, end="")
    print()
# CODUL TĂU VINE MAI SUS:

# Afișarea 3:
# abcdefg
# bcdefg
# cdefg
# defg
# efg
# fg
# g

# CODUL TĂU VINE MAI JOS:
text = "abcdefg"
for i in range(len(text)):
    print(text[i:])
# CODUL TĂU VINE MAI SUS:

# Afișarea 4:
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+

# CODUL TĂU VINE MAI JOS:
for i in range(8):
    if i % 2 == 0:
        print("+-+-+-+-+-+-+-+")
    else:
        print("-+-+-+-+-+-+-+-")
# CODUL TĂU VINE MAI SUS:

# Afișarea 5:
# 3
# 3 9
# 3 9 27
# 3 9 27 81
# 3 9 27 81 243
# 9 27 81 243
# 27 81 243
# 81 243
# 243

# CODUL TĂU VINE MAI JOS:
numbers = [3 ** i for i in range(1, 6)]
for i in range(1, len(numbers) + 1):
    print(*numbers[:i])

for i in range(1, len(numbers)):
    print(*numbers[i:])
# CODUL TĂU VINE MAI SUS:

# Completați sarcinile de mai sus pentru a exersa lucrul cu buclele în Python.
