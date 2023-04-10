import threading
import speech_recognition as sr
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import openai
import json
import time
import zmq
import pyttsx3
import subprocess

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ps import popenai
from functions import procesar_chat, procesar_mensaje2, procesar_google

options=Options()

options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--remote-allow-origins=*");
options.add_argument(r"user-data-dir=C:\Users\elmat\anaconda3\envs\luna\Lib\site-packages\selenium\cookies")
#options.add_argument('--headless')                 #Habilitar si no queremos ver la ventana
options.add_experimental_option("detach", True)    #Esta opción corrige el error de cierre repentino
options.add_argument('--start-minimized')
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
options.add_argument('--disable-extensions')
options.add_argument('--disable-infobars')

options2=Options()

options2.add_experimental_option('excludeSwitches', ['enable-automation'])
options2.add_experimental_option('useAutomationExtension', False)
options2.add_argument("--remote-allow-origins=*");
options2.add_argument(r"user-data-dir=C:\Users\elmat\anaconda3\envs\luna\Lib\site-packages\selenium2\cookies")
#options2.add_argument('--headless')                 #Habilitar si no queremos ver la ventana
options2.add_experimental_option("detach", True)    #Esta opción corrige el error de cierre repentino
options2.add_argument('--start-minimized')
options2.add_argument('--disable-gpu')
options2.add_argument('--disable-dev-shm-usage')
options2.add_argument('--no-sandbox')
options2.add_extension('driver/adblock.crx') 
#options2.add_argument('--disable-extensions')
options2.add_argument('--disable-infobars')

options3=Options()

options3.add_experimental_option('excludeSwitches', ['enable-automation'])
options3.add_experimental_option('useAutomationExtension', False)
options3.add_argument("--remote-allow-origins=*");
options3.add_argument(r"user-data-dir=C:\Users\elmat\anaconda3\envs\luna\Lib\site-packages\selenium3\cookies")
#options3.add_argument('--headless')                 #Habilitar si no queremos ver la ventana
options3.add_experimental_option("detach", True)    #Esta opción corrige el error de cierre repentino
options3.add_argument('--start-minimized')
options3.add_argument('--disable-gpu')
options3.add_argument('--disable-dev-shm-usage')
options3.add_argument('--no-sandbox')
options3.add_extension('driver/adblock.crx') 
#options3.add_argument('--disable-extensions')
options3.add_argument('--disable-infobars')


mute = False
def speak(text):
    global mute  # usamos la variable global mute dentro de la función
    engine = pyttsx3.init()
    engine.stop()
    try:
        if not mute:
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id) 
            engine.setProperty('rate', 147)
            engine.say(text)
            engine.runAndWait()
    except:
        engine.stop()
        print('Ocurrió un error de TTS')
               

def close_luna():
    QtWidgets.QApplication.exit()

