student={"archana":234 ,"christy":323,"anandh":356}
asc_by_name=dict(sorted(student.items()))
print("sorted by nmae(Ascending):")
print(asc_by_name)
desc_by_name=dict(sorted(student.items(),reverse=True))
print("\nsorted by name (Descending):")
print(desc_by_name)