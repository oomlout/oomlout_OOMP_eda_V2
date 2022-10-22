
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "Filter_EMI_CommonMode"
    hexID = "SZKDEVICEFILEMICOONMODE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'Filter_EMI_LL', 'kicadSymbolReference': 'FL', 'kicadSymbolValue': 'Filter_EMI_CommonMode', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'EMI common mode filter', 'kicadSymbolki_description': 'EMI 2-inductor common mode filter', 'kicadSymbolki_fp_filters': 'L_* L_CommonMode*'}])
    newPart['name'].append('Filter_EMI_CommonMode')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

