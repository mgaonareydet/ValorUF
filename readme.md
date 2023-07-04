# Valor UF

Obtiene el valor de la UF en CLP del último día del mes anterior al mes actual usando API [mindicador](https://mindicador.cl/api/uf/).

El valor resultante queda copiado en el clipboard listo para ser usado al pegar. 

El script puede traer valores de UF de otros periodos, agregando el periodo como parámetro.

Es requisito tener instalado Python.

### Uso de uf.bat
*(pensado para windows)*
 - Para usar parámetros al llamar el script, tanto uf.py como uf.bat deben ir en C:\Users\\(nombre de usuario)\
 - Editar uf.bat reemplazando (nombre de usuario). 
 - %* debe quedar después de la ruta.
 - Asegurarse que la ruta al archivo .py esté correcta. ( C:\Users\\(nombre de usuario)\uf.py u otro si se desea usar otra ruta).

Para obtener la UF se puede ejecutar Win + R escribiendo "uf".
Para obtener la UF de otros periodos se le puede agregar una fecha despues de "uf" en formato AAAMM. Ejemplo: "uf 202302".


