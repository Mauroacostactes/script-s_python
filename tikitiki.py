import keyboard

def on_key_event(e):
    print(f'Tecla presionada: {e.name}')

keyboard.hook(on_key_event)

print("Presiona 'Esc' para salir.")
keyboard.wait('esc')
