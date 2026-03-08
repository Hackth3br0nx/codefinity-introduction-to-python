# Counting letter frequencies in a word
freq = {}
for ch in "abracadabra":
    freq[ch] = freq.get(ch, 0) + 1
print(freq)  # each letter mapped to its count

# Storing user data by username
users = {
    "alice": {"email": "a@example.com", "role": "admin"},
    "bob":   {"email": "b@example.com", "role": "user"},
}
print(users["alice"]["role"])  # quick, readable access

# Dictionary of suppliers by name
suppliers_by_name = {
    "Fresh Farms": {"id": 101, "category": "Produce"},
    "Green Gardens": {"id": 102, "category": "Herbs"}
}

# Direct access by name
print(suppliers_by_name["Green Gardens"]["category"])
