
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "ADP5070AREZ"
    hexID = "SZKREGULATORSWITCHINGADP57AREZ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADP5070AREZ', 'kicadSymbolFootprint': 'Package_SO:ETSSOP-20-1EP_4.4x6.5mm_P0.65mm_EP3x4.2mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/ADP5070.pdf', 'kicadSymbolki_keywords': 'voltage regulator switching inverter double positive negative', 'kicadSymbolki_description': '1A/0.6A DC-to-DC Switching Regulator with Independent Positive and Negative Outputs', 'kicadSymbolki_fp_filters': 'ETSSOP*1EP?4.4x6.5mm?P0.65mm?EP3x4.2mm*'}])
    newPart['name'].append('ADP5070AREZ')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

