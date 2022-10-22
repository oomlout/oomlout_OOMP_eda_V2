
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Current"
    oIndex = "INA194"
    hexID = "SZKAMPLIFIERCURRENTINA194"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'INA193', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'INA194', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-5', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/ina193.pdf', 'kicadSymbolki_keywords': 'current sense shunt monitor', 'kicadSymbolki_description': 'Current Shunt Monitor −16V to +80V Common-Mode Range, 50V/V, SOT-23-5', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('INA194')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

