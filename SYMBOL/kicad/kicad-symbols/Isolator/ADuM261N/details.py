
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "ADuM261N"
    hexID = "SZKISOLATORADUM261N"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADuM261N', 'kicadSymbolFootprint': 'Package_SO:SOIC-16W_7.5x12.8mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.analog.com/media/en/technical-documentation/data-sheets/ADuM260N-261N-262N-263N.pdf', 'kicadSymbolki_keywords': 'digital isolator galvanic isopower', 'kicadSymbolki_description': '5.0 kV RMS, 6-Channel Digital Isolator, 1 reverse channels, SOIC-16', 'kicadSymbolki_fp_filters': 'SOIC*7.5x12.8mm*P1.27mm*'}])
    newPart['name'].append('ADuM261N')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

