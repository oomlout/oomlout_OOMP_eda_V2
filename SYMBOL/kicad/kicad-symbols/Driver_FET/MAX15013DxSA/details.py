
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_FET"
    oIndex = "MAX15013DxSA"
    hexID = "SZKDRIVERFETMAX1513DXSA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MAX15012DxSA', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX15013DxSA', 'kicadSymbolFootprint': 'Package_SO:SOIC-8-1EP_3.9x4.9mm_P1.27mm_EP2.514x3.2mm', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/MAX15012-MAX15013B.pdf', 'kicadSymbolki_keywords': 'Half Bridge Gate Driver', 'kicadSymbolki_description': 'High Frequency Half Bridge Driver, Output Current 2.0A, 175V, TTL Input, SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*1EP*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Driver_FET : MAX15013DxSA')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

