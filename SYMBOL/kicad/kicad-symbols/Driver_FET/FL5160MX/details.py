
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_FET"
    oIndex = "FL5160MX"
    hexID = "SZKDRIVERFETFL516MX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'FL5150MX', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'FL5160MX', 'kicadSymbolFootprint': 'Package_SO:SSOP-10_3.9x4.9mm_P1.00mm', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/FL5150-D.pdf', 'kicadSymbolki_keywords': 'dimmer', 'kicadSymbolki_description': 'IGBT and MOSFET, AC Phase Cut, Dimmer Controller, SSOP-10', 'kicadSymbolki_fp_filters': 'SSOP?10?3.9x4.9mm*1.00mm*'}])
    newPart['name'].append('FL5160MX')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

