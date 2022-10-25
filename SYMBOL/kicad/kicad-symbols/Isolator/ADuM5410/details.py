
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "ADuM5410"
    hexID = "SZKISOLATORADUM541"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADuM5410', 'kicadSymbolFootprint': 'Package_SO:SSOP-24_5.3x8.2mm_P0.65mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/ADuM5410-5411-5412.pdf', 'kicadSymbolki_keywords': 'digital isolator galvanic isopower', 'kicadSymbolki_description': 'Quad-Channel 2.5kV isolator with integrated dc-dc converter, 4 Input / 0 output, SSOP-24', 'kicadSymbolki_fp_filters': 'SSOP*5.3x8.2mm*P0.65mm*'}])
    newPart['name'].append('Isolator : ADuM5410')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

