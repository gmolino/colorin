# -*- coding: utf-8 -*-
#!/usr/bin/env python3
from colorin import Colorin

col= Colorin(['Items', 'Values_1', 'Values_2'])

col.add_row(['Nottingham', 115, 400])
col.add_row(['Luton', 152, 380])
col.add_row(['Huddersfield', 148, 623])
col.add_row(['Carlisle', 128, 370])

print(col.showTable())

print(col.showGraph('Items','Values_1'))
print(col.showGraph('Items','Values_1', 'Values_2'))
