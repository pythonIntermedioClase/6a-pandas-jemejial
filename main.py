"""
main.py
Flujo ETL: carga, inspección, clasificación y exportación de declaraciones IVA.
Sesión 6: Pandas I — Python Intermedio para Análisis de Datos · DIAN 2026
"""

# =============================================================================
# IMPORTS
# Todos los imports van aquí, al inicio del archivo, antes de cualquier otra
# línea de código. Nunca dentro de funciones ni distribuidos a lo largo del
# código. A medida que implementas cada módulo, descomenta el import
# correspondiente.
import numpy as np
import pandas as pd
from datetime import date

# Sección 3:
# from src.data_loader import cargar_declaraciones
#
# Sección 4 — agrega las dos funciones nuevas al import de data_loader:
# from src.data_loader import cargar_declaraciones, inspeccionar_datos, validar_nulos
#
# Sección 5:
# from src.data_transformer import clasificar_por_valor, agregar_identificador_periodo, preparar_columnas_salida
#
# Sección 6:
# from src.data_exporter import exportar_csv, exportar_excel_por_categoria
# =============================================================================


# =============================================================================
# CONFIGURACIÓN
# =============================================================================

RUTA_DATOS = "data/inputs/declaraciones_iva_2025.csv"
CARPETA_RESULTADOS = "data/outputs"
COLUMNAS_CRITICAS = ["nit", "valor_declarado", "estado"]
COLUMNAS_SALIDA = [
    "identificador_periodo",
    "nit",
    "razon_social",
    "municipio",
    "periodo",
    "valor_declarado",
    "nivel_riesgo",
    "estado",
]


# =============================================================================
# MENÚ
# Esta función ya está implementada. Ejecútala, lee el código y úsala como
# referencia para entender el ciclo del programa.
# =============================================================================

def mostrar_menu():
    """Muestra el menú principal y retorna la opción elegida por el usuario."""
    print("\n" + "=" * 45)
    print("  Pipeline — Declaraciones IVA 2025")
    print("=" * 45)
    print("  1. Cargar datos")
    print("  2. Inspeccionar datos")
    print("  3. Transformar datos")
    print("  4. Exportar resultados")
    print("  5. Ejecutar pipeline completo")
    print("  0. Salir")
    print("=" * 45)
    return input("  Opción: ").strip()


# =============================================================================
# PIPELINE
# __main__ solo llama a main(). La lógica vive en funciones, no a nivel de
# módulo: así puedes importar main.py desde otros scripts sin efectos.
# =============================================================================

def main():
    """Ejecuta el pipeline interactivo de declaraciones IVA."""

    # df y df_salida se declaran aquí para que todas las opciones del menú
    # puedan leerlas y modificarlas. Arrancan en None hasta que se ejecute
    # la carga.
    df = None
    df_salida = None

    opcion = mostrar_menu()

    while opcion != "0":

        # -----------------------------------------------------------------
        # OPCIÓN 1: CARGA
        # El import ya está en el bloque de arriba, solo descoméntalo.
        # Completa los espacios marcados con ___ y ejecuta.
        # -----------------------------------------------------------------
        if opcion == "1":
            # df = cargar_declaraciones(___)
            # print(f"Filas cargadas: {___}")
            pass

        # -----------------------------------------------------------------
        # OPCIÓN 2: INSPECCIÓN
        # Tienes los nombres de las funciones. Escribe las llamadas completas.
        # Antes de llamar a inspeccionar_datos(), verifica que df no sea None;
        # si lo es, muestra un mensaje y vuelve al menú.
        # Funciones disponibles: inspeccionar_datos(), validar_nulos()
        # -----------------------------------------------------------------
        elif opcion == "2":
            pass

        # -----------------------------------------------------------------
        # OPCIÓN 3: TRANSFORMACIÓN
        # - Clasificar cada registro en nivel de riesgo (Alto / Medio / Bajo)
        #   con umbral_alto=10_000_000 y umbral_medio=5_000_000.
        # - Agregar la columna identificador_periodo.
        # - Guardar en df_salida solo las columnas de COLUMNAS_SALIDA.
        # Verifica que df no sea None antes de transformar.
        # -----------------------------------------------------------------
        elif opcion == "3":
            pass

        # -----------------------------------------------------------------
        # OPCIÓN 4: EXPORTACIÓN
        # Genera un CSV y un Excel en data/outputs/.
        # -----------------------------------------------------------------
        elif opcion == "4":
            pass

        # -----------------------------------------------------------------
        # OPCIÓN 5: PIPELINE COMPLETO
        # Ejecuta las cuatro etapas anteriores en secuencia.
        # -----------------------------------------------------------------
        elif opcion == "5":
            pass

        else:
            print("  Opción no válida. Intenta de nuevo.")

        opcion = mostrar_menu()

    print("  Hasta luego.")


