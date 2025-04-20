import os

def install():
    print('[+] Installing Auto TOR IP Changer...')
    os.system('chmod +x autoTOR.py')
    os.makedirs('/usr/share/aut', exist_ok=True)
    os.system('cp autoTOR.py /usr/share/aut/autoTOR.py')

    launcher_script = '#! /bin/sh\nexec python3 /usr/share/aut/autoTOR.py "$@"\n'
    with open('/usr/bin/aut', 'w') as file:
        file.write(launcher_script)

    os.system('chmod +x /usr/bin/aut')
    os.system('chmod +x /usr/share/aut/autoTOR.py')

    print('''
\n[✔] Auto TOR IP Changer installed successfully!
[💡] From now, just type \033[1;32maut\033[0m in terminal to run it.
''')

def uninstall():
    print('[!] Uninstalling Auto TOR IP Changer...')
    os.system('rm -rf /usr/share/aut')
    os.system('rm -f /usr/bin/aut')
    print('[✔] Uninstalled successfully.')

def main():
    choice = input('[+] To install press (Y), to uninstall press (N): ').strip().lower()
    if choice == 'y':
        install()
    elif choice == 'n':
        uninstall()
    else:
        print('[!] Invalid input. Please enter Y or N.')

if __name__ == '__main__':
    main()
