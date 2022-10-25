
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Filter"
    oIndex = "LTC1562xG-2"
    hexID = "SZKFILLTC1562XG2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LTC1562xxG', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC1562xG-2', 'kicadSymbolFootprint': 'Package_SO:SSOP-20_5.3x7.2mm_P0.65mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/15622fa.pdf', 'kicadSymbolki_keywords': 'filter opamp quad', 'kicadSymbolki_description': 'Active RC Quad Universal Filter, 20kHz to 300kHz, Low Noise, Low Distortion, SSOP-20', 'kicadSymbolki_fp_filters': 'SSOP*5.3x7.2mm*P0.65mm*'}])
    newPart['name'].append('Filter : LTC1562xG-2')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

