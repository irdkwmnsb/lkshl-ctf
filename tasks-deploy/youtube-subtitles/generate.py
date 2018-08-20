TITLE = "Ты и Маргарита"
STATEMENT_TEMPLATE = '''
[https://youtube.com/watch?v=3O03uhakcFk](https://youtube.com/watch?v=3O03uhakcFk)
'''

def generate(context):
    return TaskStatement(TITLE, STATEMENT_TEMPLATE)
