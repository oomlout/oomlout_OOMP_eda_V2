
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Controller"
    oIndex = "IR1168S"
    hexID = "SZKREGULATORCONTROLLERIR1168S"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'IR1168S', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/ir1168.pdf?fileId=5546d462533600a4015355c467fa1658', 'kicadSymbolki_keywords': 'dual synchronous rectifier controller', 'kicadSymbolki_description': 'Dual Smart Rectifier Driver IC, 500kHz, 200V, 1.0/4.0A, SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Regulator_Controller : IR1168S')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

