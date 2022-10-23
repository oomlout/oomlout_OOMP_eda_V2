
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Supervisor"
    oIndex = "MC34064P"
    hexID = "SZKPOWERSUPERVISORMC3464P"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MC34064P', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-92L_Inline', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/MC34064-D.PDF', 'kicadSymbolki_keywords': 'Power Supervisor', 'kicadSymbolki_description': 'Undervoltage Sensing Circuit, TO-92', 'kicadSymbolki_fp_filters': 'TO?92L?Inline*'}])
    newPart['name'].append('MC34064P')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