def main():

    global mute

    r = sr.Recognizer()
    
    r.pause_threshold = 0.8
    r.phrase_threshold = 0.25
    r.non_speaking_duration = 0.5
    r.energy_threshold = 8000

    mic = sr.Microphone(device_index=1)

    clave = "luna"
    clave_stop = "tierra"
    grabando = False

    print('----------')
    print('¡Bienvenido a LUNA!')
    speak('¡Bienvenido a LUNA!')

    while True:
        
        print('----------')
        try:
            # Leer un fragmento de audio
            with mic as fuente:
                print('Ajustando sonido ambiente...')
                r.adjust_for_ambient_noise(fuente)
                print('Sonido ajustado. Hable cuando quiera')
                sound = r.listen(fuente, phrase_time_limit=10)
                #print(sound)
                result = r.recognize_google(sound, language="es-ES")

        except:
            continue

        if 'silenciar luna' == result.lower():
            try:
                speak("Activando modo silencio...")
                mute = True
            except:
                pass

        if 'activar voz luna' == result.lower():
            mute = False
            speak('Voz activada')

        if 'cerrar luna' == result.lower():
            print('Cerrando programa...')
            speak('Cerrando programa...')
            close_luna()  
            sys.exit(0)   

        if not grabando and clave == result.lower():
                print('----------')
                print("LUNA activada. ¿Qué necesitas?")
                grabando = True
                t2 = threading.Thread(target=logo)
                t2.start()
                speak("LUNA activada, ¿qué necesitas?")

        elif grabando and clave_stop == result.lower():
                grabando = False
                print('Pasando a modo de espera')
                speak('Pasando a modo de espera')
                close_luna()   
            
                
        if grabando and result != 'luna':
            print(result)
            
            if result.split()[0].lower() == 'whatsapp':
                t3 = threading.Thread(target=wap, args=(result,))
                t3.start()
            elif result.split()[0].lower() == "youtube":
                t4 = threading.Thread(target=you, args=(result,))
                t4.start()
                speak('Abriendo YouTube...')
            elif result.lower() == "cerrar youtube":
                speak('Cerrando YouTube...')
                driver2.quit()
            elif result.split()[0].lower() == "consulta":
                t5 = threading.Thread(target=chat, args=(result,))
                t5.start()
            elif result.split()[0].lower() == "buscar":
                t8 = threading.Thread(target=goo, args=(result,))
                t8.start()
                speak('Buscando en Google...')
            elif result.lower() == "cerrar google":
                speak('Cerrando Google...')
                driver3.quit()
            elif result.lower() == 'abrir word':
                speak('Abriendo Word...')
                word()
            elif result.lower() == 'abrir excel':
                speak('Abriendo Excel...')
                excel()
            elif result.lower() == 'abrir visual':
                speak('Abriendo Visual Studio Code...')
                code()
            elif result.lower() == 'cerrar word':
                speak('Cerrando Word...')
                close_word()
            elif result.lower() == 'cerrar excel':
                speak('Cerrando Excel...')
                close_excel()
            elif result.lower() == 'cerrar visual':
                speak('Cerrando Visual Studio Code...')
                close_code()
            else:
                print('No valid word')
            time.sleep(0.1)
        
def logo():
    print("Ejecutando Logo")

    class Luna(QtWidgets.QWidget):
        def __init__(self):
            super().__init__()

            # Cargamos la imagen de la luna
            self.luna = QtGui.QPixmap(r"img\crescent-moon-moon-svgrepo-com.svg")

            # Obtener la resolución de la pantalla
            screen_resolution = QtWidgets.QApplication.primaryScreen().geometry()
            screen_width, screen_height = screen_resolution.width(), screen_resolution.height()

            # Calcular la posición de la ventana
            windowWidth, windowHeight = 70, 70
            x = screen_width - windowWidth - 5 # Restar 5 para separar medio centímetro del borde
            y = screen_height // 2 - windowHeight // 2 - 30 # Restar 30 para subir 3 centímetros


            # Configuramos la ventana principal
            self.setWindowTitle("Luna")
            self.setGeometry(x, y, windowWidth, windowHeight)
            self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)
            self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        def paintEvent(self, event):
            painter = QtGui.QPainter(self)
            painter.drawPixmap(self.rect(), self.luna)

        def mousePressEvent(self, event):
            if event.button() == QtCore.Qt.LeftButton:
                self.drag_position = event.globalPos() - self.frameGeometry().topLeft()
                event.accept()

        def mouseMoveEvent(self, event):
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(event.globalPos() - self.drag_position)
                event.accept()

    if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        luna = Luna()
        luna.show()
        sys.exit(app.exec_())

def wap(result):
    print("Ejecutando WhatsApp")

    PATH = ChromeDriverManager().install() 

    try:
        mode, text, name = procesar_mensaje2(result)

        if mode == 'whatsapp':
            
            print(f"Modo: {mode}")
            print(f"Texto: {text}")
            print(f"Nombre: {name}")

            speak(f'Enviando mensaje de WhatsApp a {name.split()[0]}')

            driver=webdriver.Chrome(PATH, options=options)
            driver.get('https://web.whatsapp.com/')

            wait = WebDriverWait(driver, 30)  # Wait for up to 10 seconds

            busca = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p')))
            busca.click()
            busca.click()
            busca.send_keys(name)

            busca.click()
            busca.send_keys('')
            time.sleep(1)
            busca.send_keys(Keys.TAB, Keys.TAB)
            time.sleep(0.5)
            busca.send_keys(Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB)

            txt = driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
            txt.send_keys(text)
            time.sleep(1)

            ent = driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')
            ent.click()
            time.sleep(1.5)

            try:
                speak('Mensaje enviado')
            except:
                pass

            driver.close() 

    except Exception as e:
        time.sleep(0.5)
        print('Ocurrió un error con WhatsApp')

