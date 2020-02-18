import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime,date
import time
import openpyxl

def guardarDato(numero):
    excelDoc = openpyxl.load_workbook('prueba.xlsx')
    hoja = excelDoc.get_sheet_by_name('Hoja1')
    hoja.append([numero,datetime.now()])
    excelDoc.save('prueba.xlsx')


def verificar_precio():
    URL = 'https://www.invertironline.com/titulo/cotizacion/BCBA/AY24/BONOS-NACION-ARGENTINA-USD-8.75--2024/'

    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'}

    page = requests.get(URL, headers=headers)
    soup = bs(page.content, 'html.parser')
    precio = soup.find(id='IdTitulo').get_text()
    precio_nuevo = precio[3:11]
    aca = precio_nuevo.replace(".", '')     #realiza el primer cambio de un punto por un vacio
    final = float(aca.replace(",", '.'))    #realiza el ultimo cambio de una coma por un punto para poder castearlo a un float
    print(final)
    guardarDato(final)
    time.sleep(2)


while True:
    verificar_precio()
