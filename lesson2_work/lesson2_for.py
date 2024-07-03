for x in range(1, 21):
    print("x=",x, "x2=", x*x)

students = ["Алексей", "Борис","Елена", "Рома", "Дима", "Румяна", "Stefan", "Morty"]

x = f"Количество человек в списке: {len(students)}"

print(x)

for i in range(len(students)):
    print(students[i])

word = "test"

for student in students:
    print(student)

for s in word:
    print(s)

# нужно напечатать только нечетные числа
nums = [1,2,3,4,5,6,7,8,9,10]

for n in nums:
    if(n % 2 == 1):
        print(n, "", end="")