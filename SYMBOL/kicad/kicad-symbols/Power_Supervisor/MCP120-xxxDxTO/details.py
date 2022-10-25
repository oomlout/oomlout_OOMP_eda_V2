
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Supervisor"
    oIndex = "MCP120-xxxDxTO"
    hexID = "SZKPOWERSUPERVISORMCP12XXXDXTO"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP120-xxxDxTO', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-92_Inline', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/11184d.pdf', 'kicadSymbolki_keywords': 'supervisory circuit', 'kicadSymbolki_description': 'Microcontroller supervisory circuit, TO-92', 'kicadSymbolki_fp_filters': 'TO*92*Inline*'}])
    newPart['name'].append('Power_Supervisor : MCP120-xxxDxTO')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

