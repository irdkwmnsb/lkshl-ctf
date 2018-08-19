TITLE = "Название задания"
STATEMENT_TEMPLATE = '''
'''

def generate(context):
    participant = context['participant']
    token = tokens[participant.id % len(tokens)]
    return TaskStatement(TITLE, STATEMENT_TEMPLATE.format(token))
