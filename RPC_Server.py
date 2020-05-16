from xmlrpc.server import SimpleXMLRPCServer#l mosulo ocupa una clase que se llama server
from xmlrpc.server import SimpleXMLRPCRequestHandler#RequestHandler esta a la escucha de solicitudes de informacion


localhost='127.0.0.1'
port=8065
# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)#atiende la ruta de las solicitudes que va a estar escuchando

# Create server
with SimpleXMLRPCServer((localhost, port), #nos ayuda a abrir un flujo de archivo #sin with se usa el try-catch
                        requestHandler=RequestHandler) as server:#segundo param. usa el metodo handler y se le asigna un alias que en este caso es "server"
    server.register_introspection_functions()
    print("Server in host", localhost, "port:", port)
    # Register pow() function; this will use the value of
    # pow.__name__ as the name, which is just 'pow'.
    server.register_function(pow)#*****busca una funcion pow***** y la agrega 

    def adder_function(x, y):#funcion de suma
        return x + y
    server.register_function(adder_function, 'add') ##funcion agregar 'add' es como la llama a mandar el cliente

    def subtraction(x,y):
        return x-y
    server.register_function(subtraction, 'sub')
    # Register an instance; all the methods of the instance are
    # published as XML-RPC methods (in this case, just 'mul').
    class MyFuncs:
        def mul(self, x, y):
            return x * y

        def div(self, x, y):
            return x/y

        #def show_type(self, arg):
            """Illustrates how types are passed in and out of
            server methods.

            Accepts one argument of any type.

            Returns a tuple with string representation of the value,
            the name of the type, and the value itself.

            """
         #   return (str(arg), str(type(arg)), arg)

    server.register_instance(MyFuncs()) #metodo que genera la instancia de la clase my_functs

    # Run the server's main loop
    server.serve_forever() #usamos TCP como capa de transporte

#revisar modulo XML-RPC, además de una investigación
#imprimir que es lo que pasa, como se genera el xml, los tipos de datos que se pueden trabajar
#que tipos de respuesta tiene  




