
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LM723_TO100"
    hexID = "SZKREGULATORLINEARLM723TO1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM723_TO100', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-100-10', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm723.pdf', 'kicadSymbolki_keywords': 'POWER REGUL', 'kicadSymbolki_description': 'Linear Regulator (adjustable), TO-100', 'kicadSymbolki_fp_filters': 'TO?100*'}])
    newPart['name'].append('LM723_TO100')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

