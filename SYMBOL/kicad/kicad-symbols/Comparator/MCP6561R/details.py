
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Comparator"
    oIndex = "MCP6561R"
    hexID = "SZKCOMPARATORMCP6561R"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP6561R', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-5', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/MCP6561-1R-1U-2-4-1.8V-Low-Power-Push-Pull-Output-Comparator-DS20002139E.pdf', 'kicadSymbolki_keywords': 'cmp', 'kicadSymbolki_description': 'Single 1.8V Low-Power Push-Pull Output Comparator, SOT-23-5', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Comparator : MCP6561R')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

