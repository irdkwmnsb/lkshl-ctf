# Странный архив
## Условие
Мы получили по почте этот архив. Посмотрите, есть ли в нём что-нибудь интересное.

## Вложения
Архив

## Флаг
`LKSHL{S4Y_H3LLO_T0_G1T_<magic>}`

## Решение
В архиве есть папка .git

Откатываемся на 1 коммит назад и видим флаг

## Генерация тасков
```
./gen_teams_and_flags.py NUM_TEAMS
for i in {1..NUM_TEAMS}; do
    ./gen.py $i
done
```

NUM_TEAMS - макс.число команд
