# LUNA 2.0 - Asistente Virtual por voz

## Índice

1. [Descripción](#descripción)
2. [Archivos](#archivos)
3. [Ejecución](#ejecución)


<a name="descripción"/>

## Descripción del proyecto

Este proyecto nace de las ganas de seguir aprendiendo. Tras mis primeros dos meses programando, necesitaba poner a prueba las habilidades que he adquirido en el bootcamp de Ironhack, y también ir un poco más allá. Atraído por la parte más "ingeniera" de los datos, he decidido explorar nuevas formas de usar Python para crear un pequeño Asistente Virtual por voz. LUNA, ese sátelite que, aunque no siempre veamos siempre está, pretende ser un programa en segundo plano que siempre está escuchando.

Cuando oye la palabra 'LUNA', se activa. El logo de LUNA aparecerá entonces en la pantalla como indicador de que ya está lista para ejecutar cualquiera de las funcionalidades que tiene:

- Consultas al Chat GPT: comando de voz "consulta" + la consulta que deseas realizar.
- Envío de mensajes por WhatsApp: comando de voz "whastapp" + "nombre de contacto" + "texto" + "mensaje a enviar".
- Música o vídeo en YouTube: comando de voz "youtube" + el título del vídeo que buscas.
- Búsquedas en Google: comando de voz "buscar" + lo que quieres buscar
- Manejo de aplicaciones de escritorio como Word, Excel o Visual Studio Code: comando de voz "abrir/cerrar + word/excel/visual".

Tanto el envío de WhatsApp, como Youtube o la búsqueda en Google se ejecutan en ventanas en segundo plano, mientras que la consulta al chat GPT es respondida mediante una ventana emergente con la respuesta en forma de texto, lista para ser copiada. Las aplicaciones de escritorio también se abren en ventanas no minimizadas.

Cuando escucha la palabra 'tierra', LUNA se esconde y, aunque no deja de oír hasta el cierre completo del programa, desactiva la escucha activa hasta y entra en modo de espera hasta que vuelva a oir "LUNA". 

Además, respecto a la primera versión, se ha incoporado tecnología TTS (Text To Speech) para que LUNA interactúe con el usuario mediante la voz. En caso de querer silenciarla, simplemente hay que decir el comando de voz "silenciar LUNA" y, para activarla de nuevo, "activar voz LUNA". Finalmente, podemos cerrar el programa usando el comando "cerrar LUNA".

Así funciona, a grandes rasgos, mi pequeño asistente por voz.

 
 <a name="archivos"/>
 
## Archivos

1. Archivos principales (ubicados en la carpeta principal LUNA-2.0):

- <strong>main.py</strong>: script para el reconocimiento de voz y trasncripción.
- <strong>gui.py</strong>: script para la ventana emergente con la respuesta. 

2. Carpetas accesorias:

- <strong>notebooks</strong>: contiene dos notebooks con pruebas: test.ipynb para la librería Threading y voicetest.ipynb para pyttsx3.
- <strong>img</strong>: contiene dos posibles logos en varios formatos (.png, .ico, .svg).
- <strong>driver</strong>: contiene la extensión AdBlocker para la librería selenium.

3. Otros archivos (también incluidos en la carpeta principal LUNA-2.0):

- <strong>functions.py</strong>: script con funciones utilizadas.
- <strong>LUNA.bat</strong>: archivo ejecutable para iniciar LUNA.


 <a name="ejecucion"/>
 
## Ejecución

Para poner en marcha LUNA, se deben seguir los siguientes pasos:

- Crea un entorno virtual nuevo para el proyeto (opcional).
- Descarga este repositorio en local.
- Instala las librerías necesarias (en caso de no tenerlas ya instaladas) usando pip: threading, speech recognition, PyQt5, openai, zmq, pyttsx3, selenium, PySimpleGui y tkinter.
- Especifica las rutas de guardado de cookies (opciones de Selenium) para Youtube, WhatsApp y Google al principio de 'main.py'.
- Asegúrate de que los puertos especificados para el socket de ZeroMQ está libres o, en caso contrario, especifica uno nuevo (dentro de def chat, en main.py, y al principio de gui.py).
- Ejecuta los dos archivos principales a la vez, cada uno con su propia terminal.

En caso de querer hacer un único ejecutable:
- Desde la terminal, navega hasta la carpeta de proyecto y ejecuta el comando "pyinstaller archivo.py", donde "archivo.py" debe ser remplazado por 'main.py'.
- Repetir el proceso para gui.py. Se crearán dos carpetas nuevas llamadas "build" y "dist", y dentro de ésta última se encuentran los archivos ejecutables creados ('main.exe' y 'gui.exe'), cada uno en una carpeta con su nombre.
- Doble click en el ejecutable 'LUNA.bat'. En caso de no funcionar, cambiar la extensión del archivo a .txt y comprobar si las rutas son correctas. En caso de que no lo sean, cambiarlas y después renombrar ese mismo archivo con extensión .bat, convirtiéndolo así en el ejecutable principal.

Y eso es todo.

Ojalá disfrutéis usando LUNA tanto como yo desarrollándola. ¡Gracias!

<br>
<br>
<br>

<img src="https://github.com/CharlyKill7/LUNA/blob/main/img/luna.png" alt="luna_logo" style="width: 15%; height: auto;">
