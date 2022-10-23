
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Supervisor"
    oIndex = "MCP130-xxxHxTO"
    hexID = "SZKPOWERSUPERVISORMCP13XXXHXTO"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MCP120-xxxHxTO', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP130-xxxHxTO', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-92_Inline', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/11184d.pdf', 'kicadSymbolki_keywords': 'supervisory circuit pull-up', 'kicadSymbolki_description': 'Microcontroller supervisory circuit with internal 5 kΩ pull-up, TO-92', 'kicadSymbolki_fp_filters': 'TO*92*Inline*'}])
    newPart['name'].append('MCP130-xxxHxTO')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

