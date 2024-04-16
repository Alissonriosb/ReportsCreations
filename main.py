import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Cargar los datos desde un archivo Excel
def cargar_datos(archivo):
    datos = pd.read_excel(archivo)
    return datos

# Ejemplo de uso
datos = cargar_datos('datos.xlsx')
print(datos.head())  # Muestra las primeras filas para verificar
def generar_reporte(datos, archivo_pdf):
    c = canvas.Canvas(archivo_pdf, pagesize=letter)
    width, height = letter  # Tamaño de la página

    c.drawString(100, height - 50, "Reporte de Datos")
    
    # Agregamos algunos datos del DataFrame
    y = height - 100
    for index, row in datos.iterrows():
        c.drawString(100, y, f"{row['Nombre']} - {row['Edad']}")
        y -= 20
        if y < 40:
            y = height - 100
            c.showPage()
    
    c.save()

# Generar el reporte
generar_reporte(datos, 'reporte.pdf')
