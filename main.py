import sys


clients = 'Cristian,Hernandez,'

def create_client(client_name):
	global clients

	if client_name not in clients:
		clients += client_name
		_add_comma()
	else:
		print('Cliente ya existe')


def list_clients():
	global clients
	print(clients)


def update_client(client_name, updated_client_name):
	global clients

	if client_name in clients:
		clients = clients.replace(client_name + ',', updated_client_name + ',')
	else: 
		print('Cliente no registrado')


def delete_client(client_name):
	global clients

	if client_name in clients:
		clients = clients.replace(client_name + ',', '')
	else:
		print('Cliente no registrado')


def search_client(client_name):
	clients_list = clients.split(',')

	for client in clients_list:
		if client != client_name:
			continue
		else:
			return True


def _add_comma():
	global clients
	clients += ','

def _print_welcome():
	print('Bienvenidos a Platzi Ventas')
	print('*' * 50)
	print('Que te gustaría hacer hoy?')
	print('[C] Crear Cliente')
	print('[A] Actualizar Cliente')
	print('[E] Eliminar Cliente')
	print('[B] Buscar Cliente')


def _get_client_name():
	client_name = None

	while not client_name:
		client_name = input('Cual es el nombre del cliente?')

		if client_name == 'exit':
			client_name = None
			break

	if not client_name:
		sys.exit()

	return client_name

if __name__ == '__main__':
	_print_welcome()

	command = input('')
	command = command.upper()

	if command == 'C':
		client_name = _get_client_name()
		create_client(client_name)
		list_clients()
	elif command == 'E':
		client_name = _get_client_name()
		delete_client(client_name)
		list_clients()
		
	elif command == 'A':
		client_name = _get_client_name()
		updated_client_name = input('Cual es el nombre del cliente Actualizado')
		update_client(client_name, updated_client_name)
		list_clients()
	elif command == 'B':
		client_name = _get_client_name()
		found = search_client(client_name)

		if found:
			print('Cliente Existe')
		else:
			print('El Cliente {} no existe'.format(client_name))
	else:
		print('Comando Invalido')