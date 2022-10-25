
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Comparator"
    oIndex = "MCP6561x-LT"
    hexID = "SZKCOMPARATORMCP6561XLT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP6561x-LT', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-353_SC-70-5', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/MCP6561-1R-1U-2-4-1.8V-Low-Power-Push-Pull-Output-Comparator-DS20002139E.pdf', 'kicadSymbolki_keywords': 'cmp', 'kicadSymbolki_description': 'Single 1.8V Low-Power Push-Pull Output Comparator, SC-70-5', 'kicadSymbolki_fp_filters': 'SOT?353*'}])
    newPart['name'].append('Comparator : MCP6561x-LT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

