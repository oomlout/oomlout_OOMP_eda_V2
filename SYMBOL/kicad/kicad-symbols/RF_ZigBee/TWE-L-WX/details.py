
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_ZigBee"
    oIndex = "TWE-L-WX"
    hexID = "SZKRFZIGBEETWELWX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TWE-L-WX', 'kicadSymbolFootprint': 'RF_Module:MonoWireless_TWE-L-WX', 'kicadSymbolDatasheet': 'https://www.mono-wireless.com/jp/products/TWE-LITE/MW-PDS-TWELITE-JP.pdf', 'kicadSymbolki_keywords': 'TWELITE', 'kicadSymbolki_description': 'NXP JN5164/JN5169 breakout module, SMD', 'kicadSymbolki_fp_filters': 'MonoWireless?TWE*'}])
    newPart['name'].append('TWE-L-WX')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

