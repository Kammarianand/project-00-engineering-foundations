 
def transform_users(data):

    users = []

    for user in data:
        users.append({
            "name": user["name"],
            "email": user["email"],
            "city": user["address"]["city"],
            "company": user["company"]["name"]
        })

    return users