TITLE = "Служба восстановления данных"
STATEMENT_TEMPLATE = '''
В службу восстановления данных с флешек и дисков обратился клиент. Он принёс эту флешку. Говорит, что случайно её отформатировал. Посмотрите, что здесь можно сделать.
(usb.img.tar.gz)[http://ctf.sicamp.ru/static/files/xn9gwqz3/{0}.tar.gz]
'''

def generate(context):
    participant = context['participant']
    token = tokens[participant.id % len(tokens)]
    return TaskStatement(TITLE, STATEMENT_TEMPLATE.format(token))
tokens = ['Mr3eduBFiL5Q', 'vrXy4Rdaen5S', 'axslTWTAiCi3', 'QjHNEKgjpTws', 'sJtkuzyvg9wg', '0YPXCNV8VC2p', 'eaK2ouSQCUJL', 'xYBIp9KyLHzq', 'fvAOg47w4ieO', 'o5GvLgsMlWvm', 'WPBJ01VinoTL', '94Kjg3sm9KnW', 'AmV6R8sH5RSA', 'FAquLF7ZNrkN', '3DdXvbLEuI0S', 'xG3NFcZzqUcC', 'fURyowGENyN0', 'SMDfqcydbwFr', 'hfkrmKP7fjT2', '6fkZDHMRo6Vi', 'zYrts1ujsGmo', '71K6bWC4aCXH', 'jtjYiHLJXoYE', 'fZ1oX6PZXHgW', 't9U1GlIzAaz6', 'wme1sB43CZlZ', 'irltDxxTjwLl', 'RAnJnOIjNVxQ', 'jRyPOhcDb7xf', 'fkOQhV5WugjM', 'XihOAdnD2v1p', 'GJMueiBRRIV2', 'AE1PkrTLBH8u', 'BpkYOgzD78H4', 'LNqEX2CHaEuk', 'uzxFG9ohS2Zw', 'nlB6Aom800WZ', 'pGRoc7lzrcCm', 'Ymd3Bbh5C7kb', 'AfC1CCKXmA9Q', 'DtXuaEDo9D2Z', 'sFGu3iLm4nBB', 'HNzP3j8JYL3N', 'Vjkk68YwSAKe', 'BRFWaskdMWIN', '22Y0hVdCJfmx', 'zjmqGlhd6uuE', 'i202k0QWJzCD', 'GYevjmTxLMMg', '32IfFwGKZilz', 'NdjTqlQ0qVqB', 'YzYj7Xl9cZuB', 'Lni7sYlFNh7D', 'u4nl86Bx79F1', 'nMY4jYZ4YI1I', 'lW3eFNz2qjiG', 'uKDe5CDEBWl2', 'T6U4yaryhKU9', 'LKUehxgyndUq', 'leJGPPnlz2Hk', 'XenXVeJBL7TR', 'hg1nZAzYwwP1', 'KOvfqetAxKMR', 'IUdq5PIih81t', 'oajMjb8RPuw0', 'mmdKiNfVQzxn', 'OcSoW1NRu1ct', 'V9vcCaV5nJLw', 'EfpRA1y5FtKY', 'w9tfbgCi89cj', '8tHlDW8aAwlB', '4IG04xPVvf6R', '4QSJe1oHLS9o', '9svihqFTpOr3', 'u4fmf2uECnev', 'oUuMHc8svhv1', 'o6MMTSPbEULu', 'mmUsieaPn4Bc', 'JixyWUbjHJcn', 'ZyHUnCWrParR', 'X1WzBdU9Ksx0', 'eD7dITb0Iu0f', 'qfBaHTBays6N', 'Mkkiy6mNpQVs', 'by1Y89f9682T', 'fq6lJD8HOZoK', 'WgUrJQ16T8Yy', 'C4blcGm51wq9', '5uLvI0PumRnM', 'gEtLjEEj9FSB', 'N6Jf79Zp9JZr', 'EfTdozXNDktL', 'mD94p1N0Cu5C', '9O9V1J0VZ9A8', '1SPnTT9NKACZ', 'Mc5a2gI7eHvX', 'fwbdfpqGPeHG', 'qtp8IWzxT3RQ', '1VQSCoiHFNEe', 'tAMiOmDDaLAh', 'SXaaidwcHnk2', 'ExBvND2huJVv', 'GX1g8x3QCN58', 'jALkAEDJOR9l', 'SWpvCklFI8rS', 'A6qrBZ2olfOC', 'X3rmzQXkNtqC', 'tUmEV52qbaMW', '4VjcGfMbAcLP', 'hwCMLpi51RCH', 'LQDycefd4v5V', 'eZvEmlExaon7', 'hhKaujS2uwIj', 'VvgfCmxwYxqz', 'PXTADJei3sD1', 'usvBsMJtRRVZ', 'rRTfTl2vnJio', 'ygn6XpAxkifd', '45PMmH1RtNI1', 'KHMWEiycTNok', '7yOTLI1fGQXH', 'pkM1lV70Mzzu', 'Up0rh6dAGbZP', 'U8F3z3tYi6dz', 'TM9yWapHihfa', 'pxpo9IGyDV6o', 'vdVfgxpYDleH', 's5HBVHNUCYUb', 'uoVhn0ZmqSmN', 'PikqkGxincyL', 'OCO0SQ6UGozP', 'X4sTKm24EFHa', 'ctiVBTGg7UnJ', 'mFwwhyN7oIvP', 'Gh32nCmZBYq0', 'Ltqdnn68Ua1i', '4z3tFkQx8LpA', 'DAwP7yhgAwxC', 'm1G3046SzAZA', 'LiWR1lNWwE2G', 'jwTbRQ8nDKgV', 'jdJudNryfQ2r', 'Pxv2MicWt6Xb', 'eMCTgdngNiro', '3jhwXGDrBkrH', 'U9YRx1gpJRCg', 'h514NMFs8fpQ', '4UwthP557aW0', 'qctm7MWHtD5N', 'Exqm76bh3Urv', 'BSZniPARofeC', 'IqRTj8HgWJZC', 'oiXWaed3nWtH', 'zvlEjKG7ePqL', 'KQAND0y0RxCf', 'MiZOTaHvckq1', 't0m8eITjuViD', 't3nAHGEPRvYQ', 'NdjXbqZAQhYf', 'sxtMZJJp0LPR', 'urtaqBRJUdKv', 'Hr1vZqTSgDkV', 'nvCZtJi6FeCt', 'XOE0EgSxQZti', 'b51NVJnuGqOa', 'rQC52mjcQOuf', 'ggfzEd9k9fNf', '2i77TjRXpKyH', 'Oe9SFaso0V9R', 'P4nTMNCOmIlG', 'WeWo9vd6KfGC', 'bB7rQp7BhIrT', 'gw4rmUp0uD86', 'lpuVXxHnToCe', 'GsQQz3tdgNEM', 'MAwwGaCcppaL', '6FY7bkuEzch6', 'gOxcsbFfCMGy', 'MhTJiHGHnFwC', '6RffySDswn7R', '6rrTopLQsqdU', 'f57OiSKaEflx', 'HWcrECXE8dQ2', 'QiTXTmJmrpTh', 'hBx5zFNIB9xo', 'heHKngO0lww8', '5s3RR21Eq7RR', 'WEBSwC23d0Eh', 'GUB4P81cmuTU', 'aMg1e8FlmFW9', 'BTDtwXw5qGhb', '4t4HbyTei08w', 'YAOanbEXUXrh', 'pYgp6IgCKXaf', 'dAej0hUDNq56', 'ySJHvXevQi7x', 'DwHcjMdr1yA2', 'BRLp31SroULu', 'AXUVePOcw75D', 'TIZTmcLJVx9V']