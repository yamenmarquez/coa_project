import os
import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.colors import pink, black, red, blue, green
from reportlab.lib.units import inch, cm
from pdfrw import PdfReader
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl

# Una vez obtenido los valores se imprimen el el pdf con el siguiente código
def coa_generation(data = {}, saved_coa_path = ".coas_por_enviar" + os.sep):
    created_pdf_name = saved_coa_path + referencia + lote + '.pdf'
    c = canvas.Canvas(created_pdf_name)
    template = PdfReader(files_path + pdf_template_file_name, decompress=False).pages
    t = pagexobj(template[0])
    c.doForm(makerl(c, t))
    c.setFillColor(blue)
    c.drawString(1.8*inch, 8.92*inch, cliente)
    c.drawString(2.42*inch, 8.72*inch, 'COA-No-'+coa_number)
    c.drawString(2.06*inch, 8.51*inch, referencia)
    c.drawString(1.60*inch, 8.32*inch, lote)
    c.drawString(2.84*inch, 8.12*inch, fecha_elab)
    c.drawString(2.75*inch, 7.92*inch, fecha_exp)
    c.drawString(2.50*inch, 7.71*inch, str(cant_cajas))
    c.drawString(2.60*inch, 7.52*inch, und_caja)
    c.drawString(2.58*inch, 7.31*inch, str(total_und))
    c.drawString(6.23*inch, 6.61*inch, aspecto)
    c.drawString(6.23*inch, 6.25*inch, color)
    c.drawString(6.23*inch, 6.06*inch, olor)
    c.drawString(6.23*inch, 5.83*inch, str(pH))
    c.drawString(6.23*inch, 5.63*inch, str(viscosidad))
    c.drawString(6.23*inch, 5.41*inch, str(peso_neto))
    c.drawString(6.23*inch, 5.20*inch, sp_fases)
    c.drawString(6.23*inch, 4.90*inch, atr_calidad)
    c.drawString(1.72*inch, 1.52*inch, fecha_edicion)
    c.drawString(4.85*inch, 1.52*inch, fecha_edicion)


    c.showPage()
    c.save()