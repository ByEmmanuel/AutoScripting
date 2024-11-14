## Pasos, Disclaimer y Licencias para ejecutar este script

Materia de relleno 

¿Te pusieron una materia que no querías cursar obligatoriamente? 

¿Sé te hace eterna, y no te darán Créditos? 

No pierdas más tu tiempo y utiliza este escript que te completa cerca del 80% de las actividades de lectura de la materia 

# Paso 1
Tener instalado en tu sistema los siguientes elementos

- visual studio code
- python
- Google Chrome

# paso 2 
- abre visual estudio code y dale abrir clonando repositorio
```sh
    https://github.com/ByEmmanuel/AutoScripting
```

# Paso 3
- Verifica tu version de google Chrome
- Instalar los drivers de Chrome
- Instala el archivo copiando y pegando los links de esta pagina en tu navegador, correspondiente a tu version de google chrome

```sh
    chrome://settings/help
```
<br>
<br>
https://googlechromelabs.github.io/chrome-for-testing/

- busca el apartado de "chromedriver" correspondiente a tu version, copia el link y pegalo en otra pestaña nueva

# paso 4
- una vez descargado el archivo, descomprimelo
- copia el archivo llamado chromedriver o chromedriver.exe 
- pegalo en la carpeta del proyecto donde anteriormente clonaste este repositorio

# paso 5
- ejecuta esto en la linea de comandos

```sh
    Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```
posteriormente 
```sh
    .\Setup_Windows.ps1
```

# paso 5 
- ejecuta el archivo 
```sh
    python AutoCompletions.py
```
- si no funciona prueba
    
```sh
    Python3 AutoCompletions.py
```
- o en su caso

```sh
    python .\AutoCompletions.py
```

# paso 6
- si todo salio bien minimiza la ventana y contesta las preguntas de la terminal
- inicia sesion automaticamente en la ventana que se te abrio
- disfruta como tendras una ventana funcionando, solamente procura de no cerrarla
