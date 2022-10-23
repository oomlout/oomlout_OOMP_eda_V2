
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Relay"
    oIndex = "SILxx-1Axx-71x"
    hexID = "SZKRELAYSILXX1AXX71X"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'K', 'kicadSymbolValue': 'SILxx-1Axx-71x', 'kicadSymbolFootprint': 'Relay_THT:Relay_SPST_StandexMeder_SIL_Form1A', 'kicadSymbolDatasheet': 'https://standexelectronics.com/wp-content/uploads/datasheet_reed_relay_SIL.pdf', 'kicadSymbolki_keywords': 'Single Pole Reed Relay SPST', 'kicadSymbolki_description': 'Standex Meder SIL reed relay, SPST, Closing Contact', 'kicadSymbolki_fp_filters': 'Relay*SPST*StandexMeder*SIL*Form1A*'}])
    newPart['name'].append('SILxx-1Axx-71x')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

