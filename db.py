import json

class Database:
    def register_user(self, name, email, password):
        with open('users.json') as read_file:
            data = json.load(read_file)

            if email in data:
                return 0
            else:
                data[email] = [name, password]

        with open('users.json', 'w') as write_file:
            json.dump(data, write_file, indent=4)
            return 1

    def login_user(self, email, password):
        with open('users.json') as read_file:
            data = json.load(read_file)

            if email in data:
                if data[email][1] == password:
                    return 1
                else:
                    return 0
            else:
                return 0
