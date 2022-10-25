
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Comparator"
    oIndex = "MCP6562"
    hexID = "SZKCOMPARATORMCP6562"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP6562', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/MCP6561-1R-1U-2-4-1.8V-Low-Power-Push-Pull-Output-Comparator-DS20002139E.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'cmp', 'kicadSymbolki_description': 'Dual 1.8V Low-Power Push-Pull Output Comparator, SOIC-8/MSOP-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm* MSOP*3x3mm*P0.65mm*'}])
    newPart['name'].append('Comparator : MCP6562')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

