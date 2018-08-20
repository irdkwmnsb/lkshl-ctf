TITLE = "Новый админ"
STATEMENT_TEMPLATE = '''
Старого админа уволили и на его место посадили вас.
Не оставил ли старый админ какого-нибудь послания?

Образ виртуальной машины:
- [Скачать](http://ctf.sicamp.ru/static/LKLCTF.ova)
- [Зеркало 1](https://drive.google.com/open?id=1Z3FNpUDGvrNxdGoROfOb4JtrKuLS-zYA)
- [Зеркало 2](https://cloud.mail.ru/public/5Hxu/G63c9hsCx)

Логин: admin, пароль: ctf
'''

def generate(context):
    return TaskStatement(TITLE, STATEMENT_TEMPLATE)