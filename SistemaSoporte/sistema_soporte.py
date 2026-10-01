# ============================================================
# ACT. EVALUATIVA 3
# Nombre: Deibis Olivero Santos
# Sistema dinamico de gestion de soporte tecnico
# ============================================================


# ============================================================
# CLASE SOLICITUD
# ============================================================

class Solicitud:
    def __init__(self, codigo, usuario, problema, prioridad):
        self.codigo = codigo
        self.usuario = usuario
        self.problema = problema
        self.prioridad = prioridad
        self.estado = "PENDIENTE"
        self.tecnico = "No asignado"

    def mostrar_informacion(self):
        print("----------------------------------------")
        print(f"Código: {self.codigo}")
        print(f"Usuario: {self.usuario}")
        print(f"Problema: {self.problema}")
        print(f"Prioridad: {self.prioridad}")
        print(f"Estado: {self.estado}")
        print(f"Técnico: {self.tecnico}")
        print("----------------------------------------")


# ============================================================
# CLASE NODO
# ============================================================

class Nodo:
    def __init__(self, solicitud):
        self.solicitud = solicitud
        self.siguiente = None


# ============================================================
# LISTA ENLAZADA
# Se utiliza para almacenar las solicitudes pendientes.
# ============================================================

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def esta_vacia(self):
        return self.cabeza is None

    def insertar_final(self, solicitud):
        nuevo_nodo = Nodo(solicitud)

        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return

        actual = self.cabeza

        while actual.siguiente is not None:
            actual = actual.siguiente

        actual.siguiente = nuevo_nodo

    def buscar(self, codigo):
        actual = self.cabeza

        while actual is not None:
            if actual.solicitud.codigo == codigo:
                return actual.solicitud

            actual = actual.siguiente

        return None

    def eliminar(self, codigo):
        if self.cabeza is None:
            return None

        # Si el nodo que se quiere eliminar es el primero
        if self.cabeza.solicitud.codigo == codigo:
            solicitud = self.cabeza.solicitud
            self.cabeza = self.cabeza.siguiente
            return solicitud

        anterior = self.cabeza
        actual = self.cabeza.siguiente

        while actual is not None:

            if actual.solicitud.codigo == codigo:
                solicitud = actual.solicitud

                # Se modifica la referencia
                # para saltar el nodo eliminado.
                anterior.siguiente = actual.siguiente

                return solicitud

            anterior = actual
            actual = actual.siguiente

        return None

    def mostrar(self):
        if self.esta_vacia():
            print("\nNo hay solicitudes pendientes.")
            return

        print("\n========================================")
        print("       SOLICITUDES PENDIENTES")
        print("========================================")

        actual = self.cabeza

        while actual is not None:
            solicitud = actual.solicitud

            print(f"\nCódigo: {solicitud.codigo}")
            print(f"Usuario: {solicitud.usuario}")
            print(f"Problema: {solicitud.problema}")
            print(f"Prioridad: {solicitud.prioridad}")
            print(f"Estado: {solicitud.estado}")

            actual = actual.siguiente

        print("========================================")


# ============================================================
# COLA
# Principio FIFO:
# First In - First Out
# ============================================================

class Cola:
    def __init__(self):
        self.frente_nodo = None
        self.final_nodo = None

    def esta_vacia(self):
        return self.frente_nodo is None

    def encolar(self, solicitud):
        nuevo_nodo = Nodo(solicitud)

        if self.esta_vacia():
            self.frente_nodo = nuevo_nodo
            self.final_nodo = nuevo_nodo
        else:
            self.final_nodo.siguiente = nuevo_nodo
            self.final_nodo = nuevo_nodo

    def desencolar(self):
        if self.esta_vacia():
            return None

        solicitud = self.frente_nodo.solicitud

        self.frente_nodo = self.frente_nodo.siguiente

        if self.frente_nodo is None:
            self.final_nodo = None

        return solicitud

    def frente(self):
        if self.esta_vacia():
            return None

        return self.frente_nodo.solicitud

    def mostrar(self):
        if self.esta_vacia():
            print("\nLa cola está vacía.")
            return

        print("\n========================================")
        print("             COLA DE ATENCIÓN")
        print("========================================")

        actual = self.frente_nodo

        while actual is not None:
            solicitud = actual.solicitud

            print(f"Código: {solicitud.codigo}")
            print(f"Usuario: {solicitud.usuario}")
            print(f"Prioridad: {solicitud.prioridad}")
            print("----------------------------------------")

            actual = actual.siguiente


