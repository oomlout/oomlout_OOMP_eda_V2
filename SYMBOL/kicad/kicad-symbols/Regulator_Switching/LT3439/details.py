
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LT3439"
    hexID = "SZKREGULATORSWITCHINGLT3439"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LT3439', 'kicadSymbolFootprint': 'Package_SO:TSSOP-16-1EP_4.4x5mm_P0.65mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/3439fs.pdf', 'kicadSymbolki_keywords': 'Isolated DC/DC Transformer Driver', 'kicadSymbolki_description': '1A Slew Rate Controlled Ultralow Noise Isolated DC/DC Transformer Driver, TSSOP-16', 'kicadSymbolki_fp_filters': 'TSSOP*EP*4.4x5mm*P0.65mm*'}])
    newPart['name'].append('Regulator_Switching : LT3439')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

