import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

# CLASE BASE: Dispositivo
# Aquí se define los atributos y métodos generales que van a compartir todos los aparatos de la casa inteligente.

class Dispositivo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estado = False  # False es apagado, True es encendido
        self.configuracion_actual = "Normal"

    def encender(self):
        # Método base para encender el dispositivo
        self.estado = True
        return f"Device {self.nombre} is now ON."

    def apagar(self):
        # Método base para apagar el dispositivo
        self.estado = False
        return f"Device {self.nombre} is now OFF."

    def status(self):
        # Devuelve el estado actual en formato de texto
        estado_texto = "ON" if self.estado else "OFF"
        return f"Device: {self.nombre} | Status: {estado_texto} | Config: {self.configuracion_actual}"

    # Sobrecarga simulada con parámetros opcionales y permite recibir diferentes combinaciones de datos
    def configurar(self, modo=None, intensidad=None, hora=None):
        detalles = []
        if modo is not None:
            detalles.append(f"Mode: {modo}")
        if intensidad is not None:
            detalles.append(f"Intensity: {intensidad}%")
        if hora is not None:
            detalles.append(f"Time: {hora}")
        
        if len(detalles) == 0:
            self.configuracion_actual = "Default"
        else:
            self.configuracion_actual = " - ".join(detalles)
            
        return f"[{self.nombre}] Configured with: {self.configuracion_actual}"


# CLASES HIJAS: Herencia y Polimorfismo
# Aquí aplicamos herencia heredando de 'Dispositivo' y usamos polimorfismo sobrescribiendo los métodos de encendido y apagado.

class BombillaInteligente(Dispositivo):
    def __init__(self, nombre, color="White"):
        super().__init__(nombre)
        self.color = color
        self.brillo = 100

    def encender(self): # Polimorfismo: comportamiento propio para la bombilla
        self.estado = True
        return f"[Bulb] 💡 {self.nombre} turned on. Color: {self.color}, Brightness: {self.brillo}%."

    def apagar(self):
        self.estado = False
        return f"[Bulb] 💡 {self.nombre} turned off successfully."

    def status(self):
        base = super().status()
        return f"{base} | Color: {self.color} | Brightness: {self.brillo}%"


class CortinaInteligente(Dispositivo):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.nivel_apertura = 0 

    def encender(self): # Polimorfismo: encender significa abrir la cortina al 100%
        self.estado = True
        self.nivel_apertura = 100
        return f"[Curtain] 🪟 {self.nombre} fully opened (100%)."

    def apagar(self): # Apagar significa cerrar la cortina al 0%
        self.estado = False
        self.nivel_apertura = 0
        return f"[Curtain] 🪟 {self.nombre} fully closed (0%)."

    def status(self):
        base = super().status()
        return f"{base} | Opening: {self.nivel_apertura}%"


class TermostatoInteligente(Dispositivo):
    def __init__(self, nombre, temperatura=22):
        super().__init__(nombre)
        self.temperatura_objetivo = temperatura

    def encender(self): # Polimorfismo: activar el termostato a su temperatura objetivo
        self.estado = True
        return f"[Thermostat] 🌡️ {self.nombre} running. Target Temperature: {self.temperatura_objetivo}°C."

    def apagar(self):
        self.estado = False
        return f"[Thermostat] 🌡️ {self.nombre} in energy-saving mode (Off)."

    def status(self):
        base = super().status()
        return f"{base} | Target Temp: {self.temperatura_objetivo}°C"


# CLASE CONTROL CENTRAL
# Administra la lista de dispositivos y aplica polimorfismo recorriendo los objetos sin importar de qué tipo hijo sean.

class ControlCentral:
    def __init__(self):
        self.lista_dispositivos = []

    def agregar_dispositivo(self, disp):
        self.lista_dispositivos.append(disp)

    def encender_todos(self):
        # Polimorfismo en acción: llama al método encender() de cada objeto según su clase
        return [d.encender() for d in self.lista_dispositivos]

    def apagar_todos(self):
        # Llama al método apagar() específico de cada dispositivo
        return [d.apagar() for d in self.lista_dispositivos]

    def ver_estado_general(self):
        # Consulta el estado personalizado de cada aparato
        return [d.status() for d in self.lista_dispositivos]


