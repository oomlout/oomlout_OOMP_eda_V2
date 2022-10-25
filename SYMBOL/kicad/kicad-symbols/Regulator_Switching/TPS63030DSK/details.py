
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "TPS63030DSK"
    hexID = "SZKREGULATORSWITCHINGTPS633DSK"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPS63030DSK', 'kicadSymbolFootprint': 'Package_SON:WSON-10-1EP_2.5x2.5mm_P0.5mm_EP1.2x2mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tps63030.pdf', 'kicadSymbolki_keywords': 'Buck-Boost adjustable converter', 'kicadSymbolki_description': 'Buck-Boost Converter, 1.8-5.5V Input Voltage, 1A Switch Current, Adjustable Output Voltage, VSON-10 (DSK0010A)', 'kicadSymbolki_fp_filters': 'WSON*1EP*2.5x2.5mm*P0.5mm*EP1.2x2mm*'}])
    newPart['name'].append('Regulator_Switching : TPS63030DSK')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

