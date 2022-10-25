
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_Power_Module"
    oIndex = "MG1225H-XBN2MM"
    hexID = "SZKTRANSISTORPOWERMOMG1225HXBN2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MG1215H-XBN2MM', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MG1225H-XBN2MM', 'kicadSymbolFootprint': 'Transistor_Power_Module:Littelfuse_Package_H_XBN2MM', 'kicadSymbolDatasheet': 'https://www.littelfuse.com/~/media/electronics/datasheets/power_semiconductors/littelfuse_power_semiconductor_igbt_module_mg1225h_xbn2mm_datasheet.pdf.pdf', 'kicadSymbolki_keywords': 'IGBT Power Module Trench Field Stop Technology', 'kicadSymbolki_description': '25A, 1200V, 147W x 6 , 3-phase, Freewheeling Diode, Brake Chopper, Diode Rectifier, 5k NTC, Package-H (XBN2MM)', 'kicadSymbolki_fp_filters': 'Littelfuse*Package*H*XBN2MM*'}])
    newPart['name'].append('Transistor_Power_Module : MG1225H-XBN2MM')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

