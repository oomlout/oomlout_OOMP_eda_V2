
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "ISL8117FRZ"
    hexID = "SZKREGULATORSWITCHINGISL8117FRZ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ISL8117FRZ', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-16-1EP_4x4mm_P0.5mm_EP2.45x2.45mm', 'kicadSymbolDatasheet': 'https://www.intersil.com/content/dam/Intersil/documents/isl8/isl8117.pdf', 'kicadSymbolki_keywords': 'PWM step down buck converter controller synchronous POL', 'kicadSymbolki_description': 'Synchronous step-down PWM controller, 4.5v to 60v input, 0.6v to 54v Output Voltage, QFN-16', 'kicadSymbolki_fp_filters': 'QFN*1EP*4x4mm*P0.5mm*'}])
    newPart['name'].append('Regulator_Switching : ISL8117FRZ')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