# =============================================================================
# PUNTO DE ENTRADA
# =============================================================================
def probar_acceso_diccionario():
    declaracion = {"nit": "800234567-0", "estado": "Pendiente"}
    print(declaracion["valor_declarado"])

def revisar_declaracion(declaracion):
    # Recorrer e imprimir todos los campos
    for clave, valor in declaracion.items():
        print(f"{clave}: {valor}")

    declaracion["estado"] = "Revisada"
    print(f"Estado actualizado: {declaracion['estado']}")

def resumen_declaraciones(lista_declaraciones):
    print()
    
def probar_acceso_serie():
    serie = pd.Series([100, 200, 300])
    print(serie[5])

def explorar_dataframe():
    df = pd.DataFrame([
        {
            "nit": "900123456-1",
            "razon_social": "Comercializadora Andina S.A.S",
            "municipio": "Bogotá",
            "valor_declarado": 4500000,
        },
        {
            "nit": "800987654-2",
            "razon_social": "Servicios Integrales S.A.S",
            "municipio": "Medellín",
            "valor_declarado": 3200000,
        },
        {
            "nit": "901234567-3",
            "razon_social": "Distribuciones del Caribe S.A.S",
            "municipio": "Barranquilla",
            "valor_declarado": 5100000,
        },
        {
            "nit": "890123456-4",
            "razon_social": "Inversiones del Pacífico S.A.S",
            "municipio": "Cali",
            "valor_declarado": 2750000,
        },
    ])

    print(df.index)
    print(df.columns)
    print(df.shape)

if __name__ == "__main__":
    # probar_acceso_diccionario()
    # main()  ← comentado mientras probamos
    # probar_acceso_serie()
    """
    declaracion = {
        "Nit": "900123456-1",
        "Razon_social": "Comercializadora Andina S.A.S",
        "Valor_declarado": 4_500_000,
        "Estado": "Presentada",
        "Municipio": "Bogotá",
    }
    #print("Función revisar_declaración ejecutada correctamente")
    #revisar_declaracion(declaracion)

    valores = np.array([4_500_000, 12_300_000, 2_100_000])
    serie = pd.Series(valores, index=["900123456-1", "800234567-0", "700345678-9"])

    print(serie)
    # 900123456-1     4500000
    # 800234567-0    12300000
    # 700345678-9     2100000
    # dtype: int64

    print(serie["800234567-0"])  # → 12300000
    print(serie.mean())          # → 6300000.0
    print(serie.sum())           # → 18900000
    print(serie.max())           # → 12300000
    print(serie.idxmax())        # → '800234567-0'  (index del valor máximo)
    datos = {
    "nit": ["900123456-1", "800234567-0", "700345678-9"],
    "municipio": ["Bogotá", "Cali", "Medellín"],
    "valor_declarado": [4_500_000, 12_300_000, 2_100_000],
    "estado": ["Presentada", "Presentada", "Pendiente"],
}

    df = pd.DataFrame(datos)
    print(df)

    #            nit  municipio  valor_declarado     estado   ← nombres de columna
    # 0  900123456-1     Bogotá          4500000  Presentada  ← fila 0
    # 1  800234567-0       Cali         12300000  Presentada  ← fila 1
    # 2  700345678-9   Medellín          2100000   Pendiente  ← fila 2
    # ↑
    # índice de filas (asignado automáticamente)

    print(type(df["valor_declarado"]))
    # <class 'pandas.core.series.Series'>

    print(df.shape[0])  # → 3  (número de filas)
    print(df.shape[1])  # → 4  (número de columnas)
    print(len(df))      # → 3  (equivalente a df.shape[0])
    """
    explorar_dataframe()

    


