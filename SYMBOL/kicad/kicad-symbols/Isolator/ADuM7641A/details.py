
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "ADuM7641A"
    hexID = "SZKISOLATORADUM7641A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ADuM7641C', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADuM7641A', 'kicadSymbolFootprint': 'Package_SO:QSOP-20_3.9x8.7mm_P0.635mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/ADuM7640_7641_7642_7643.pdf', 'kicadSymbolki_keywords': '6-Channels Hex Digital Isolator 1Mbps', 'kicadSymbolki_description': 'Low Power Six-Channel 5/1 Digital Isolator, 1Mbps 25ns, Fail-Safe High, QSOP-20', 'kicadSymbolki_fp_filters': 'QSOP*3.9x8.7mm*P0.635mm*'}])
    newPart['name'].append('Isolator : ADuM7641A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

