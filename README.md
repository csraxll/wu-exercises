# wu-exercises

Subir la escalera
-----------------

Estás subiendo una escalera que tiene n escalones. En cada paso podés elegir subir 1 escalón o subir 2.

Programar una solución que, dada una escalera de n escalones, encuentre de cuántas formas distintas se puede subir para llegar al final.

Ejemplo:

Para una escalera de 2 escalones, el resultado es 2 porque las posibilidades son:

Subir 1 escalón + subir 1 escalón
Subir 2 escalones
Para una escalera de 3 escalones, el resultado es 3, porque las posiblidades son:

Subir 1 escalón + subir 1 escalón + subir 1 escalón
Subir 1 escalón + subir 2 escalones
Subir 2 escalones + subir 1 escalón

------------------------------------------------------------------------------------------------------------------------------------------------

Reaprovisionamiento de productos
--------------------------------

Deberás escribir un programa que lea el archivo  Json  donde se encuentran las compras de un cliente y calcule la fecha de posible recompra de los productos que compró (solo los que compró al menos 2 veces).

Para obtener la fecha de recompra de un producto: hay que analizar cada cuanto tiempo vuelve a comprar ese producto. Luego sumarle ese tiempo a la fecha de última compra del producto. Entonces vas a calcular una fecha de recompra por producto.

------------------------------------------------------------------------------------------------------------------------------------------------

El código fue escrito y probado usando Python 3.8.2.

Para probar y ejecutar los test del primer ejercicio, usar los comandos:

```python ladder_demo_main.py```

```python ladder_test.py -v```

Para probar y ejecutar los test del segundo ejercicio, usar los comandos:

```python repurchase_demo_main.py```

```python repurchase_demo_main.py -v```
