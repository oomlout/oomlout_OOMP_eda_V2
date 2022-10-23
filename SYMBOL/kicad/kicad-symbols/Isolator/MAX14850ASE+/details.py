
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "MAX14850ASE+"
    hexID = "SZKISOLATORMAX1485ASE+"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MAX14850AEE+', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX14850ASE+', 'kicadSymbolFootprint': 'Package_SO:SOIC-16_3.9x9.9mm_P1.27mm', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/MAX14850.pdf', 'kicadSymbolki_keywords': '6 channel digital isolator bidirectional', 'kicadSymbolki_description': 'Six-channel digital isolator, bidirectional, 3V3, 5V, SOIC-16', 'kicadSymbolki_fp_filters': 'SOIC*3.9x9.9mm?P1.27mm*'}])
    newPart['name'].append('MAX14850ASE+')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

