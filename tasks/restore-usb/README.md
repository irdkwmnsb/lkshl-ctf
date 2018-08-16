# Службы восстановления данных
## Условие
В службу восстановления данных с флешек и дисков обратился клиент. Он принёс эту флешку.
Говорит, ччто случайно её отформатировал. Посмотрите, что здесь можно сделать.

## Вложения
tar.gz с образом флешки

## Решение
### TL;DR
binwalk по образу - находит с десяток сигнатур. Среди них 3 PNG-шки. Вырезаем каждую и смотрим.
В одной из них оказывается флаг

### Подробно
Если смонтировать образ, то на нём мы ничего не найдём. Собственно, так и должно быть - ведь
флешка была отформатирована. Тогда попробуем поискать бывшие файлы вручную. Мы не знаем,
где именно они расположены, но можем поискать по сигнатуре. Например, все картинки PNG начинаются
с байтов ` \x89`, `P`, `N`, `G`. Для поиска по сигнатурам служит программа `binwalk`. Запустим её:

```
binwalk usb.img
```

Получим приблизительно следующий вывод:

```

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
282624        0x45000         PNG image, 800 x 600, 8-bit/color RGBA, non-interlaced
301056        0x49800         PNG image, 241 x 174, 8-bit/color RGBA, non-interlaced
319488        0x4E000         Zip archive data, at least v2.0 to extract, name: _rels/.rels
319762        0x4E112         Zip archive data, at least v2.0 to extract, name: docProps/app.xml
320122        0x4E27A         Zip archive data, at least v2.0 to extract, name: docProps/core.xml
320540        0x4E41C         Zip archive data, at least v2.0 to extract, name: word/_rels/document.xml.rels
320828        0x4E53C         Zip archive data, at least v2.0 to extract, name: word/fontTable.xml
321151        0x4E67F         Zip archive data, at least v2.0 to extract, name: word/settings.xml
321379        0x4E763         Zip archive data, at least v2.0 to extract, name: word/numbering.xml
321808        0x4E910         Zip archive data, at least v2.0 to extract, name: word/document.xml
322952        0x4ED88         Zip archive data, at least v2.0 to extract, name: word/styles.xml
323922        0x4F152         Zip archive data, at least v2.0 to extract, name: [Content_Types].xml
324937        0x4F549         End of Zip archive
325632        0x4F800         PNG image, 800 x 600, 8-bit/color RGBA, non-interlaced
325673        0x4F829         Zlib compressed data, default compression
348160        0x55000         Executable script, shebang: "/usr/bin/env bash"
```

Это все найденные сигнатуры. Смещения (DECIMAL и HEXADECIMAL) показывают, где на флешке
хранится тот или иной файл. Давайте сначала посмотрим все изображения. Для этого обрежем
N первых байт у образа, где N - это смещение файла

```
tail -c +282625 usb.img > picture1.png
tail -c +301057 usb.img > picture2.png
tail -c +325633 usb.img > picture3.png
```

Напоминаем, что команда `tail -c +N FILE` берёт содержимое файла, начиная с N-ного байта, считая с 1,
а не с 0, как binwalk, и отсюда взялось увеличение чисел на 1.

Просматриваем изображения и в одном из них находим флаг.

## Генерация тасков
Сначала `./gen_teams_and_flags.py <МАКС_ЧИСЛО_КОМАНД>`, чтобы сгенерировать нужное число флагов в
файле teams_and_flags.py.

Затем `./gen.py X` для генерации файлов для команды номер X. Выходной файл будет иметь имя
`files-teamX.tar.gz`, в папке `teamX` будут временные файлы. Если файл `teams_and_flags` был сгенерирован заново, то нужно заново
сгенерировать файлы для всех команд.
