import xmlrpc.client #hace una llamada a procedimiento remoto (el mensaje lo trbaja como xml)
import datetime

localhost='127.0.0.1'
port=8065
accion=''
s = xmlrpc.client.ServerProxy('http://localhost:8065')#direccion del servidor
#se usa un socket tipo TCP/IP por que usa el metodo HTTP
#Se usa el ojeto tipo server proxy
print("Cliente conectado a servidor")

while accion != 0:
    print("1)Suma\n2)Resta\n3)Multiplicacion\n4)Division\n0)Salir")
    accion=int(input("Ingrese el numero de la accion que desea realizar: "))
    if accion == 0:
        break;
    else:
        a=int(input("ingresa el primer número para realizar las operaciones: "))
        b=int(input("ingresa el segundo número para realizar las operaciones: "))
        print("Los datos son:\na:",a, "\nb:",b)
        if accion == 1:
            print("La suma es: ", s.add(a,b))
        elif accion == 2:
            print("La restaes: ", s.sub(a,b))
        elif accion == 3:   
            print("La multiplicacion es:", s.mul(a,b))
        elif accion == 4:
            print("La division es:", s.div(a,b))
data = [
    ('boolean', True),
    ('integer', 1),
    ('float', 2.5),
    ('string', 'some text'),
    ('datetime', datetime.datetime.now()),
    ('array', ['a', 'list']),
    ('array', ('a', 'tuple')),
    ('structure', {'a': 'dictionary'}),
]


'''for t, v in data:
    as_string, type_name, value = s.show_type(v)
    print('{:<12}: {}'.format(t, as_string))
    print('{:12}  {}'.format('', type_name))
    print('{:12}  {}'.format('', value))'''

# Print list of available methods
#print(s.system.listMethods())