driver2 = None

def you(result):

    global driver2

    PATH = ChromeDriverManager().install() 

    try:

        if driver2 is None:
            # Si no hay una sesión de Selenium abierta
            service2 = Service(PATH)
            driver2 = webdriver.Chrome(service=service2, options=options2)
            driver2.get('https://www.google.com/')

        elif driver2 is not None:
            driver2.quit()
            service2 = Service(PATH)
            driver2 = webdriver.Chrome(service=service2, options=options2)
            driver2.get('https://www.google.com/')

        wait2 = WebDriverWait(driver2, 30)  

        buscador = wait2.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="APjFqb"]')))
        buscador.click()
        buscador.send_keys(result)
        buscador.send_keys(Keys.ENTER)

        time.sleep(0.4)

        buscar = driver2.find_element(By.XPATH,'//*[@id="APjFqb"]')
        buscar.click()
        buscar.send_keys(Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, 
                        Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, Keys.ENTER)

    except Exception as e:
        print(f"Ocurrió un error: {e}")
        time.sleep(0.1)

driver3 = None

def goo(result):

    global driver3

    mode , text = procesar_google(result)

    PATH = ChromeDriverManager().install() 

    try:

        if driver3 is None:
            # Si no hay una sesión de Selenium abierta
            service3 = Service(PATH)
            driver3 = webdriver.Chrome(service=service3, options=options3)
            driver3.get('https://www.google.com/')

        elif driver3 is not None:
            driver3.quit()
            service3 = Service(PATH)
            driver3 = webdriver.Chrome(service=service3, options=options3)
            driver3.get('https://www.google.com/')

        wait3 = WebDriverWait(driver3, 30)  

        buscador = wait3.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="APjFqb"]')))
        buscador.click()
        buscador.send_keys(text)
        buscador.send_keys(Keys.ENTER)

    except Exception as e:
        print(f"Ocurrió un error: {e}")
        time.sleep(0.1)
        

def chat(result):
    print("Ejecutando Chat")

    speak('Haciendo consulta al Chat GPT')

    openai.api_key = popenai

    def send_message(message, chat_log=None):

        model_engine = "text-davinci-003"

        if chat_log is None:
            chat_log = []
        prompt = ""
        for chat in chat_log:
            prompt += chat["speaker"] + ": " + chat["text"] + "\n"
        prompt += "User: " + message + "\nLuna:"

        completions = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop="Luna:",
            temperature=0.7,
        )

        response_text = completions.choices[0].text
        return response_text.strip()

    # Chat loop
    chat_log = []
    print("Luna: ¿Qué necesitas?")
    if 'consulta' in result:
            modo, texto = procesar_chat(result)
            print(modo)
            print(texto)
            chat_log.append({"speaker": "user", "text": texto})

            # Check for specific instructions
            if "como te llamas" in texto.lower():
                chat_log.append({"speaker": "luna", "text": "Soy Luna."})
            elif "di tu frase" in texto.lower():
                chat_log.append({"speaker": "luna", "text": "Del parqué... al parque."})

            try:
                response = send_message(texto, chat_log)

            except Exception as e:
                print(f"Error al enviar mensaje: {e}")

            else:
                chat_log.append({"speaker": "luna", "text": response})
                print("Luna:", response)
                t6 = threading.Thread(target=gui, args=(response,))
                t6.start()
                speak(response)
                with open("chatlog.json", "w") as f:
                    json.dump(chat_log, f)

context = zmq.Context()
socket_sen = context.socket(zmq.PUB)
socket_sen.bind("tcp://127.0.0.1:7788")

def gui(response):

    print('Ejecutando GUI')
    socket_sen.send_string(response)
    print('Envío a GUI completado')

def excel():
    subprocess.Popen([r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE"])

def word():
    subprocess.Popen([r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE"])

def code():
    subprocess.Popen([r"C:\Users\elmat\AppData\Local\Programs\Microsoft VS Code\Code.exe"])

def close_excel():
    subprocess.call(["taskkill", "/f", "/im", "EXCEL.EXE"])

def close_word():
    subprocess.call(["taskkill", "/f", "/im", "WINWORD.EXE"])

def close_code():
    subprocess.call(["taskkill", "/f", "/im", "Code.exe"])


t1 = threading.Thread(target=main)

t1.start()
t1.join()
