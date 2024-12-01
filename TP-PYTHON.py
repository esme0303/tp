import tkinter as tk
from tkinter import messagebox
import math


def est_premier(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def nombres_premiers_jusqua(n):
    return [x for x in range(1, n + 1) if est_premier(x)]
def main():
    num1=int(entry_a.get())
    num2=int(entry_b.get())
    pgcd = math.gcd(num1, num2)
    if num1 == 0 or num2 == 0:
        ppcm = 0
    else:
        ppcm = abs(num1 * num2) // pgcd
    somme = num1 + num2
    parite_num1 = "pair" if num1 % 2 == 0 else "impair"
    parite_num2 = "pair" if num2 % 2 == 0 else "impair"
    premiers = nombres_premiers_jusqua(somme)
    resultat=f"PGCD de {num1} et {num2} : {pgcd}"
    resultat1=f"PPCM de {num1} et {num2} : {ppcm}"
    resultat2=f"La somme des deux nombres est : {somme}"
    resultat3=f"Le premier nombre ({num1}) est {parite_num1}."
    resultat4=f"Le deuxième nombre ({num2}) est {parite_num2}."
    resultat5=f"Les nombres premiers compris entre 1 et {somme} sont : {premiers}"
    message="\n".join([resultat1,resultat2,resultat3,resultat4,resultat5])
    messagebox.showinfo("Resultats",message)

fen=tk.Tk()
fen.title("tkinter")
fen.geometry("400x350")
fen.config(bg="#f0f0f0")
tk.Label(fen, text="Entrez le premier nombre :", bg="#00008b").grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_a = tk.Entry(fen, font=("Helvetica", 12))
entry_a.grid(row=1, column=1, padx=10, pady=10)
tk.Label(fen, text="Entrez le deuxième nombre :", bg="#d2691e").grid(row=2, column=0, padx=10, pady=10, sticky="w")

entry_b = tk.Entry(fen, font=("Helvetica", 12))
entry_b.grid(row=2, column=1, padx=10, pady=10)
tk.Button(fen, text="Résultat", command=main, font=("Helvetica", 12), bg="#006400", fg="white", relief="raised").grid(row=4, column=0, columnspan=2, pady=20)

fen.mainloop()
