# Calcul de la moyenne

"""
Très bien’’ à partir de 16, ‘’Bien’’ entre 14 et 16, ‘’Assez Bien’’ entre 12 et 14, ‘’Passable’’ entre 10 et 12, ‘’Insuffisant’’ en dessous de 10
"""

avg1 = int(input("Enter average1: "))
avg2 = int(input("Enter average2: "))
avg3 = int(input("Enter average3: "))

avg = (avg1+avg2+avg3)/3
print("Vôtre moyenne totale est : "+str(avg))

if avg >= 16:
    print ("Mention Très Bien!")
elif avg > 14 and avg < 16:
    print ("Mention Bien!")
elif avg > 12 and avg <= 14:
    print ("Mention Assez Bien!")
elif avg > 10 and avg <= 12:
    print ("Mention Passable!")
else:
    print ("Insuffisant")
