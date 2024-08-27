from machine import Pin
import time

# Configuração dos pinos
up = Pin(2, Pin.IN, Pin.PULL_UP)
down = Pin(4, Pin.IN, Pin.PULL_UP)
left = Pin(6, Pin.IN, Pin.PULL_UP)
right = Pin(8, Pin.IN, Pin.PULL_UP)
button_b = Pin(10, Pin.IN, Pin.PULL_UP)
button_a_start = Pin(12, Pin.IN, Pin.PULL_UP)

# Dicionário para mapear os pinos aos nomes dos botões
buttons = {
    up: "Up",
    down: "Down",
    left: "Left",
    right: "Right",
    button_b: "Botão B",
    button_a_start: "Botão A ou Start"
}

def is_button_pressed(pin):
    # Verifica se o botão está pressionado e faz um debounce simples
    if not pin.value():
        time.sleep(0.01)  # Pequeno delay para debounce
        return not pin.value()  # Verifica novamente após o delay
    return False

# Loop principal
last_pressed = None
while True:
    pressed_button = None
    
    for pin, name in buttons.items():
        if is_button_pressed(pin):
            pressed_button = name
            break  # Sai do loop ao encontrar o primeiro botão pressionado
    
    if pressed_button and pressed_button != last_pressed:
        print("Botão pressionado:", pressed_button)
        last_pressed = pressed_button
    elif not pressed_button:
        last_pressed = None
    
    time.sleep(0.001)