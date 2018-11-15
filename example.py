# -*- coding: utf-8 -*-
#!/usr/bin/env python3
from colorin import Colorin
import time, sys

col= Colorin(['Place', 'Country', 'Phone Code', 'Population'])
col.add_row(['Nottingham', col._yellow('Nottinghamshire', 'it'), '0115', col._green(292400)])
col.add_row(['Luton', col._yellow('Bedfordshire', 'it'), '01582', 203800])
col.add_row(['Huddersfield', col._yellow('Yorkshire', 'it'), '01484', 146234])
col.add_row(['Carlisle', col._yellow('Cumbria', 'it'), '01228', col._red(103700)])
col.add_row(['Brighton', col._yellow('East Sussex', 'it'), '01273', 155919])

print(col.showTable())

print (col._blue("Texto en azul, formato por defecto"))
print (col._red("Texto en rojo, cursiva" , 'it'))
print (col._green("Texto en verde, negrita", 'bo'))
