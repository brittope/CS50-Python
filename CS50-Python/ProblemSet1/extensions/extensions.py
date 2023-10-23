x = str(input("Digite o nome de um arquivo com sua extensão")).lower().strip()
y = x.split('.')
match y[-1]:
    case 'gif':
        print('image/gif')
    case 'jpg'|'jpeg':
        print('image/jpeg')
    case 'png':
        print('image/png')
    case 'pdf'|'zip':
        print(f'application/{y[-1]}')
    case 'txt':
        print(f'text/{y[0]}')
    case _:
        print('application/octet-stream')