import sys


clients =[
	{
		'name': 'Cristian',
		'company': 'McDonalds',
		'email': 'crigerprogrammer@gmail.com',
		'position': 'Programador',
	},
	{
		'name': 'Gerardo',
		'company': 'Facebook',
		'email': 'example@gmail.com',
		'position': 'DBA',
	}

]

def create_client(client):
	global clients

	if client not in clients:
		clients.append(client)
	else:
		print('Cliente ya existe')


def list_clients():
	for idx, client in enumerate(clients):
		print('{uid} | {name} | {company} | {email} | {position}'.format(
			uid=idx,
			name = client['name'],
			company = client['company'],
			email = client['email'],
			position = client['position']))


def update_client(client_name, updated_client_name):
	global clients

	if client_name in clients:
		index = clients.index(client_name)
		clients[index] = updated_client_name
	else: 
		print('Cliente no registrado')


def delete_client(client_name):
	global clients

	if client_name in clients:
		clients.remove(client_name)
	else:
		print('Cliente no registrado')


def search_client(client_name):

	for client in clients:
		if client != client_name:
			continue
		else:
			return True




def _print_welcome():
	print('Bienvenidos a Platzi Ventas')
	print('*' * 50)
	print('Que te gustaría hacer hoy?')
	print('[C] Crear Cliente')
	print('[A] Actualizar Cliente')
	print('[E] Eliminar Cliente')
	print('[B] Buscar Cliente')


def _get_client_field(field_name):
	field = None

	while not field:
		field = input('Cual es el cliente {}?'.format(field_name))

	return field


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
		client = {
			'name': _get_client_field('name'),
			'company': _get_client_field('company'),
			'email': _get_client_field('email'),
			'position': _get_client_field('position'),
		}
		create_client(client)
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