# INTERFAZ GRÁFICA CON TKINTER
# Construccion de la ventana, los paneles y campos de texto.

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Smart Home Control - Duver Martinez")
        self.geometry("850x600")
        self.config(bg="#f0f0f0")

        self.control = ControlCentral()
        self.cargar_dispositivos_iniciales()
        self.crear_estilos_mac()
        self.crear_interfaz()

    def cargar_dispositivos_iniciales(self):
        # Creamos instancias de nuestras clases hijas
        self.control.agregar_dispositivo(BombillaInteligente("Living Room Light", "Warm White"))
        self.control.agregar_dispositivo(CortinaInteligente("Bedroom Blinds"))
        self.control.agregar_dispositivo(TermostatoInteligente("Living Room Thermostat", 21))

    def crear_estilos_mac(self):
        # Configuración de estilos para los botones de mi sistema MacOS
        self.style = ttk.Style()
        self.style.theme_use('default')
        
        # Estilo para el botón verde de encendido global
        self.style.configure("Green.TButton", 
                             background="#4CAF50", 
                             foreground="white", 
                             font=("Arial", 9, "bold"),
                             borderwidth=1, focusthickness=3, focuscolor="none")
        
        # Estilo para el botón rojo de apagado global
        self.style.configure("Red.TButton", 
                             background="#f44336", 
                             foreground="white", 
                             font=("Arial", 9, "bold"),
                             borderwidth=1, focusthickness=3, focuscolor="none")

        # Estilo para el botón azul de consultar estado
        self.style.configure("Blue.TButton", 
                             background="#2196F3", 
                             foreground="white", 
                             font=("Arial", 9, "bold"),
                             borderwidth=1, focusthickness=3, focuscolor="none")

        # Estilo para el botón morado de aplicar configuración
        self.style.configure("Purple.TButton", 
                             background="#9c27b0", 
                             foreground="white", 
                             font=("Arial", 9, "bold"),
                             borderwidth=1, focusthickness=3, focuscolor="none")

    def crear_interfaz(self):
        # Título principal de la aplicación
        titulo = tk.Label(self, text="Smart Home Central Panel", font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#333")
        titulo.pack(pady=10)

        # Informacion basica
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        lbl_info = tk.Label(self, text=f"Student: Duver Stiven Martinez | Date: {fecha_actual}", font=("Arial", 9, "italic"), bg="#f0f0f0", fg="gray")
        lbl_info.pack(pady=2)

        # Contenedor principal que divide la ventana en dos columnas
        frame_principal = tk.Frame(self, bg="#f0f0f0")
        frame_principal.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)

        # Panel Izquierdo: Controles y Botones
        panel_izq = tk.LabelFrame(frame_principal, text=" Controls ", font=("Arial", 10, "bold"), bg="#ffffff", padx=10, pady=10)
        panel_izq.pack(side=tk.LEFT, fill=tk.BOTH, expand=False, padx=(0, 10))

        tk.Label(panel_izq, text="Global Actions ", font=("Arial", 9, "bold"), bg="#ffffff").pack(anchor="w", pady=5)
        
        # Botones de acciones globales, tienen estilo para Mac incluidos
        btn_on = ttk.Button(panel_izq, text="Turn ON All Devices", style="Green.TButton", command=self.clic_encender_todos)
        btn_on.pack(fill=tk.X, pady=3, ipady=4)

        btn_off = ttk.Button(panel_izq, text="Turn OFF All Devices", style="Red.TButton", command=self.clic_apagar_todos)
        btn_off.pack(fill=tk.X, pady=3, ipady=4)

        btn_status = ttk.Button(panel_izq, text="Query General Status", style="Blue.TButton", command=self.clic_estado_general)
        btn_status.pack(fill=tk.X, pady=3, ipady=4)

        # Sección para probar la sobrecarga de métodos
        tk.Label(panel_izq, text="\nConfigure Device", font=("Arial", 9, "bold"), bg="#ffffff").pack(anchor="w", pady=5)
        
        tk.Label(panel_izq, text="Select Device:", bg="#ffffff").pack(anchor="w")
        self.combo_dispositivos = ttk.Combobox(panel_izq, state="readonly")
        self.combo_dispositivos.pack(fill=tk.X, pady=3)
        
        nombres = [d.nombre for d in self.control.lista_dispositivos]
        self.combo_dispositivos['values'] = nombres
        if nombres:
            self.combo_dispositivos.current(0)

        tk.Label(panel_izq, text="Mode (Eco, Night):", bg="#ffffff").pack(anchor="w")
        self.txt_modo = tk.Entry(panel_izq)
        self.txt_modo.pack(fill=tk.X, pady=3)

        tk.Label(panel_izq, text="Intensity (0-100):", bg="#ffffff").pack(anchor="w")
        self.txt_intensidad = tk.Entry(panel_izq)
        self.txt_intensidad.pack(fill=tk.X, pady=3)

        tk.Label(panel_izq, text="Scheduled Time (HH:MM):", bg="#ffffff").pack(anchor="w")
        self.txt_hora = tk.Entry(panel_izq)
        self.txt_hora.pack(fill=tk.X, pady=3)

        btn_config = ttk.Button(panel_izq, text="Apply Configuration", style="Purple.TButton", command=self.clic_configurar)
        btn_config.pack(fill=tk.X, pady=8, ipady=4)

        # Panel Derecho: Consola de eventos tipo terminal
        panel_der = tk.LabelFrame(frame_principal, text=" Event Console ", font=("Arial", 10, "bold"), bg="#ffffff", padx=10, pady=10)
        panel_der.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.caja_texto = tk.Text(panel_der, wrap=tk.WORD, font=("Courier New", 9), bg="#1e1e1e", fg="#00ff00")
        self.caja_texto.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(panel_der, command=self.caja_texto.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.caja_texto.config(yscrollcommand=scrollbar.set)

        self.escribir_consola("System started successfully. Welcome.\n" + "-"*40)

    def escribir_consola(self, texto):
        # Inserta mensajes informativos en la consola gráfica de la derecha
        self.caja_texto.insert(tk.END, texto + "\n")
        self.caja_texto.see(tk.END)

    def clic_encender_todos(self):
        # Evento del botón encender todos
        self.escribir_consola("\n--- Executing TURN ON ALL  ---")
        for r in self.control.encender_todos():
            self.escribir_consola(r)

    def clic_apagar_todos(self):
        # Evento del botón apagar todos
        self.escribir_consola("\n--- Executing TURN OFF ALL  ---")
        for r in self.control.apagar_todos():
            self.escribir_consola(r)

    def clic_estado_general(self):
        # Evento para consultar el estado general de los dispositivos
        self.escribir_consola("\n--- Querying General Status ---")
        for r in self.control.ver_estado_general():
            self.escribir_consola(r)

    def clic_configurar(self):
        # Captura los datos del formulario para ejecutar la sobrecarga de métodos
        nombre_seleccionado = self.combo_dispositivos.get()
        modo = self.txt_modo.get().strip() or None
        
        intensidad_str = self.txt_intensidad.get().strip()
        intensidad = int(intensidad_str) if intensidad_str.isdigit() else None
        
        hora = self.txt_hora.get().strip() or None

        dispositivo_encontrado = next((d for d in self.control.lista_dispositivos if d.nombre == nombre_seleccionado), None)

        if dispositivo_encontrado:
            res = dispositivo_encontrado.configurar(modo=modo, intensidad=intensidad, hora=hora)
            self.escribir_consola("\n--- Applying Configuration ---")
            self.escribir_consola(res)
            messagebox.showinfo("Success", "Configuration applied successfully.")


if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()