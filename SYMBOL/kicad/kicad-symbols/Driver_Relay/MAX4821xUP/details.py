
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_Relay"
    oIndex = "MAX4821xUP"
    hexID = "SZKDRIVERRELAYMAX4821XUP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX4821xUP', 'kicadSymbolFootprint': 'Package_SO:HTSSOP-20-1EP_4.4x6.5mm_P0.65mm_EP2.85x4mm', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/MAX4820-MAX4821.pdf', 'kicadSymbolki_keywords': 'Relay Driver', 'kicadSymbolki_description': '8-Channel Parallel Interface Low-Side Driver, TSSOP-20', 'kicadSymbolki_fp_filters': '*TSSOP*4.4x6.5mm*P0.65mm*'}])
    newPart['name'].append('Driver_Relay : MAX4821xUP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

