
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "ADuM7641C"
    hexID = "SZKISOLATORADUM7641C"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADuM7641C', 'kicadSymbolFootprint': 'Package_SO:QSOP-20_3.9x8.7mm_P0.635mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/ADuM7640_7641_7642_7643.pdf', 'kicadSymbolki_keywords': '6-Channels Hex Digital Isolator 25Mbps', 'kicadSymbolki_description': 'Low Power Six-Channel 5/1 Digital Isolator, 25Mbps 6ns, Fail-Safe High, QSOP-20', 'kicadSymbolki_fp_filters': 'QSOP*3.9x8.7mm*P0.635mm*'}])
    newPart['name'].append('ADuM7641C')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

