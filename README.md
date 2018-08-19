# lkshl-ctf
Jeopardy CTF based in SiCamp and LKSH

## The plan:
Вся инфа в Wiki. Если хотите сделать какой либо таск создавайте страничку на Wiki. **Пример о том как работать с Wiki показан в таске Welcome за 0**

## Правила форматирования тасков:
1. Флаг должен быть разным для всех команд. Для этого всё что необходимо для таска (условия, файлы) должны генериться автоматически. Для этого во флаге должна быть случайная часть, обозначаемая в Wiki как `<magic>`. Добавьте в свой таск файл teams_and_flags.py содержащий словарь data, где ключ - id команды а значение - её флаг.
2. Коммит в мастер должен иметь префикс вида <категория> <сложность> - <название>


## Pre-launch status

RTL -  Ready To Launch
ND - No docker
DAG - Done And Generated

Название|Тип задания|Готовность
 ------ | --------- | -------- 
a-plus-b | Service | ND
**bassboosted** | File | DAG 
**blind-robot** | Nginx | RTL
**broadcast** | Nginx | RTL
**brute-zip** | Text | DAG
**caesar** | File | DAG
calc-1 | Service | ND
calc-2 | Service | ND
code-lock | lighthttpd | ND
empty-website | Unknown
**glue** | Text | DAG
hackers-pc | File | Not Ready
**hexandxor** | Text | DAG
**im-hiding** | File | DAG
it-knows | File | Not Ready
**logo** | File | DAG
**minecraft** | File | DAG
new-admin | File | DAG
**nooisee** | Nginx | RTL
**printer** | File | DAG
**qr** | File | DAG
**red-button** | Nginx | RTL
restore-usb | File | Not ready
rsa | Text | DAG
**strange-archive** | File | DAG
true-reverse | File | Not ready
**terminal** | Nginx | RTL
**usbrip** | File | DAG
**xortop** | Text | DAG
youtube-subtitles | Youtube | Not ready