import os
from util.data_manipulation import excell_data

excell_file_path = "../files"  + os.sep
excell_file_name = "SHAMPOO COLAGENO.xlsx"
excell_sheet_name = 'SH. COLAGENO'

def table_list(excell_file_path, excell_file_name, excell_sheet_name):
    """Crea una lista anidada que se utilizara para imprimir luego con Reportlab Table

    Argumentos:
    excell_file_path --- Diccionario de datos a partir con la estructura de 
                         COLUMN_NAMES descrita en constants.py
    """
    table_data = [['Descripcion', 'Especificación', 'Resultado']]

    coas_data = excell_data(excell_file_path, excell_file_name, excell_sheet_name)

    for coa_data in coas_data:
        table_data = [['Descripcion', 'Especificación'          , 'Resultado'],
                      ['Apecto'     , 'coa_data[appearance]'    , 'Cumple'   ]
                      ['']]


