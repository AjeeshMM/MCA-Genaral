contacts1 = {
    "Anu":"9846653636",
    "teena":"9876359544"
}
contacts2 = {
    "John":"9857667476",
    "priya":"8654566453"
}
print("Contact1:",contacts1)
print("Contact2:",contacts2)
merged_contacts = contacts1.copy()
merged_contacts.update(contacts2)
print("Merged Contacts:")
print(merged_contacts)