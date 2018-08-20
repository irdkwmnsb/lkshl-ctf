TITLE = "Странный архив"
STATEMENT_TEMPLATE = '''
Мы получили по почте этот архив. Посмотрите, есть ли в нём что-нибудь интересное.

[file.zip](http://ctf.sicamp.ru/static/files/o8weyxsgn/{0}.zip)
'''

def generate(context):
    participant = context['participant']
    token = tokens[participant.id % len(tokens)]
    return TaskStatement(TITLE, STATEMENT_TEMPLATE.format(token))
    
token = ['gQq8MjHu1Jf', 'jvhwujZjYXF', '5ogaDpfsjQW', 'CQsvAk0t0Hp', 'hzunrOK4Wut', 'NF6zqFQb9I8', 'KTtHspIPaQr', 'wp1kxMUvsvv', 'dHRCb5VSl2s', 'ZRywQsCTEBU', '5IufLeL69Ka', 'y05EzW8utoK', 'VhO8UBe5qld', 'HOCadTJu0zE', 'ovxWMZnDXoB', 'YFiQz6NAL6g', 'rYwgpMfEXmr', 'b4X3RfNTcfS', 'zR16uUOkW0b', 'aNq98jg0ud0', '84IOpUOxwQO', 'ESmRsG5g2V6', '33flW3qw51M', '8rBS5OWN4y2', 'MsxeS4vMJii', 'zRByxsKcjtn', 'dt5UK3ND2IQ', 'gXTyqvAcdyL', 'ygZAxR8Dp4X', 'sxhfRGEh67A', 'qDd9XJgomkH', 'wZ5B6C716tx', 'HVUtUkQXCJu', 'dmpzCzXDbz7', 'kRvbEnRgjDu', 'i6ALBVCj0KF', 'b0KakGAtvyU', 'payhdSTS7JN', 'Ypbzpx4z43S', 'r0MqUSqebm0', 'oZSTMDtrTj8', 'yhiQqxM2dB7', 'NGXBwXn77Vm', 'Gv4qAZ2C76Z', 'osa0yBQRWjq', 'aXuBSJIkcaD', 'w0ZFThRZi83', '4zujGZ2KpHP', 'ytZ6VdQ8GS1', 'woBbM3Xm26h', 'uPuslqnXLAA', 'OVwx2nFv2Js', 'DqBzgEAW8Np', '9cjx53a92Ca', 'Np23jdYJb2a', 'IyA7EbCeJXQ', 'Yji4vwgJ63j', 'T70Vxu0M0Xr', 'EKOA4CdzGTl', 'KTuzA9tKr1p', 'Za1R1W4YBK4', 'YALsOhAJyhH', '0ZnWojWExpR', '6kuf0UH10GH', 'XJIH4PE4da0', 'pb21XsbOUy0', 'PeepjB9jnIb', 'u8wgHds9h2Q', 'GJvX1AbomZt', '5Kh8FJKgIuO', 'NK9iTf8dvB0', 'mPcxC90WiRo', 'hRDYaPunv4d', 'Qr4lZQUDLEj', 'MHkPsimbsuK', 'U4fAUAfBYkX', 'lz7pGzabzQ3', 'kSVLU9gIsbb', 'LsneZiii2lj', 'F0wbG7IvM11', 'Cyb3E9V80VK', 'UgV2bPUp938', '8IngD8FZvJz', 'c3XJ0zmb8B0', '0hZpeMv7vAt', 'GlcMebxEkck', 'TA4b2UBE46E', 'ds1C0SvAaEH', 'Bnc8wQvlyeb', 'It04qPPcizh', 'Up7tCoy4L8x', 'VnTDKNRHBAj', '4Ud4tr4GOiJ', '4eEHSoOt62L', 'tC2hGoue6HI', '5fSedNVHnTC', '1SakS3377R6', 'indK997LecC', '8xec7dDOSV8', 'SCIuGZgkmds', 'DHUgtPuSHSm', 'jjIk9ANDM9x', '5IwNvqMJ7Ro', 'lGi0CMq0B9z', 'oTsfS0fk3Vn', 'mOyFJXx9R6c', 'LD6Z9ghc1px', 'nQmBKqeMSXt', 'J42o7EoYmCf', 'SGcN0M633ax', 'BLUmyF729Up', 'ktWbN1g4t3s', 'A0tsdlWXF2v', 'Xjjl6SZ8X6W', 'XDJC5Yi3oCG', 'RMkoy73Bdhs', '0PGlWLckK6s', 'rDkcfxuN4Ac', 'Y1uxBLTZHUF', 'm95FNzAnumd', 'j87pyNycTyF', 'JfpCBoo41JL', '7dceUBP5oax', 'G4H0mSOKUZU', 'jOlkxdkFhcz', '9e35vP5pZXt', '6YfSuXmiLCA', 'D3iTLqkFH1Y', 'l0QGwW0gV2w', '89GRrX1JTal', '7DkwZgGaSyL', 'h4n7bo45mtl', 'zCL4NETv4hj', 'FYDNEuiEPVY', '1fyFLyXcdAx', 'TDh7y3QUy8R', 'pvnVQHf54yJ', 'totqAqGFKyC', '5PlM7IbxFLb', 'TGHwYfPblMf', 'RwsXNYfYXHr', 'TlC9J752AbV', 'NaHqAdA34rK', '4fRUBElSOor', 'pZepJ3lRaDk', 'qYWdbraQn4H', '6n1SaSZOCdr', 'PXemMFiYN06', 'p64U1Hq6OJZ', '0e7HbHMqjGf', '1eI9Rry4E4K', 'IHxZCM0teBJ', 'KMW4g14M0PM', 'GEjPAPNO6tw', 'wDw2oToEJgn', 'jSwPwSoJQ7E', '2mwPjeS4hcG', 'iI3id924VLD', 'Imtxqw2lXMW', 'oWzO0yyB6Cp', 'gCNEpQmE1YB', 'V55N5aNL0nj', 'xn6728zkk3O', 'wGDxAigJbp8', 'jgFMvWLtnKH', '9n0wOPx5wuW', 'jenaipuBZ07', 'uT3SnSfEBtt', 'y845OX72QI1', 'wUvNKjVzI1N', '3JLNncjvdgT', 'gHVLbCauMAl', 'UwaMpnuluc5', 's8Nl6Ncywjv', 'tjvsgkSWAj6', 'XVoqZVLxEcX', 'uj77ju0EONt', 'RHuuf2C9etT', 'WbQwbX3XybT', 'yCMGzdUDeOt', 'TqgF1gDlfJq', 'oeAct73efUt', 'izgCwREO4xa', '7flX1usZutN', 'EN8TwIH8LK8', 'vAmhdLJ3LbJ', 'lBSd8907UcB', 'ELcLUupSU6m', 'xjkCb4Qdq1X', 'vWg3m9cSxYd', '2KkcD9rycDR', 'uf5teiF39u8', 'ZOuRrQUKFqs', 'td0zWQAJJ7P', 'weH33FKUnWc', '3CiSLkdUDX8', 'zJ5LRzC1P2F', '7Prxie7z7Tn', 'f1ff5wWzXbg', 'PHMDdar7YIs']