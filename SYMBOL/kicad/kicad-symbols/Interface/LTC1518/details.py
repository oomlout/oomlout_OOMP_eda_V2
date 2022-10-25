
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface"
    oIndex = "LTC1518"
    hexID = "SZKINTERFACELTC1518"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC1518', 'kicadSymbolFootprint': 'Package_SO:SOIC-16_3.9x9.9mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/15189fa.pdf', 'kicadSymbolki_keywords': 'receiver rs485 rs422 differential', 'kicadSymbolki_description': '52Mbps Precision Delay RS485 Quad Line Receivers', 'kicadSymbolki_fp_filters': 'SOIC*16*3.9x9.9mm*P1.27mm*'}])
    newPart['name'].append('Interface : LTC1518')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

