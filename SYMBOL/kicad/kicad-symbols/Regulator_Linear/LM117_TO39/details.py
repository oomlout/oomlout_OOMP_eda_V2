
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LM117_TO39"
    hexID = "SZKREGULATORLINEARLM117TO39"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM317_TO39', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM117_TO39', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-39-3', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm317.pdf', 'kicadSymbolki_keywords': 'Adjustable Voltage Regulator 500mA Positive', 'kicadSymbolki_description': '500mA 35V Adjustable Linear Regulator, TO-39', 'kicadSymbolki_fp_filters': 'TO?39*'}])
    newPart['name'].append('LM117_TO39')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

