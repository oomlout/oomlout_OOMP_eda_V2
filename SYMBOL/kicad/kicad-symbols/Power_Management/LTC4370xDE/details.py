
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "LTC4370xDE"
    hexID = "SZKPOWERMANAGEMENTLTC437XDE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC4370xDE', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-16-1EP_3x4mm_P0.45mm_EP1.7x3.3mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/4370f.pdf', 'kicadSymbolki_keywords': 'ideal-diode or-ing current sharing load balancing', 'kicadSymbolki_description': 'OR Controller Current Sharing Controller N-Channel 2:1, DFN-16', 'kicadSymbolki_fp_filters': 'DFN*1EP*3x4mm*P0.45mm*'}])
    newPart['name'].append('LTC4370xDE')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

