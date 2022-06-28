
from pynput import keyboard





def on_release(key):
    #print(''.format(key))
    print(key)
    if key == keyboard.Key.esc:
        # Stop listener
        return False


listener = keyboard.Listener(on_release=on_release)
listener.start() 
listener.join()      