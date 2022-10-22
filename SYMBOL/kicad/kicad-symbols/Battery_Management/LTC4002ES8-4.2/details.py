
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Battery_Management"
    oIndex = "LTC4002ES8-4.2"
    hexID = "SZKBATMANAGEMENTLTC42ES842"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC4002ES8-4.2', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/4002f.pdf', 'kicadSymbolki_keywords': 'lithium li-ion battery charger', 'kicadSymbolki_description': 'Standalone Li-Ion Switch Mode Battery Charger, 4.7-22V input, single cell, SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*8*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('LTC4002ES8-4.2')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

