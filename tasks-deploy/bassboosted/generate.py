TITLE = "BASSBOOSTED"
STATEMENT_TEMPLATE = '''
Вы знаете что такое BASSBOOSTED? Да? Мне вас жаль. Что-ж, вам нужно сделать DETSOOBSSAB. Тогда вы получите флаг.
[audio.wav](/static/files/kljhsafd/{0}.wav)
'''

def generate(context):
    participant = context['participant']
    token = tokens[participant.id % len(tokens)]
    return TaskStatement(TITLE, STATEMENT_TEMPLATE.format(token))

tokens = ['pxFEIkRjDn6a', 'q9yLfSvZGkxy', 'AWBkJqkOUsj9', 'AhTBjFa8NOtG', 'eNxIZ9k1nOAh', 'BJMhtpJW3BV9', '2CDMqMz4PRZo', 'exNbYlYlpQ7C', '6dRGssZOyGar', 'Ki4ZG8OoPfIn', 'mvl7JUJVcyVj', 'BqY0GwDpJOwJ', '0tQldYtaIf0A', '9EipLHRZ4inB', 'CPiyEgOO4ICg', 'AScSyXctdE62', 'hDXttQIk7MNI', '66mGkcklJXfd', 'xikqHw58Kt3T', '9L7GRYtKpdIu', 'I4t5ZfR59Ki1', '5HwfXnkzcxjY', 'byUrLxD1Gb2R', 't1nKCcwFphRh', '2VC8s2P9P8uN', 'GHHpvK4mYAAv', 'BbraOtn9lOhG', 'yk1VIcv9Dt1M', 'sgii1iuuip4M', '3WANPM7Pv1hG', 'Oh6wQpET3lF4', 'nEFJUHMy66aX', '4YmWoKZLSHP1', 'mmKrh8PsjC6d', '8zNGkKOKx2aX', 'zsTMoYwmn2gw', '4OdP4pPpxVog', 'cLLvaSKRxNRl', '19c56ri7k2HY', 'Xsl6fGqtATO0', 'QCQ2KZWP1jKT', 'LRZdpyEXovpr', 'V9OJckdj1TIp', '098xEwKN9UJ3', 'HyIDgbbJVyqD', 's4VsfsLB9Spu', 'mjn5tnKlQwTI', 'sa337Nr6XllD', '8ZXpTXU56Oxn', '8ssMTPZXu3Lq', '19Y0antEBHm1', '9KceznGdtG1n', 'aJy3bXeHjHxG', 'QPGRsSlZ2JTH', 'wDRcv6N2BbqV', 'ktFQR4vrL302', 'nXxsgcpzj2A3', 'SVQuSs7L0VsU', 'hcfw5EFasSDM', 'Ul2RTtsckLoq', '8jdXDyD7JddV', 'uW8Y1D8yYHwP', 'RIBbA5kJGlb8', '9CeZSw8yFJpZ', 'uR5zAUL21nAt', 'Ngt7W0BAigcK', 'SrhiGVM6jv22', 'PqOM9DZM8hmh', 'aH93sKl8prp9', 'XK5PDrY044Zb', 'vzZ7fAfFmWTu', '3o0jDffXqSXn', 'SUSqJMX8e6BI', '6hXq1dqQbBqa', 'pKZ4yc2CUMgw', '4aivD6kDR8WR', 'QkrPuYEZnKnf', '7o0UikLg8ByA', 'ZIm9O3qvcP1Y', '945TFjnniHaP', 'mGrb3u6oHLpk', 'VXpdTCx5WSSs', 'l3upUL4IaoxG', 'CZ8e1k7YzsdS', 'NIVhFk7FF2pa', 'l6R53dvMJay4', 'PfZEqp88ZRJ7', 'p21J8nBc6osy', 'K5azcWH8JC4A', 'tdTRa6bvJ87Y', 'f3zuqGB8LttI', 'uGjPCoR94CCK', 'iUaWJhJqdoga', 'waY11shQZLBM', '9wyczIQEL8lN', 'deRw030vJ6PM', 'O80O79Z6Jqep', 'gd653NdFGgZx', 'o4PkEN4SGgeP', 'eQ3OZdqawyLc', 'dyxJEf6SlSP9', 'rxwsEDzGlIbP', 'GpgoI0sufuK4', 'hHq7cq537nY3', 'DCvKKL9ZAJk1', 'kyS4L0bSLhVe', 'fAg2QgADM4Fj', 'oS1sjwmnSwEY', 'vVo7EIDhN04I', 'Saec916qGval', '6dmvc4dm5pXw', 'tB8QpVk3o4TW', 'VTlkmfhTVlfa', 'yVPlGqKK8wfM', '1dmlBzMJZVTy', 'OkeTwqgI4ESN', 'GZmaNfqnAiCK', 'cS2HubhAbLJj', 'cYeas3pTImZy', 'GLZMlSbTNJfk', 'PslSP8iEGWxb', '5QCH0OQvu4Sn', 'wcu2Aji555yi', 'kzyQLhbp08tg', '1xEYmY7HwBdh', 'vLuTixgoxoQF', 'Hmxjn72MaMNy', 'worFCDYnbYRo', 'p06QjbqfhBXb', 'SzkPiySZuFoV', 'fhWUY9wPJ80W', 'hxk8iAbrvhyY', 'BrnW0AhTPPbH', 'lmoDQV7Fyqed', 'RM2XAzAYEuMq', 'bttl51nF2QAv', '4ays2WkpOsel', 'InTKoLace8za', 'IsxPpQsYvQXf', 'eM18RGM4pECD', 'xFhM3G2YX11x', 'PWSqR1NhBUXw', 'B74JBqMHRmvt', 'HN0bi7vsZTzi', 'ySO5Lo7cnTn6', '9yGHYJDafwHI', 'pNhXMDa9ax8u', 'ShfyVrEpADt5', 'NmJTb9SC7BvI', 'Sk4C25NRtuKP', '1vwv2OFu7kKn', 'Lgu7ZM1URA0f', 'VjSCbkvqHBG0', 'T4xSG9mhe6bM', '8qjtI13W3SAo', 'bq424TFjBbiQ', 'AlBgpHq1EqOf', 'OVVBpUquRlh9', 'w2eKEn9WddG6', 'IFhlImDiL5la', '7VmutUXbMjF2', '5qrrgXenzQfs', '5IM6212s5OxM', '0bg2gTxR6FEw', 'Fe3M6qIrg4pK', 'uTmLCWqwQH5Z', 'C3eCdg3wjRNa', 'kkJ8VwMa5E5N', 'aWfEO2j2AxMM', 'Etvx6aZz14O1', '4Lv6KJ7DHNEb', 'TOaleFDQHC5H', 'HN2TLekbz5bx', 'vgdjgl8i0ErV', '5hV8LfWpDtEd', 'KsMl05RZ6mXr', 'wUE71MhAgaOq', '0dujhi2x9X79', 'IbSjGqXjGnkS', 'TeUw07OFEgkc', 'q2y2WKj6Muq4', 'ALdmBBt7UsFL', 'QTBsi0EL1YHE', '6DzabbpH2Irr', 'qJTDD7Zojn3M', 'f3Xn4g8n1VML', 'Ukag0geBQoS0', 'Vne0KcHvzfAE', 'dblxKsNH4k45', 'q7nQmsGtvrkM', 'KOgTz4kjM0Fr', 'we5gtzOypfvq', 'U4EsI4w1XCjT', 'PO7YhgqSsBK6', 'BaUraL5kX1nd', 'ayk9bfwlOhy7', 'ksJTc6x94aJl', 'JX82xYpj9uKR', 'CY4h8yy5ivh2', 'AiFI861czX7k']