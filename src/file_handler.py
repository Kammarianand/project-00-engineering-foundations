 
def save_to_file(data):

    with open("../data/users.txt", "w") as file:
        file.write(str(data))