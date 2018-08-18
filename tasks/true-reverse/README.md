# True reverse
## Условие
Только истинные мастера решения тасков в категории reverse смогут полычить этот флаг

## Решение
```
with open('task_...', 'rb') as f:
    data = f.read()
reversed_data = bytes(reversed(data))
with open('task_...', 'wb') as f:
    f.write(reversed_data)
```

## Примечание
Это скорее стего, чем ревёрс, но в принципе нельзя сказать, что это не ревёрс.
