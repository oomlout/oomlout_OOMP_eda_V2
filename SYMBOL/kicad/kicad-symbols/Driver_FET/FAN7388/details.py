
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_FET"
    oIndex = "FAN7388"
    hexID = "SZKDRIVERFETFAN7388"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'FAN7888', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'FAN7388', 'kicadSymbolFootprint': 'Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/FAN7388-D.pdf', 'kicadSymbolki_keywords': '3 Phase Gate Driver', 'kicadSymbolki_description': '3 Half-Bridge Gate-Drive IC, 600V operation, Output Current 350/650mA, SOIC-20', 'kicadSymbolki_fp_filters': 'SOIC*7.5x12.8*P1.27mm*'}])
    newPart['name'].append('FAN7388')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

