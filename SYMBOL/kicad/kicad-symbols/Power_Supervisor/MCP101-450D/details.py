
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Supervisor"
    oIndex = "MCP101-450D"
    hexID = "SZKPOWERSUPERVISORMCP1145D"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MCP101-270D', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP101-450D', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/11187f.pdf', 'kicadSymbolki_keywords': 'supervisor reset push-pull', 'kicadSymbolki_description': 'Microcontroller reset monitor, 4.50V threshold, active high output', 'kicadSymbolki_fp_filters': 'SOT?23* TO?92*'}])
    newPart['name'].append('MCP101-450D')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

