TASK_URL = "empty-website.ctf.sicamp.ru"
TITLE = "Пустой сайт?"
STATEMENT_TEMPLATE = f'''
Действительно ли на [этом]({TASK_URL}/{{0}}) сайте нет ничего полезного?
'''

def generate(context):
    participant = context['participant']
    token = tokens[participant.id % len(tokens)]
    return TaskStatement(TITLE, STATEMENT_TEMPLATE.format(token))
    
tokens = ['JYXQy1aaW8a', '6Mx8ScjqDT1', 'iwqT9p3fk9M', '3P50kxuhT3Z', '1jQQOPRP6H7', 'wJUii7jqEd7', 'ZzbpWLSMeTS', 'Af1DrKb8EHc', '2FQ3KQHodip', 'bahsBje6xoj', '858SBV067AX', 'Q3xuPnFRvmQ', 'HBQy8PxIh5a', 'Z8YhgXjPR2M', 'KlaIXS6XiYT', 'NtA01niBRPO', 'HEKMYj08M8T', '9mtdnWOYo2r', 'FrtxKtJAFrX', 'Nv0gsE1Fg0D', 'SIz1gKoxFe2', 'xQxe6KvaygR', 'TYH4cyE4T0T', 'KuQKWXyTJBd', 'yFS50iWCHft', 'MXbWUmPH6RT', 'l9couPDiJIN', 'r2NyZoKVv7C', 'ZK3Zdn3Jegi', '5U8dQWS1Xj1', 'KV4TmV4GRr9', 'akalCLNwfv9', 'koAIaUJikKX', 'lnTFVzDsXrg', 'tKMitYN6UUv', 'Q4Bxv9mbTWi', 'e3zVTqOv7Aa', 'QGN776NKym5', 'yr5Bw2bgMyG', 'CyP2OW6slCG', 'dIXIO1Am63W', 'qoIBvXM6DCZ', 'Mtw8fJcN3Fm', 'KFOu1oGwGHm', 'g7ENHKbxipz', 'fYIpIEJKSg0', 'sDGgKenZeth', 'Ia1h3Mr7JXl', 'LSlm9Fgwyrf', 'fRnpnXmx7n0', 'LDv8SoknyKR', 'Dc6sYYLLIGd', 'TA1MXGEUgQw', 'hqoDvU0s72H', 'bZNFLFRJ3uL', 'KDUuI7B7p0x', 'DVisdvNqULV', 'XZncuTzXrtu', 'FcyPTmjdv28', 'vRd4tkAR49y', 'is7ldpp1yJF', 'KmDTxXVTu7G', 'mJ7bVli0wKt', 'P3lCZs402l2', 'GR1TFZ2n0Zv', 'ToIGufGe8WU', 'iS9alRiFBtk', 'by3NViB1NLq', '8Qq5udeeHtu', 's2Psk5fngQB', '4GU3sfn3wUn', 'l36mYTKattP', 'FSiqIS6wI2d', 'TFQa62Ra1Gy', 'mv6HSMR1VWy', 'mCupiAEHH4P', 'VJ2gVGv6h9k', 'WOdzzjsRm7t', 'RRJgM6ISouE', 'h6OngeT9tVW', '4n7KmYl0t08', '05QWZOC5IEx', 'TIdYIsULi2O', 'yy4fpgNgzL3', 'MCuFsoSfDBA', 'WqASJsL4wQW', 'uC8hdWMnYJp', 'szrCF5wrcoC', 'xeAs3elzHdB', 'qfhPa6lkaBT', 'vqZD1wVqj5U', '7cHXPmZk6r1', 'It9LanMAigH', 'X7gLYUSnOzW', '80pKaFAwvoZ', 'kb5zKbNyRag', 'Zm2GZUkfuKq', 'vu4fUsWcqxs', 'Cga427nt4Uh', 'ypaTBRdFtmG', '1DNit22cZCp', 'lBko0YFrbAV', 'C1qLMjDifOn', 'yUru5xep9Yo', 'XdtqnkccQDw', 'cqwZVmtgHUz', 'bqY6IGx3C3E', 'l1ZiWgy0ndf', 'hA8kulfqlGM', 'kdFFG6E0d6o', 'PBInOCZzNnt', 'viDHxtHUZg6', 'h41hpcCKuH0', 'wLE3Yaowm1F', 'lE7FNi9bTwO', 'iAq6wsM1ZVZ', 'vijQq3NVQoo', 'nehrYgtFu2T', 'h3xtaHVUVHe', '93uF6mauk9e', 'HDhmQ1gSfkj', 'lLTc53CvcxJ', '2kb9qI1riSg', 'bnB32cIpXcb', '0xVBnxNm5up', 'cq1xklFqEYO', 'drUpm4eEr8V', 'GBj3pIhg1vN', 'b150iodchxP', 'Cr2wvqyOU7m', 'p6Jq2Zao5UK', '4L7rXjk9FQy', '1qoAbGaTPBi', 'ijmLTvs3SnG', 'b5vVB5cwsbb', 'a2KiYdXSRLx', 'DnqFMubOoZY', 'N2ENocGsfxv', 'V2JZdHUlKgA', '33Hx4cGWBc7', 'Z6Ok8FBNQH3', 'xcNynugmnPY', 'JCpoIfrsC3v', 'iTwbQobC8o5', 'XKwirImHcNC', '0KMPBkbL70T', 'kYgxuUeEDmp', 'vc1lxSO765L', '3mEYDPMUqXT', 'kGG8pk5xLwn', '51XDb7HqH89', '9fqISjAVGpT', '1N1A8Bh3wJ7', 'oSpzHHVzD8o', 'B62NnFLMy9i', 'MGfrnzOotRZ', '2SAQoPq6bZE', '64vx5DWdYT7', 'itPTS3ayJPv', 'bQPVQcACplx', 'b8I7XFhm4zw', 'WUuBtOxyfLm', 'j6EVrDWPsvm', 'l3NgtPRsvPv', 'ds7zgnmYdZ7', 'QZJkekC3HOa', 'rBETFKSa1mH', 'lPwq0qMHROa', 'RuCe6Pim798', 'qUKsHPtPW4T', 'rvqty6vXmCU', 'kC7NwqiwQhj', 'cxDkVXXFCPr', '2YkqfeKcigl', 'WS9EQnfkIAt', 'BdIrEnA5NGC', 'PKlYR6mglNG', '2vm7oR11xWT', '6fHAtT3MyZz', 'v6hmWLxtdoU', 'HLnwIawgzMc', 'gGSgrIYsqqm', '7qyioDgHJmn', 'GiqiTKevEV3', 'Zt7AFBqRkJz', 'evtj9vVYTXi', 'L3sv1FRRTWx', 'tV08XSJwQTy', 'DCphK7pwtMO', 'yeFjqpizUtF', 'oBvweIFeHfE', 'M8V3Z1tWjX3', 'oCfrVAZDkr4', 'LlZuCPjpvqa', 'G7JsqHfTcIC', 'hJH3VtM9MSi', 'mPLnbWyymGl', '5CRYNdWlYNp', 'wSVHLWSkC2C', 'n3iPLlzoCrk']
