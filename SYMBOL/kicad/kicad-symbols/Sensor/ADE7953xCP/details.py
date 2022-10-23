
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor"
    oIndex = "ADE7953xCP"
    hexID = "SZKSENADE7953XCP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADE7953xCP', 'kicadSymbolFootprint': 'Package_CSP:LFCSP-28-1EP_5x5mm_P0.5mm_EP3.14x3.14mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/ADE7953.pdf', 'kicadSymbolki_keywords': 'Energy Metering', 'kicadSymbolki_description': 'Single Phase Multifunction Energy Metering with Neutral Current Measurement, LFCSP-28', 'kicadSymbolki_fp_filters': 'LFCSP*1EP*5x5mm*P0.5mm*'}])
    newPart['name'].append('ADE7953xCP')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

