
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "ATX-24"
    hexID = "SZKCNATX24"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'ATX-24', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.intel.com/content/dam/www/public/us/en/documents/guides/power-supply-design-guide-june.pdf#page=33', 'kicadSymbolki_keywords': 'ATX PSU', 'kicadSymbolki_description': 'ATX Power supply 24pins', 'kicadSymbolki_fp_filters': '*Mini?Fit*2x12*Vertical* *Mini?Fit*2x12*Horizontal*'}])
    newPart['name'].append('ATX-24')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