# ============================================================
# PILA
# Principio LIFO:
# Last In - First Out
# ============================================================

class Pila:
    def __init__(self):
        self.tope_nodo = None

    def esta_vacia(self):
        return self.tope_nodo is None

    def apilar(self, solicitud):
        nuevo_nodo = Nodo(solicitud)

        nuevo_nodo.siguiente = self.tope_nodo
        self.tope_nodo = nuevo_nodo

    def desapilar(self):
        if self.esta_vacia():
            return None

        solicitud = self.tope_nodo.solicitud

        self.tope_nodo = self.tope_nodo.siguiente

        return solicitud

    def tope(self):
        if self.esta_vacia():
            return None

        return self.tope_nodo.solicitud

    def mostrar(self):
        if self.esta_vacia():
            print("\nNo hay solicitudes atendidas.")
            return

        print("\n========================================")
        print("       HISTORIAL DE ATENCIONES")
        print("========================================")

        actual = self.tope_nodo
        contador = 1

        while actual is not None:
            solicitud = actual.solicitud

            print(
                f"{contador}. Solicitud {solicitud.codigo} "
                f"- Usuario: {solicitud.usuario} "
                f"- Técnico: {solicitud.tecnico}"
            )

            actual = actual.siguiente
            contador += 1

        print("========================================")


# ============================================================
# CLASE PRINCIPAL DEL SISTEMA
# ============================================================

