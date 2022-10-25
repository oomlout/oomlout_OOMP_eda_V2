
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Supervisor"
    oIndex = "MCP100-315D"
    hexID = "SZKPOWERSUPERVISORMCP1315D"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MCP100-270D', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP100-315D', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/11187f.pdf', 'kicadSymbolki_keywords': 'supervisor reset push-pull', 'kicadSymbolki_description': 'Microcontroller reset monitor, 3.15V threshold, active low output', 'kicadSymbolki_fp_filters': 'SOT?23* TO?92*'}])
    newPart['name'].append('Power_Supervisor : MCP100-315D')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

