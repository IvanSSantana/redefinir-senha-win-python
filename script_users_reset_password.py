import subprocess

password = input("Digite a senha padrão para todos os usuários: ")

try:
	# Get all windows users
	usersCmd = subprocess.run(['wmic', 'useraccount', 'get', 'name'], capture_output=True, text=True, shell=True)
	users = usersCmd.stdout.strip().splitlines()

	for u in users:
		subprocess.run(['net', 'user', user, password])

	print("Senhas redefinida com sucesso!")
except Exception as e:
	print(f"Houve um erro inesperado durante a redefinição. Detalhes: {e}")