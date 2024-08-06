url:‌ https://z.voorivex.academy/qPLGmDkK6e
hint: Use your mobile

next level url :‌ https://z.voorivex.academy/MNFx06dHTX

> how can find this ?

1- As in the previous step, we first inspect the first page:
<br>
![inspect first page](img/level-13-0.png)

2- Intercept request with (Burp Suite)[https://portswigger.net/burp/communitydownload]:
<br>
![Burp Suite request](img/level-13-1.png)

3- Change `User-Agent` to `Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30`:
<br>
![after change User-Agent](img/level-13-2.png)

3- Add `Referer` in request headers and set value `https://google.com/`:
<br>
![after set Referer](img/level-13-3.png)