class SistemaSoporte:

    def __init__(self):

        # Lista enlazada para solicitudes pendientes
        self.pendientes = ListaEnlazada()

        # Cola para solicitudes que serán atendidas
        self.cola = Cola()

        # Pila para historial de solicitudes atendidas
        self.historial = Pila()

        # Contadores de estadísticas
        self.total_registradas = 0
        self.total_atendidas = 0
        self.total_canceladas = 0

    # ========================================================
    # COMPROBAR SI EXISTE UN CÓDIGO
    # ========================================================

    def buscar_solicitud(self, codigo):

        # Buscar primero en pendientes
        solicitud = self.pendientes.buscar(codigo)

        if solicitud is not None:
            return solicitud

        # Buscar en la cola
        actual = self.cola.frente_nodo

        while actual is not None:

            if actual.solicitud.codigo == codigo:
                return actual.solicitud

            actual = actual.siguiente

        # Buscar en historial
        actual = self.historial.tope_nodo

        while actual is not None:

            if actual.solicitud.codigo == codigo:
                return actual.solicitud

            actual = actual.siguiente

        return None

    # ========================================================
    # REGISTRAR SOLICITUD
    # ========================================================

    def registrar_solicitud(self):

        print("\n========================================")
        print("          REGISTRAR SOLICITUD")
        print("========================================")

        codigo = input("Ingrese el código de la solicitud: ").strip()

        if codigo == "":
            print("El código no puede estar vacío.")
            return

        # Comprobar que el código sea único
        if self.buscar_solicitud(codigo) is not None:
            print("Error: el código de solicitud ya existe.")
            return

        usuario = input("Ingrese el nombre del usuario: ").strip()

        if usuario == "":
            print("El usuario no puede estar vacío.")
            return

        problema = input("Ingrese la descripción del problema: ").strip()

        if problema == "":
            print("La descripción del problema no puede estar vacía.")
            return

        print("\nSeleccione la prioridad:")
        print("1. Alta")
        print("2. Media")
        print("3. Baja")

        opcion_prioridad = input("Seleccione una opción: ").strip()

        if opcion_prioridad == "1":
            prioridad = "ALTA"
        elif opcion_prioridad == "2":
            prioridad = "MEDIA"
        elif opcion_prioridad == "3":
            prioridad = "BAJA"
        else:
            print("Prioridad no válida.")
            return

        solicitud = Solicitud(
            codigo,
            usuario,
            problema,
            prioridad
        )

        # Se agrega a la lista enlazada de pendientes
        self.pendientes.insertar_final(solicitud)

        # También se agrega a la cola de atención
        self.cola.encolar(solicitud)

        self.total_registradas += 1

        print("\nSolicitud registrada correctamente.")
        print(f"Código: {codigo}")
        print(f"Prioridad: {prioridad}")

    # ========================================================
    # MOSTRAR SOLICITUDES PENDIENTES
    # ========================================================

    def mostrar_pendientes(self):
        self.pendientes.mostrar()

    # ========================================================
    # BUSCAR SOLICITUD
    # ========================================================

    def buscar(self):

        print("\n========================================")
        print("           BUSCAR SOLICITUD")
        print("========================================")

        codigo = input("Ingrese el código de la solicitud: ").strip()

        solicitud = self.buscar_solicitud(codigo)

        if solicitud is None:
            print("\nSolicitud no encontrada.")
        else:
            print("\nSolicitud encontrada:")
            solicitud.mostrar_informacion()

    # ========================================================
    # ATENDER SIGUIENTE SOLICITUD
    # ========================================================

    def atender_siguiente(self):

        print("\n========================================")
        print("        ATENDER SIGUIENTE SOLICITUD")
        print("========================================")

        if self.cola.esta_vacia():
            print("No hay solicitudes para atender.")
            return

        # Se retira de la cola siguiendo FIFO
        solicitud = self.cola.desencolar()

        print("\nAtendiendo solicitud...")
        print(f"Código: {solicitud.codigo}")
        print(f"Usuario: {solicitud.usuario}")
        print(f"Problema: {solicitud.problema}")
        print(f"Prioridad: {solicitud.prioridad}")

        tecnico = input("Ingrese el nombre del técnico: ").strip()

        if tecnico == "":
            tecnico = "Técnico no especificado"

        # Actualizar información
        solicitud.estado = "ATENDIDA"
        solicitud.tecnico = tecnico

        # Eliminar de la lista de pendientes
        self.pendientes.eliminar(solicitud.codigo)

        # Guardar en el historial utilizando la pila
        self.historial.apilar(solicitud)

        self.total_atendidas += 1

        print("\nSolicitud atendida correctamente.")
        print(f"Técnico: {tecnico}")

    # ========================================================
    # CANCELAR SOLICITUD
    # ========================================================

    def cancelar_solicitud(self):

        print("\n========================================")
        print("          CANCELAR SOLICITUD")
        print("========================================")

        codigo = input(
            "Ingrese el código de la solicitud pendiente: "
        ).strip()

        solicitud = self.pendientes.buscar(codigo)

        if solicitud is None:
            print("\nSolicitud pendiente no encontrada.")
            return

        print("\nSolicitud encontrada:")
        solicitud.mostrar_informacion()

        confirmacion = input(
            "¿Desea cancelarla? S/N: "
        ).strip().upper()

        if confirmacion == "S":

            # Eliminar modificando referencias entre nodos
            eliminada = self.pendientes.eliminar(codigo)

            if eliminada is not None:

                solicitud.estado = "CANCELADA"

                # También se elimina de la cola
                self.eliminar_de_cola(codigo)

                self.total_canceladas += 1

                print("\nSolicitud cancelada correctamente.")
                print(f"La solicitud {codigo} fue cancelada.")

        elif confirmacion == "N":

            print("\nLa solicitud no fue cancelada.")

        else:

            print("\nOpción no válida.")

    # ========================================================
    # ELIMINAR SOLICITUD DE LA COLA
    # ========================================================

    def eliminar_de_cola(self, codigo):

        if self.cola.esta_vacia():
            return

        anterior = None
        actual = self.cola.frente_nodo

        while actual is not None:

            if actual.solicitud.codigo == codigo:

                if anterior is None:
                    self.cola.frente_nodo = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente

                if actual == self.cola.final_nodo:
                    self.cola.final_nodo = anterior

                return

            anterior = actual
            actual = actual.siguiente

    # ========================================================
    # MOSTRAR HISTORIAL
    # ========================================================

    def mostrar_historial(self):
        self.historial.mostrar()

    # ========================================================
    # DESHACER ÚLTIMA ATENCIÓN
    # ========================================================

    def deshacer_ultima_atencion(self):

        print("\n========================================")
        print("         DESHACER ÚLTIMA ATENCIÓN")
        print("========================================")

        if self.historial.esta_vacia():
            print("No hay atenciones para deshacer.")
            return

        ultima = self.historial.tope()

        print("\nÚltima atención:")
        ultima.mostrar_informacion()

        confirmacion = input(
            "¿Desea deshacer esta atención? S/N: "
        ).strip().upper()

        if confirmacion == "S":

            # Se recupera mediante desapilar()
            solicitud = self.historial.desapilar()

            # Cambiar nuevamente su estado
            solicitud.estado = "PENDIENTE"
            solicitud.tecnico = "No asignado"

            # Regresarla a la lista de pendientes
            self.pendientes.insertar_final(solicitud)

            # Regresarla a la cola
            self.cola.encolar(solicitud)

            self.total_atendidas -= 1

            print("\nLa atención fue deshecha.")
            print(
                f"La solicitud {solicitud.codigo} "
                "regresó a pendientes."
            )

        elif confirmacion == "N":

            print("\nLa atención no fue deshecha.")

        else:

            print("\nOpción no válida.")

    # ========================================================
    # ESTADÍSTICAS
    # ========================================================

    def mostrar_estadisticas(self):

        print("\n++++++++++++++++++++++++++++++++++++++++")
        print("              ESTADÍSTICAS")
        print("++++++++++++++++++++++++++++++++++++++++")

        pendientes = 0
        atendidas = 0
        canceladas = 0

        prioridad_alta = 0
        prioridad_media = 0
        prioridad_baja = 0

        # Recorrer la lista de pendientes
        actual = self.pendientes.cabeza

        while actual is not None:

            solicitud = actual.solicitud

            pendientes += 1

            if solicitud.prioridad == "ALTA":
                prioridad_alta += 1
            elif solicitud.prioridad == "MEDIA":
                prioridad_media += 1
            elif solicitud.prioridad == "BAJA":
                prioridad_baja += 1

            actual = actual.siguiente

        # Recorrer el historial
        actual = self.historial.tope_nodo

        while actual is not None:

            solicitud = actual.solicitud

            atendidas += 1

            if solicitud.prioridad == "ALTA":
                prioridad_alta += 1
            elif solicitud.prioridad == "MEDIA":
                prioridad_media += 1
            elif solicitud.prioridad == "BAJA":
                prioridad_baja += 1

            actual = actual.siguiente

        # Las solicitudes canceladas ya no están en pendientes
        # ni en historial, por eso se obtiene el contador.
        canceladas = self.total_canceladas

        print(f"Total registradas: {self.total_registradas}")
        print(f"Pendientes: {pendientes}")
        print(f"Atendidas: {atendidas}")
        print(f"Canceladas: {canceladas}")
        print(f"Prioridad alta: {prioridad_alta}")
        print(f"Prioridad media: {prioridad_media}")
        print(f"Prioridad baja: {prioridad_baja}")

        print("++++++++++++++++++++++++++++++++++++++++")

    # ========================================================
    # MENÚ PRINCIPAL
    # ========================================================

    def ejecutar(self):

        while True:

            print("\n")
            print("========================================")
            print("       CENTRO DE SOPORTE TÉCNICO")
            print("========================================")
            print("1. Registrar solicitud")
            print("2. Mostrar solicitudes pendientes")
            print("3. Buscar solicitud")
            print("4. Atender siguiente solicitud")
            print("5. Cancelar solicitud")
            print("6. Mostrar historial de atenciones")
            print("7. Deshacer última atención")
            print("8. Mostrar estadísticas")
            print("9. Salir")
            print("========================================")

            opcion = input("Seleccione una opción: ").strip()

            if opcion == "1":

                self.registrar_solicitud()

            elif opcion == "2":

                self.mostrar_pendientes()

            elif opcion == "3":

                self.buscar()

            elif opcion == "4":

                self.atender_siguiente()

            elif opcion == "5":

                self.cancelar_solicitud()

            elif opcion == "6":

                self.mostrar_historial()

            elif opcion == "7":

                self.deshacer_ultima_atencion()

            elif opcion == "8":

                self.mostrar_estadisticas()

            elif opcion == "9":

                print("\n========================================")
                print("Gracias por utilizar el sistema.")
                print("Programa finalizado.")
                print("========================================")

                break

            else:

                print("\nOpción no válida.")
                print("Seleccione una opción del 1 al 9.")


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

if __name__ == "__main__":

    sistema = SistemaSoporte()

    sistema.ejecutar()