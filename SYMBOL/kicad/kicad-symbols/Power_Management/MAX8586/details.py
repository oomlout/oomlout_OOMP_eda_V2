
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "MAX8586"
    hexID = "SZKPOWERMANAGEMENTMAX8586"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX8586', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-8-1EP_3x3mm_P0.65mm_EP1.55x2.4mm', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/MAX8586.pdf', 'kicadSymbolki_keywords': '1-channel USB current limiting power switch', 'kicadSymbolki_description': 'Single 1.2A USB Current Limiting Switch', 'kicadSymbolki_fp_filters': 'DFN?8?1EP*3x3mm*P0.65mm*EP1.55x2.4mm*'}])
    newPart['name'].append('MAX8586')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

