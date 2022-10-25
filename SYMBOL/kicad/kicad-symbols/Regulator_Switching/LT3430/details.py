
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LT3430"
    hexID = "SZKREGULATORSWITCHINGLT343"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LT3430', 'kicadSymbolFootprint': 'Package_SO:TSSOP-14-1EP_4.4x5mm_P0.65mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/34301fa.pdf', 'kicadSymbolki_keywords': 'Step-Down Switching Regulator', 'kicadSymbolki_description': '3A High Voltage 200kHz Step-Down Switching Regulator, TSSOP-16', 'kicadSymbolki_fp_filters': 'TSSOP*EP*4.4x5mm*P0.65mm*'}])
    newPart['name'].append('Regulator_Switching : LT3430')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

