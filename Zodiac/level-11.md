url:‌ https://z.voorivex.academy/2YruFQiP0L
hint: Zodiac craves sustenance, offer him a Cookie (again)

next level url :‌ https://z.voorivex.academy/x5t23S4Nhf

> how can find this ?

1- As in the previous step, we first inspect the first page:
<br>
![inspect first page](img/level-11-0.png)

2- Intercept request with (Burp Suite)[https://portswigger.net/burp/communitydownload]:
<br>
![Burp Suite request](img/level-11-1.png)

3- Oooo, We find a new cookie with name `next` and set it with `true` value, and refresh page:
<br>
![after set cookie](img/level-11-2.png)
