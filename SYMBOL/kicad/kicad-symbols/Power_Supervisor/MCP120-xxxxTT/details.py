
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Supervisor"
    oIndex = "MCP120-xxxxTT"
    hexID = "SZKPOWERSUPERVISORMCP12XXXXTT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP120-xxxxTT', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/11184d.pdf', 'kicadSymbolki_keywords': 'supervisory circuit', 'kicadSymbolki_description': 'Microcontroller supervisory circuit, SOT-23', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Power_Supervisor : MCP120-xxxxTT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

