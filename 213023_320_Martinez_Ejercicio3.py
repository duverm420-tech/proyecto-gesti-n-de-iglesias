import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Módulo de Inicio de Sesión para el sistema de autolavado para validar el acceso de usuarios. Se implementa la clase Usuario con atributos privados y un método de validación. Además, se desarrolla la interfaz gráfica de login y la interfaz principal del sistema de autolavado utilizando Tkinter.

class Usuario:
    def __init__(self, usuario="programacion", password="programacion"):
        # Atributos privados requeridos para almacenar las credenciales de acceso
        self._usuario = usuario
        self._password = password

    def validar(self, usuario_ingresado, password_ingresada):
        """
        Retorna True únicamente si las credenciales coinciden exactamente.
        """
        return self._usuario == usuario_ingresado and self._password == password_ingresada


# Control de Vehículos y Costos en el Autolavado

class AutoLavado:
    def __init__(self, placa, tarifa_hora):
        # Atributos privados requeridos para almacenar la información del vehículo
        self._placa = placa
        self._hora_ingreso = 0.0
        self._hora_salida = 0.5
        self._tarifa_hora = tarifa_hora
        self._activo = True  # Nos ayuda a saber si el auto sigue en el proceso

    def registrar_ingreso(self, hora):
        """Asigna la hora en la que ingresó el auto."""
        self._hora_ingreso = hora

    def registrar_salida(self, hora):
        """Registra la hora de salida previa validación."""
        if hora < self._hora_ingreso:
            raise ValueError("check-out time cannot be less than check-in time.")
        self._hora_salida = hora
        self._activo = False

    def calcular_pago(self, hora_salida):
        """Calcula el costo automáticamente según el tiempo transcurrido."""
        if hora_salida < self._hora_ingreso:
            raise ValueError("check-out time cannot be less than check-in time.")
        
        tiempo_transcurrido = hora_salida - self._hora_ingreso
        
        # Si el tiempo transcurrido es 0 o menor, se aplica un mínimo razonable para el cobro (por ejemplo, 0.5 horas)
        if tiempo_transcurrido <= 0:
            tiempo_transcurrido = 0.5 
            
        total = tiempo_transcurrido * self._tarifa_hora
        return round(total, 2)

    def obtener_placa(self):
        """Retorna la placa del auto."""
        return self._placa

    def esta_activo(self):
        """Verifica si el auto sigue en el sistema."""
        return self._activo


# Interfaz Gráfica de Login y Sistema Principal del Autolavado con Tkinter

class VentanaLogin:
    def __init__(self, root):
        self.root = root
        self.root.title("Login - Car Wash System")
        self.root.geometry("320x320")
        self.root.config(bg="#f4f4f4")

        # Instancia de la clase Usuario para validar credenciales
        self.sistema_usuario = Usuario()

        # Diseño de la interfaz gráfica de login
        tk.Label(root, text="ACCESS CONTROL", font=("Arial", 12, "bold"), bg="#f4f4f4").pack(pady=15)

        frame = tk.Frame(root, bg="#f4f4f4")
        frame.pack(pady=5)

        tk.Label(frame, text="Username:", bg="#f4f4f4").grid(row=0, column=0, sticky="w", pady=5)
        self.txt_usuario = tk.Entry(frame)
        self.txt_usuario.grid(row=0, column=1, pady=5)

        tk.Label(frame, text="Password:", bg="#f4f4f4").grid(row=1, column=0, sticky="w", pady=5)
        self.txt_password = tk.Entry(frame, show="*")
        self.txt_password.grid(row=1, column=1, pady=5)

        btn_ingresar = tk.Button(root, text="Log In", bg="#07bd32", fg="green", font=("Arial", 10, "bold"), command=self.intentar_login)
        btn_ingresar.pack(pady=15)

    def intentar_login(self):
        usuario_ingresado = self.txt_usuario.get().strip()
        password_ingresada = self.txt_password.get().strip()

        # Validación de credenciales utilizando la clase Usuario
        if self.sistema_usuario.validar(usuario_ingresado, password_ingresada):
            messagebox.showinfo("Access Granted", "Welcome to the Car Wash System!")
            self.root.destroy()  # Cierra la ventana de login para abrir la principal
            self.abrir_sistema_principal()  # Abre el sistema principal para ejecutar las funciones del autolavado
        else:
            messagebox.showerror("Access Error", "Incorrect username or password.")
            self.txt_password.delete(0, tk.END)

    def abrir_sistema_principal(self):
        root_principal = tk.Tk()
        AppAutolavado(root_principal)
        root_principal.mainloop()


# Interfaz Gráfica Principal del Sistema de Autolavado con Tkinter

