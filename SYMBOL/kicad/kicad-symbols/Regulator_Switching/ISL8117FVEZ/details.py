
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "ISL8117FVEZ"
    hexID = "SZKREGULATORSWITCHINGISL8117FVEZ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ISL8117FVEZ', 'kicadSymbolFootprint': 'Package_SO:HTSSOP-16-1EP_4.4x5mm_P0.65mm_EP3.4x5mm', 'kicadSymbolDatasheet': 'https://www.intersil.com/content/dam/Intersil/documents/isl8/isl8117.pdf', 'kicadSymbolki_keywords': 'PWM step down buck converter controller synchronous POL', 'kicadSymbolki_description': 'Synchronous step-down PWM controller, 4.5v to 60v input, 0.6v to 54v Output Voltage, HTSSOP-16', 'kicadSymbolki_fp_filters': 'HTSSOP*EP*4.4x5mm*P0.65mm*'}])
    newPart['name'].append('Regulator_Switching : ISL8117FVEZ')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

