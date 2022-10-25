
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "74xx"
    oIndex = "74HCT244"
    hexID = "SZK74XX74HCT244"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '74HC244', 'kicadSymbolReference': 'U', 'kicadSymbolValue': '74HCT244', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://assets.nexperia.com/documents/data-sheet/74HC_HCT244.pdf', 'kicadSymbolki_keywords': 'HCTMOS BUFFER 3State', 'kicadSymbolki_description': '8-bit Buffer/Line Driver 3-state', 'kicadSymbolki_fp_filters': 'TSSOP*4.4x6.5mm*P0.65mm* SSOP*4.4x6.5mm*P0.65mm*'}])
    newPart['name'].append('74xx : 74HCT244')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

