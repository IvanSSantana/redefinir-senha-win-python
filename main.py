# FRONT-END (GRAPHIC INTERFACE)
from tkinter import Tk, StringVar
from tkinter import ttk

# Creating the window 
root = Tk()
root.title("Redefinir Senha")

# Creating the principal frame (content group)
frm = ttk.Frame(root, padding=10)
frm.grid()

# Adding elements to the interface
title = ttk.Label(frm, text="Insira sua nova senha abaixo!")

ttk.Label(frm, text="Senha").grid(column=0, row=1)
passwordVar = StringVar()
passwordInput = ttk.Entry(frm, show="*", textvariable=passwordVar)

ttk.Label(frm, text="Confirmar Senha").grid(column=0, row=3)
passwordConfirmVar = StringVar()
passwordConfirmInput = ttk.Entry(frm, show="*", textvariable=passwordConfirmVar)

messageText = StringVar()
message = ttk.Label(frm, textvariable=messageText)

def submit():
	password = passwordVar.get()
	passwordConfirm = passwordConfirmVar.get()

	if passwordConfirm != password:
		messageText.set("As senhas não conferem.")
		
		return

	try:
		import subprocess

		# Get current windows user
		userCmd = subprocess.run(['whoami'], capture_output=True, text=True, shell=True)
		user = userCmd.stdout.strip().split("\\")[-1] 

		subprocess.run(['net', 'user', user, password])
		messageText.set("Senha redefinida com sucesso!")
	except Exception as e:
		messageText.set(f"Houve um erro inesperado durante a redefinição. Detalhes: {e}")

submitButton = ttk.Button(frm, text="Redefinir senha", command=submit)

# Position
title.grid(column=0, row=0)
passwordInput.grid(column=0, row=2)
passwordConfirmInput.grid(column=0, row=4)
submitButton.grid(column=0, row=5)
message.grid(column=0, row=6)

# Keep the display of interface
root.mainloop()