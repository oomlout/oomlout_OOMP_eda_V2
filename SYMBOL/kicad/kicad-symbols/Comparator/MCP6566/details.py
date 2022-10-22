
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Comparator"
    oIndex = "MCP6566"
    hexID = "SZKCOMPARATORMCP6566"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP6566', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/MCP6566-6R-6U-7-9-1.8V-Low-Power-Open-Drain-Output-Comparator-DS20002143G.pdf', 'kicadSymbolki_keywords': 'cmp collector', 'kicadSymbolki_description': 'Single 1.8V Low-Power Open-Drain Output Comparator, SOT-23-5/SC-70', 'kicadSymbolki_fp_filters': 'SOT?23* *SC*70*'}])
    newPart['name'].append('MCP6566')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

