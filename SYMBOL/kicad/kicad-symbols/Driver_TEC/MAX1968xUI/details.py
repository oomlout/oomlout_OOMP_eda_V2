
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_TEC"
    oIndex = "MAX1968xUI"
    hexID = "SZKDRIVERTECMAX1968XUI"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX1968xUI', 'kicadSymbolFootprint': 'Package_SO:HTSSOP-28-1EP_4.4x9.7mm_P0.65mm_EP2.85x5.4mm', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/MAX1968-MAX1969.pdf', 'kicadSymbolki_keywords': 'thermoelectric cooler', 'kicadSymbolki_description': 'Power Driver for Peltier TEC Modules, +-3A, HTSSOP-28', 'kicadSymbolki_fp_filters': 'HTSSOP*4.4x9.7mm*P0.65mm*'}])
    newPart['name'].append('MAX1968xUI')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

