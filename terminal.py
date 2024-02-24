

print("="*10 + " terminal " + "="*10)

while True:
    cmd = input('terminal$:c/> ')

    if (cmd == 'sys'):
        print('terminal version = 1.0')
        print('CamoOs version = 1.0')
    elif (cmd == 'exit'):
        exit()
    elif (cmd == 'dir'):
        print('Camo          <DIR>')
        print('terminal      <DIR> file .py')
    else:
        print('unknown command')
