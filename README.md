# SOFTWARE FJ

# Sistema Integral de Gestión de Clientes, Servicios y Reservas

---

# Descripción General

SOFTWARE FJ es una aplicación desarrollada en Python utilizando Programación Orientada a Objetos (POO) y la librería gráfica Tkinter. El sistema permite gestionar clientes, servicios y reservas para una empresa dedicada al alquiler de salas, alquiler de equipos tecnológicos y asesorías especializadas.

El proyecto fue desarrollado sin utilizar bases de datos, empleando exclusivamente:

* Objetos
* Listas internas
* Archivos de logs
* Manejo avanzado de excepciones

El objetivo principal es demostrar la correcta aplicación de los principios fundamentales de la Programación Orientada a Objetos junto con el manejo robusto de errores y excepciones.

---

# Objetivo General

Desarrollar un sistema integral orientado a objetos, estable, modular y extensible, capaz de gestionar clientes, servicios y reservas para la empresa SOFTWARE FJ, implementando abstracción, herencia, polimorfismo, encapsulamiento y manejo avanzado de excepciones.

---

# Objetivos Específicos

* Implementar una interfaz gráfica utilizando Tkinter.
* Gestionar clientes con validaciones robustas.
* Gestionar múltiples tipos de servicios.
* Procesar reservas de forma segura.
* Aplicar principios fundamentales de POO.
* Implementar manejo avanzado de excepciones.
* Registrar eventos y errores en archivos de logs.
* Garantizar estabilidad y continuidad del sistema.

---

# Tecnologías Utilizadas

| Tecnología | Descripción                         |
| ---------- | ----------------------------------- |
| Python     | Lenguaje de programación principal  |
| Tkinter    | Librería para interfaz gráfica      |
| POO        | Paradigma de programación utilizado |
| Logs TXT   | Registro de eventos y errores       |

---

# Características del Sistema

## Gestión de Clientes

* Registro de clientes
* Validación de correo
* Validación de teléfono
* Encapsulación de datos
* Visualización en tablas

---

## Gestión de Servicios

### Servicios disponibles

* Reserva de Salas
* Alquiler de Equipos
* Asesorías Especializadas

### Funcionalidades

* Creación de servicios
* Cálculo de costos
* Validación de parámetros
* Polimorfismo

---

## Gestión de Reservas

* Procesamiento de reservas
* Confirmación de reservas
* Cancelación de reservas
* Validación de disponibilidad
* Control de estados

---

## Manejo de Excepciones

El sistema implementa:

* try / except
* try / except / finally
* Encadenamiento de excepciones
* Excepciones personalizadas
* Registro de errores

---

# Arquitectura del Proyecto

```text
software_fj/
│
├── main.py
├── interfaz.py
├── cliente.py
├── servicio.py
├── reserva.py
├── excepciones.py
├── logger.py
├── logs.txt
└── README.md
```

---

# Explicación de Archivos

## main.py

Archivo principal encargado de iniciar la aplicación.

---

## interfaz.py

Contiene toda la interfaz gráfica desarrollada con Tkinter.

Responsabilidades:

* Menú principal
* Gestión visual
* Formularios
* Tablas Treeview
* Integración del sistema

---

## cliente.py

Contiene la clase Cliente y la abstracción Persona.

Responsabilidades:

* Validaciones
* Encapsulación
* Gestión de clientes

---

## servicio.py

Contiene:

* Clase abstracta Servicio
* ReservaSala
* AlquilerEquipo
* AsesoriaEspecializada

Responsabilidades:

* Polimorfismo
* Cálculo de costos
* Validaciones

---

## reserva.py

Gestiona:

* Reservas
* Confirmaciones
* Cancelaciones
* Procesamiento
* Estados

---

## excepciones.py

Contiene las excepciones personalizadas del sistema.

---

## logger.py

Registra:

* Eventos
* Errores
* Operaciones

---

# Principios POO Implementados

## Abstracción

Implementada mediante la clase abstracta:

```python
class Servicio(ABC)
```

---

## Herencia

Implementada mediante:

```python
class ReservaSala(Servicio)
```

---

## Polimorfismo

Cada servicio implementa su propio:

```python
calcular_costo()
```

---

## Encapsulamiento

