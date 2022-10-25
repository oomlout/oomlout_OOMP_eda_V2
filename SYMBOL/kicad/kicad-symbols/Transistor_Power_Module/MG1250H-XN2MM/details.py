
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_Power_Module"
    oIndex = "MG1250H-XN2MM"
    hexID = "SZKTRANSISTORPOWERMOMG125HXN2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'FS75R07N2E4', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MG1250H-XN2MM', 'kicadSymbolFootprint': 'Transistor_Power_Module:Littelfuse_Package_H_XN2MM', 'kicadSymbolDatasheet': 'https://www.littelfuse.com/~/media/electronics/datasheets/power_semiconductors/littelfuse_power_semiconductor_igbt_module_mg1250h_xn2mm_datasheet.pdf.pdf', 'kicadSymbolki_keywords': 'IGBT Power Module Trench Field Stop Technology', 'kicadSymbolki_description': '50A, 1200V, 260W x 6 , 3-phase, Freewheeling Diode, 5k NTC, Package-H (XN2MM)', 'kicadSymbolki_fp_filters': 'Littelfuse*Package*H*XN2MM*'}])
    newPart['name'].append('Transistor_Power_Module : MG1250H-XN2MM')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

