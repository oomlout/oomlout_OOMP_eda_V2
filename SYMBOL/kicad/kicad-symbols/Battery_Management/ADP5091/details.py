
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Battery_Management"
    oIndex = "ADP5091"
    hexID = "SZKBATMANAGEMENTADP591"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADP5091', 'kicadSymbolFootprint': 'Package_CSP:LFCSP-24-1EP_4x4mm_P0.5mm_EP2.3x2.3mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/ADP5091-5092.pdf', 'kicadSymbolki_keywords': 'energy harvester', 'kicadSymbolki_description': 'Ultralow Power Energy Harvester PMUs with MPPT and Charge Management, LFCSP-24', 'kicadSymbolki_fp_filters': 'LFCSP*1EP*4x4mm*P0.5mm*'}])
    newPart['name'].append('ADP5091')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