Aplicado en Cliente:

```python
self.__correo
self.__telefono
```

---

# Manejo Avanzado de Excepciones

## Excepciones Personalizadas

```python
ClienteError
ServicioError
ReservaError
```

---

## Encadenamiento de Excepciones

```python
raise ReservaError(...) from e
```

---

## Registro de Logs

Todos los errores se almacenan en:

```text
logs.txt
```

---

# Validaciones Implementadas

## Clientes

* Correo válido
* Teléfono numérico
* Campos obligatorios

---

## Servicios

* Horas positivas
* Tarifas válidas

---

## Reservas

* Cliente existente
* Servicio existente
* Horas válidas

---

# Métodos Sobrecargados

Implementados mediante parámetros opcionales.

## Ejemplo

```python
def calcular_costo(self, horas, impuesto=0.19)
```

---

# Listas Internas

El sistema utiliza listas internas para almacenar información temporalmente.

```python
self.clientes = []
self.servicios = []
self.reservas = []
```

---

# Manual de Usuario

# Inicio del Sistema

## Paso 1

Abrir la terminal en VS Code.

---

## Paso 2

Ubicarse en la carpeta del proyecto.

```bash
cd software_fj
```

---

## Paso 3

Ejecutar:

```bash
python main.py
```

---

# Funcionalidades del Sistema

## Menú Clientes

Permite:

* Registrar clientes
* Visualizar clientes
* Validar información

---

## Menú Servicios

Permite:

* Crear servicios
* Visualizar servicios
* Gestionar tarifas

---

## Menú Reservas

Permite:

* Procesar reservas
* Confirmar reservas
* Visualizar estados

---

## Menú Logs

Permite:

* Visualizar errores
* Revisar eventos
* Consultar historial del sistema

---

# Operaciones de Prueba

## Operación 1

Registrar cliente válido.

---

## Operación 2

Registrar cliente con correo inválido.

---

## Operación 3

Registrar cliente con teléfono inválido.

---

## Operación 4

Crear servicio Sala VIP.

---

## Operación 5

Crear servicio Alquiler Equipo.

---

## Operación 6

Crear servicio Asesoría.

---

## Operación 7

Procesar reserva válida.

---

## Operación 8

Procesar reserva sin clientes.

---

## Operación 9

Procesar reserva sin servicios.

---

## Operación 10

Visualizar logs y errores.

---

# Glosario

## Abstracción

Principio de la POO que representa únicamente las características esenciales de un objeto.

---

## Clase

Plantilla utilizada para crear objetos.

---

## Clase Abstracta

Clase base que no puede instanciarse directamente.

---

## Encapsulamiento

Protección de datos internos mediante atributos privados.

---

## Excepción

Error producido durante la ejecución del programa.

---

## Herencia

Mecanismo que permite reutilizar atributos y métodos entre clases.

---

## Instancia

Objeto creado a partir de una clase.

---

## Método

Función definida dentro de una clase.

---

## Modularidad

Organización del sistema en módulos independientes.

---

## Objeto

Entidad creada a partir de una clase.

---

## Polimorfismo

Capacidad de múltiples clases de responder diferente al mismo método.

---

## POO

Paradigma basado en clases y objetos.

---

## Reserva

Proceso mediante el cual un cliente solicita un servicio.

---

## Robustez

Capacidad del sistema para seguir funcionando ante errores.

---

## Servicio

Funcionalidad ofrecida por la empresa.

---

## Tkinter

Librería gráfica utilizada para construir interfaces visuales.

---

## Treeview

Componente utilizado para mostrar tablas en Tkinter.

---

## Validación

Proceso de verificación de datos.

---

# Conclusiones

* Se desarrolló un sistema orientado a objetos completamente funcional.
* Se implementaron correctamente los principios fundamentales de POO.
* El sistema demuestra estabilidad y robustez mediante manejo avanzado de excepciones.
* Se logró una arquitectura modular y extensible.
* El uso de listas internas permitió gestionar información sin bases de datos.
* El sistema registra eventos y errores mediante logs.
* La interfaz gráfica facilita la interacción del usuario.

---

# Autor
Elkin Neira
Proyecto académico desarrollado para la Programación Orientada a Objetos.