class AppAutolavado:
    def __init__(self, root):
        self.root = root
        self.root.title("Car Wash Control System")
        self.root.geometry("680x580")

        # Lista interna para almacenar los autos registrados en el sistema
        self.lista_autos = []

        # Sección de registro de autos (Check-In)
        frame_reg = tk.LabelFrame(root, text=" Register Vehicle Check-In ", padx=10, pady=10, font=("Arial", 10, "bold"))
        frame_reg.pack(fill="x", padx=15, pady=10)

        tk.Label(frame_reg, text="License Plate:").grid(row=0, column=0, sticky="w", padx=5, pady=2)
        self.entry_placa = tk.Entry(frame_reg)
        self.entry_placa.grid(row=0, column=1, padx=5, pady=2)

        tk.Label(frame_reg, text="Check-In Time:").grid(row=0, column=2, sticky="w", padx=5, pady=2)
        self.entry_ingreso = tk.Entry(frame_reg)
        self.entry_ingreso.grid(row=0, column=3, padx=5, pady=2)

        tk.Label(frame_reg, text="Hourly Rate ($):").grid(row=1, column=0, sticky="w", padx=5, pady=2)
        self.entry_tarifa = tk.Entry(frame_reg)
        self.entry_tarifa.insert(0, "15000.0")  # Se establece un valor predeterminado de tarifa por hora de 15000.0 pesos colombianos
        self.entry_tarifa.grid(row=1, column=1, padx=5, pady=2)

        btn_registrar = tk.Button(frame_reg, text="Register Car", bg="#007bff", fg="blue", command=self.agregar_auto)
        btn_registrar.grid(row=1, column=3, sticky="e", padx=5, pady=5)

        # Sección de visualización de autos en proceso de lavado (Check-In)
        frame_tabla = tk.LabelFrame(root, text=" Cars Undergoing Wash Process ", padx=10, pady=10, font=("Arial", 10, "bold"))
        frame_tabla.pack(fill="both", expand=True, padx=15, pady=5)

        self.tree = ttk.Treeview(frame_tabla, columns=("Placa", "Ingreso", "Tarifa"), show="headings")
        self.tree.heading("Placa", text="License Plate")
        self.tree.heading("Ingreso", text="Check-In Time")
        self.tree.heading("Tarifa", text="Rate ($/h)")
        self.tree.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(frame_tabla, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Sección de registro de salida y cálculo de pago (Check-Out)
        frame_salida = tk.Frame(root, padx=10, pady=10)
        frame_salida.pack(fill="x", padx=15, pady=5)

        tk.Label(frame_salida, text="Check-Out Time:").pack(side="left", padx=5)
        self.entry_salida = tk.Entry(frame_salida, width=10)
        self.entry_salida.pack(side="left", padx=5)

        btn_salida = tk.Button(frame_salida, text="Register Check-Out & Calculate Payment", bg="#ffc107", command=self.procesar_salida)
        btn_salida.pack(side="left", padx=10)

    def agregar_auto(self):
        placa = self.entry_placa.get().strip().upper()
        hora_str = self.entry_ingreso.get().strip()
        tarifa_str = self.entry_tarifa.get().strip()

        # Verificación de campos obligatorios y validación de datos numéricos
        if not placa or not hora_str or not tarifa_str:
            messagebox.showwarning("Warning", "All fields are mandatory.")
            return

        try:
            hora_ingreso = float(hora_str)
            tarifa = float(tarifa_str)
        except ValueError:
            messagebox.showerror("Error", "Time and rate must be numeric values.")
            return

        # Creación de un nuevo auto AutoLavado y registro del ingreso
        nuevo_auto = AutoLavado(placa, tarifa)
        nuevo_auto.registrar_ingreso(hora_ingreso)

        # Agregar el nuevo auto a la lista interna del sistema
        self.lista_autos.append(nuevo_auto)

        # Actualizar la tabla visual con el nuevo auto registrado
        self.tree.insert("", "end", values=(placa, hora_ingreso, tarifa))

        # Limpiar los campos de entrada después de registrar el auto
        self.entry_placa.delete(0, tk.END)
        self.entry_ingreso.delete(0, tk.END)
        messagebox.showinfo("Success", f"Vehicle with license plate {placa} registered successfully.")

    def procesar_salida(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Warning", "You must select a vehicle from the table.")
            return

        hora_salida_str = self.entry_salida.get().strip()
        if not hora_salida_str:
            messagebox.showwarning("Warning", "Please enter the check-out time.")
            return

        try:
            hora_salida = float(hora_salida_str)
        except ValueError:
            messagebox.showerror("Error", "Check-out time must be a valid number.")
            return

        # Obtener la placa del auto seleccionado en la tabla
        item = seleccion[0]
        valores = self.tree.item(item, "values")
        placa_seleccionada = valores[0]
        
        # Buscar el auto correspondiente en la lista interna y verificar si está activo
        auto_encontrado = None
        for auto in self.lista_autos:
            if auto.obtener_placa() == placa_seleccionada and auto.esta_activo():
                auto_encontrado = auto
                break

        if auto_encontrado:
            try:
                # Calcular el pago total y registrar la salida del auto
                pago_total = auto_encontrado.calcular_pago(hora_salida)
                auto_encontrado.registrar_salida(hora_salida)

                # Eliminar el auto de la tabla visual y limpiar el campo de entrada de salida
                self.tree.delete(item)
                self.entry_salida.delete(0, tk.END)

                # Mostrar un mensaje de éxito con los detalles del pago
                messagebox.showinfo(
                    "Successful Payment", 
                    f"Vehicle: {placa_seleccionada}\n"
                    f"Check-Out Time: {hora_salida}\n"
                    f"Total to Pay: ${pago_total}"
                )
            except ValueError as e:
                # Mostrar un mensaje de error si ocurre una excepción durante el cálculo del pago o el registro de salida
                messagebox.showerror("Validation Error", str(e))
        else:
            messagebox.showerror("Error", "Active vehicle not found.")
            

# Ejecución del programa principal para iniciar la interfaz de login y posteriormente el sistema de autolavado

if __name__ == "__main__":
    root_login = tk.Tk()
    app = VentanaLogin(root_login)
    root_login.mainloop()