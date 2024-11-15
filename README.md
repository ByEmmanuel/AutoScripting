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

# paso 3
### Si estas en windows
- ejecuta esto en la linea de comandos

```sh
    Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```
posteriormente 
```sh
    .\Setup_Windows.ps1
```

# Importante
- Ejecuta el comando que te devolvio la terminal copiandolo y pegandolo
deberia ser algo tal que:
- "Entorno virtual creado en ... "
- Para activarlo ejecuta: 

### Si estas en MacOS
- haz ejecutable el archivo e ingresa tu contraseña si te lo pide

```sh
    sudo chmod +x Setup_Macos.sh && ./Setup_Macos.sh
```

# Paso 4
- Ejecuta el siguiente comando
```sh
    python Init.py
```

# Paso 5
- Ten Instalada la version mas reciente de google chrome
- Instalar los drivers de Chrome
- Instala el archivo copiando y pegando los links de esta pagina en tu navegador, correspondiente a tu version de google chrome

```sh
    chrome://settings/help
```
<br>
<br>
https://googlechromelabs.github.io/chrome-for-testing/

- busca el apartado de "chromedriver" correspondiente a tu version y sistema operativo, copia el link y pegalo en otra pestaña nueva
- si tu version de chrome no aparece en el listado, intenta una mas cercana a tu version 

# paso 6
- una vez descargado el archivo, descomprimelo
- copia el archivo llamado chromedriver o chromedriver.exe 
- pegalo en la carpeta del proyecto que se llama "Chromedriver"

# paso 7 
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
