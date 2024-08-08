students = {
    'Alice': {
         'Mathematiques': 90,
         'Francais': 80,
         'Histoire': 95
    },
    'Bob': {
         'Mathematiques': 75,
         'Francais': 85,
         'Histoire': 70
    },
     'Charlie': {
         'Mathematiques': 88,
         'Francais': 92,
         'Histoire': 78
     }
}

student_name = input('Entrez le nom de l’étudiant : ')


if student_name in students:
    print(f'Notes de {student_name}: ')

    for matiere, note in students[student_name].items():
        print(f"{matiere} : {note}")
    moyenne = sum(students[student_name].values()) / len(students[student_name])
    print(f"Moyenne de {student_name} : {moyenne:.2f}")
else:
    print(f"L'étudiant {student_name} n'existe pas dans la liste.")

