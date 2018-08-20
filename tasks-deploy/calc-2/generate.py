TASK_URL =  "calc-2.ctf.sicamp.ru 50003"
TITLE = "НЕПростой калькулятор"
STATEMENT_TEMPLATE = f'''
Весьма ленивый компьютер снова не хочет считать. Поговорите с ним   
`nc {TASK_URL}`  
 Ваш токен: `{{0}}`
'''

def generate(context):
    participant = context['participant']
    token = tokens[participant.id % len(tokens)]
    return TaskStatement(TITLE, STATEMENT_TEMPLATE.format(token))
