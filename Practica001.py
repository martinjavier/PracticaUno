
import pyautogui
import subprocess

# Abre la Calculadora

cmd = "C:/Windows/System32/calc.exe"
process = subprocess.Popen(cmd, stdout=subprocess.PIPE, creationflags=0x08000000)

# Pausa de rigor

pyautogui.PAUSE = 2

# Funcion <pulsarBoton>
# Verifica si existe un elemento en pantalla
# Si existe, toma sus coordenadas y le hace click

def pulsarBoton(objeto):
    ObjName = "images\\" + objeto + '.PNG'

    SiExiste = pyautogui.locateOnScreen(ObjName)
    print(SiExiste)
    button7x, button7y = pyautogui.center(SiExiste)
    pyautogui.click(button7x, button7y)
    pyautogui.moveTo(10, 20)
    return

# Funcion <validarValor>
# Verifica si existe una imagen en pantalla
def validarValor(resultado):
    ObjName = "images\\" + resultado + '.PNG'
    print (ObjName)
    SiExiste = pyautogui.locateOnScreen(ObjName)
    pyautogui.PAUSE = 0.25
    if (SiExiste == None):
        resultado = False
    else:
        resultado = True
    return resultado

# Posiciona el cursor en el ángulo superior izquierdo
pyautogui.moveTo(5, 5)

# Valida que esté abierta la Calculadora
assert (validarValor("CALCULADORA"))

# Borra el valor
pulsarBoton("BOTON CE")

# Realizza la operación
pulsarBoton("NUEVE")
pulsarBoton("OCHO")
pulsarBoton("SUMA")
pulsarBoton("DOS")
pulsarBoton("TRES")
pulsarBoton("IGUAL")

# Valida el Resultado esperado
assert (validarValor("RESULTADO"))
