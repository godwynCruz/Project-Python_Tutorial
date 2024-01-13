# {} if dictionaries
# none is an object that represent the absence of value
customer = {
    "name": "Gadwen",
    "age": 30,
    "is_verified": True
}

customer["name"] = "Jack Smith"
customer["birthdate"] = "Jan 1 1980"
# print(customer.get("birthdate", "Jan 1, 1980"))
print(customer["name"])
print(customer["birthdate"])