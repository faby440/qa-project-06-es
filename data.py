headers = {
    "Content-Type": "application/json"
}

user_body = {
    "firstName": "Max",
    "email": "max@example.com",
    "phone": "+10005553535",
    "comment": "Cuidado con el perro",
    "address": "8042 Lancaster Ave.Hamburg, NY"
}

authorization = {
    "Content-Type": "application/json",
    "Authorization": f'Bearer {"auth_token"}'
}

kit_body = {"name": "Mi cojunto"}

auth_token = {
    "Content-Type": "application/json",
    "Authorization": "Bearer f3d9ff6b-afc9-40da-bb0d-82f55d718c03 "
}