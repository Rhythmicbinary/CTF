url:‌ https://z.voorivex.academy/x5t23S4Nhf
hint: Expectancy foiled!

next level url :‌ https://z.voorivex.academy/qPLGmDkK6e

> how can find this ?

1- As in the previous step, we first inspect the first page:
<br>
![inspect first page](img/level-12-0.png)

2- Intercept request with (Burp Suite)[https://portswigger.net/burp/communitydownload]:
<br>
![Burp Suite request](img/level-12-1.png)

3- Oooo, We find a new headers with name `X-Next` and value `false`, so set it with `true` value, and send request:
<br>
![after set headers](img/level-12-2.png)
