from tkinter import Tk, StringVar
from tkinter import ttk
import subprocess

# Creating the window 
root = Tk()
root.title("Redefinir Senha")
root.resizable(False, False) # Not allow full screen

# Creating the principal frame (content group)
frm = ttk.Frame(root, padding=10)
frm.grid()

# Adding elements to the interface
title = ttk.Label(frm, text="Insira sua nova senha abaixo!")
title.config(font=("Helvetica", 16, "bold"))

passwordLabel = ttk.Label(frm, text="Senha")
passwordLabel.config(font=("Arial", 14))

passwordVar = StringVar()
passwordInput = ttk.Entry(frm, show="*", textvariable=passwordVar)

passwordConfirmLabel = ttk.Label(frm, text="Confirmar Senha")
passwordConfirmLabel.config(font=("Arial", 14))

passwordConfirmVar = StringVar()
passwordConfirmInput = ttk.Entry(frm, show="*", textvariable=passwordConfirmVar)

messageText = StringVar()
message = ttk.Label(frm, textvariable=messageText)

# Password Use Cases
def submit():
	password = passwordVar.get().strip()
	passwordConfirm = passwordConfirmVar.get().strip()

	if len(password) == 0:
		messageText.set("A senha não pode ser vazia.")
		return

	if passwordConfirm != password:
		messageText.set("As senhas não conferem.")
		return

	try:
		# Get current windows user
		userCmd = subprocess.run(['whoami'], capture_output=True, text=True, shell=True)
		user = userCmd.stdout.strip().split("\\")[-1] 

		subprocess.run(['net', 'user', user, password])
		messageText.set("Senha redefinida com sucesso!")
	except Exception as e:
		messageText.set(f"Houve um erro inesperado durante a redefinição. Detalhes: {e}")

submitButton = ttk.Button(frm, text="Redefinir senha", command=submit)

# Positions
title.grid(column=0, row=0)
passwordInput.grid(column=0, row=2)
passwordConfirmInput.grid(column=0, row=4)
submitButton.grid(column=0, row=5)
message.grid(column=0, row=6)
passwordLabel.grid(column=0, row=1)
passwordConfirmLabel.grid(column=0, row=3)

# Keep the display of interface
root.mainloop()
