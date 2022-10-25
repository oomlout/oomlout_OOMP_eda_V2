
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_FET"
    oIndex = "IR2214S"
    hexID = "SZKDRIVERFETIR2214S"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IR2114S', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'IR2214S', 'kicadSymbolFootprint': 'Package_SO:SSOP-24_5.3x8.2mm_P0.65mm', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/ir2114ss.pdf?fileId=5546d462533600a4015355c836cd168a', 'kicadSymbolki_keywords': 'Gate Driver', 'kicadSymbolki_description': 'Half-Bridge Gate Driver IC, 1200V, 1.0/1.5A, SSOP-24', 'kicadSymbolki_fp_filters': 'SSOP*5.3x8.2mm*P0.65mm*'}])
    newPart['name'].append('Driver_FET : IR2214S')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

