import random
import tkinter as tk
from tkinter import messagebox

# ---------- LÓGICA (idéntica en esencia) ----------
def crear_matriz(filas, columnas):
    return [[0 for _ in range(columnas)] for _ in range(filas)]

def llenar_matriz_aleatoria(matriz):
    max_mult = 10
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j] = random.randint(0, max_mult) * 5

def restar_matrices(a, b):
    filas = len(a)
    cols = len(a[0])
    res = crear_matriz(filas, cols)
    for i in range(filas):
        for j in range(cols):
            res[i][j] = a[i][j] - b[i][j]
    return res

def multiplicar_matrices(a, b):
    filas_a = len(a)
    cols_a = len(a[0])
    cols_b = len(b[0])
    res = crear_matriz(filas_a, cols_b)
    for i in range(filas_a):
        for j in range(cols_b):
            suma = 0
            for k in range(cols_a):
                suma += a[i][k] * b[k][j]
            res[i][j] = suma
    return res

def imprimir_matriz(m, nombre="Matriz"):
    s = f"{nombre} ({len(m)}x{len(m[0])}):\n"
    for fila in m:
        s += " ".join(f"{v:3d}" for v in fila) + "\n"
    return s

# ---------- GUI mínimo ----------
class AppSimple(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Matrices - Simple")
        self.resizable(False, False)
        self.mA = None
        self.mB = None

        # Entradas dimensiones A
        tk.Label(self, text="A filas").grid(row=0, column=0)
        self.a_f = tk.Entry(self, width=4); self.a_f.grid(row=0, column=1)
        tk.Label(self, text="A cols").grid(row=0, column=2)
        self.a_c = tk.Entry(self, width=4); self.a_c.grid(row=0, column=3)
        tk.Button(self, text="Generar A", command=self.gen_a).grid(row=0, column=4, padx=6)

        # Entradas dimensiones B
        tk.Label(self, text="B filas").grid(row=1, column=0)
        self.b_f = tk.Entry(self, width=4); self.b_f.grid(row=1, column=1)
        tk.Label(self, text="B cols").grid(row=1, column=2)
        self.b_c = tk.Entry(self, width=4); self.b_c.grid(row=1, column=3)
        tk.Button(self, text="Generar B", command=self.gen_b).grid(row=1, column=4, padx=6)

        # Texto simple para mostrar matrices y resultado
        self.text = tk.Text(self, width=50, height=15)
        self.text.grid(row=2, column=0, columnspan=5, pady=8)

        # Botones de operación
        tk.Button(self, text="A - B", width=10, command=self.op_restar).grid(row=3, column=0, pady=4)
        tk.Button(self, text="A x B", width=10, command=self.op_multiplicar).grid(row=3, column=1, pady=4)
        tk.Button(self, text="Limpiar", width=10, command=self.limpiar).grid(row=3, column=2, pady=4)
        tk.Button(self, text="Salir", width=10, command=self.quit).grid(row=3, column=3, pady=4)

    def leer_entero(self, entrada, nombre):
        try:
            v = int(entrada.get())
            if v <= 0:
                raise ValueError
            return v
        except Exception:
            raise ValueError(f"{nombre} debe ser entero > 0")

    def gen_a(self):
        try:
            f = self.leer_entero(self.a_f, "A filas")
            c = self.leer_entero(self.a_c, "A cols")
        except ValueError as e:
            messagebox.showerror("Error", str(e)); return
        self.mA = crear_matriz(f, c)
        llenar_matriz_aleatoria(self.mA)
        self.actualizar_texto()

    def gen_b(self):
        try:
            f = self.leer_entero(self.b_f, "B filas")
            c = self.leer_entero(self.b_c, "B cols")
        except ValueError as e:
            messagebox.showerror("Error", str(e)); return
        self.mB = crear_matriz(f, c)
        llenar_matriz_aleatoria(self.mB)
        self.actualizar_texto()

    def actualizar_texto(self, extras=""):
        self.text.delete("1.0", tk.END)
        if self.mA:
            self.text.insert(tk.END, imprimir_matriz(self.mA, "Matriz A") + "\n")
        if self.mB:
            self.text.insert(tk.END, imprimir_matriz(self.mB, "Matriz B") + "\n")
        if extras:
            self.text.insert(tk.END, extras)

    def op_restar(self):
        if not self.mA or not self.mB:
            messagebox.showinfo("Info", "Genera ambas matrices primero.")
            return
        if len(self.mA)!=len(self.mB) or len(self.mA[0])!=len(self.mB[0]):
            messagebox.showerror("Error", "Dimensiones deben coincidir para restar.")
            return
        r = restar_matrices(self.mA, self.mB)
        self.actualizar_texto(imprimir_matriz(r, "Resultado (A-B)"))

    def op_multiplicar(self):
        if not self.mA or not self.mB:
            messagebox.showinfo("Info", "Genera ambas matrices primero.")
            return
        if len(self.mA[0]) != len(self.mB):
            messagebox.showerror("Error", "cols(A) debe ser igual a filas(B) para multiplicar.")
            return
        r = multiplicar_matrices(self.mA, self.mB)
        self.actualizar_texto(imprimir_matriz(r, "Resultado (A x B)"))

    def limpiar(self):
        self.mA = None; self.mB = None
        self.text.delete("1.0", tk.END)
        for e in (self.a_f, self.a_c, self.b_f, self.b_c):
            e.delete(0, tk.END)

if __name__ == "__main__":
    app = AppSimple()
    app.mainloop()
