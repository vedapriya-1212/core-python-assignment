def add(patients, name, age, disease):
    patients.append({"Name": name, "Age": age, "Disease": disease})
    print(f"Patient {name} added successfully.")
    return patients
def search(patients, disease):
    result = [p["Name"] for p in patients if p["Disease"].lower() == disease.lower()]
    if result:
        return result
    else:
        return ["No patients found with this disease"]

patients = []
n = int(input("Enter number of patients to register: "))

for i in range(1,n+1):
    print(f"\nEnter details for patient {i}:")
    name = input("Name: ")
    age = int(input("Age: "))
    disease = input("Disease: ")
    patients = add(patients, name, age, disease)

search_disease = input("\nEnter disease to search patients: ")
found_patients = search(patients, search_disease)

print(f"\nPatients with {search_disease}: {found_patients}")