
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "Filter_EMI_LL"
    hexID = "SZKDEVICEFILEMILL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'FL', 'kicadSymbolValue': 'Filter_EMI_LL', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'EMI filter', 'kicadSymbolki_description': 'EMI 2-inductor filter', 'kicadSymbolki_fp_filters': 'L_* L_CommonMode*'}])
    newPart['name'].append('Device : Filter_EMI_LL')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

