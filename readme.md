# Colorin

La siguiente clase *python* permite el coloreado y el formateo de la salida estándar para la terminal.   
A su vez, la clase es polimórfica y se puede instanciar indicando los títulos de la cabecera y generar así un tabla que se formateará adaptándose al tamaño de los campos, se puede mostrar con el método *showTable*.
La clase también permite mostar la gráfica de valores numéricos a través del método *showGraph()*

### Instalación

`pip install colorin`

### Uso de la Clase

- [x] Importar e instanciar la clase **colorin** sin parámetros o con la lista de campos para cabecera de la tabla.
- [x] Llamar a la función *print* de python y al método-color de la clase **colorin** y formato elegido, no obligatorio, según la siguente tabla:

**Color**

| Color | Método
|---|---
| Negro | \_black
| Rojo | \_red |
| Verde | \_green |
| Amarillo | \_yellow |
| Azul | \_blue |
| Magenta | \_magenta |
|  (...) | (...) |

  **Formato**

  | Color | Método
  |---|---
  | bold | 'bo'
  | dim | 'di'
  | cursiva | 'it'
  | underline | 'un'
  | blink | 'bl'
  | reverse | 'rv'
  | hidden | 'hi'
  | tachado | 'cr'

#### Ejemplo:

```python

# -*- coding: utf-8 -*-
#!/usr/bin/env python3

from colorin import Colorin

col= Colorin()
print (col._cyan("Texto en cyan", 'bo')
```

#### Mostrar texto en la misma línea

Agregar el parámetro `end='\r'` al *print*:

```python
for i in range(10):
  print(col._lblue("Recibido...%d"%i), end='\r')
```

## Creando tabla con Colorin

Para usar la clase para mostrar la tabla, instanciar la clase con los campos de la tabla. Agregar las filas con el método add_row y la lista de valores por columna. Se puede sustituir los *None* por '' o incluso la lista pude contener menos items que la cabecera, pero si hubiera más, se generaría un error.    
Por supuesto, se puede dar color y formato a los campos, salvo a los de cabecera que por defecto tiene efecto *bold*.

`class colorin([lista])`   
Inserta lista con títulos de cabecera para tabla.

> `.add_row([lista])`     
> Agrega fila con el contenido de los campos. No superar el número de campos de la cabecera.
>
> `.showTable()`   
> Devuelve la tabla generada para imprimir.
>
> `.showGraph('EjeVert','EjeHoriz_1',['EjeHoriz_2'])`   
> Devuelve la gráfica generada para imprimir.
>
> `._header()`     
> Devuelve lista de campos de la cabaecera.
>
> `._rows()`     
> Devuelve lista de los campos de las filas.
>
> `._len_header()`     
> Devuelve lista de enteros con los tamaños de las columnas.

```python
# -*- coding: utf-8 -*-
#!/usr/bin/env python3

from colorin import Colorin

col= Colorin(['Place', 'Country', 'Population'])

col.add_row(['Nottingham', 'Nottinghamshire', 292400])
col.add_row(['Luton', 'Bedfordshire', 203800])
col.add_row(['Huddersfield', 'Yorkshire', 146234])

print(col.printTable())
```

![Tabla](./out_table.png)

### Mostrando gráfica con Colorin

El método *showGraph* devuelve la gráfica generada a través de los parámetro aportados con las columnas a mostrar en la gráfica: el primero corresponde al eje vertical y el segundo el eje horizontal, y, opcionalmente, agregar una tercera columna para comparar en la gráfica horizontal.

```python
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
```

![Grafica](./out_graph.png)

Espero sea de utilidad :+1:
