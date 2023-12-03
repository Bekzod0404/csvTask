import os

import httpx

url = "https://jsonplaceholder.typicode.com/users"

response = httpx.get(url)

res = response.json()

os.mkdir('files')

os.chdir('files')
for user in res:
    with open(f'{user["username"]}.json', 'w') as fs:
        fs.write(f"Id: {user['id']}\n")
        fs.write(f"username: {user['username']}\n")
        fs.write(f"Email: {user['email']}\n")
        fs.write(f"Phone: {user['phone']}\n")
        fs.write(f"Website: {user['website']}\n")
        fs.write(f"Company name: {user['company']}\n")