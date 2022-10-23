
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Relay"
    oIndex = "DIPxx-1Axx-11x"
    hexID = "SZKRELAYDIPXX1AXX11X"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'K', 'kicadSymbolValue': 'DIPxx-1Axx-11x', 'kicadSymbolFootprint': 'Relay_THT:Relay_StandexMeder_DIP_LowProfile', 'kicadSymbolDatasheet': 'https://standexelectronics.com/wp-content/uploads/datasheet_reed_relay_DIP.pdf', 'kicadSymbolki_keywords': 'Single Pole Reed Relay SPST', 'kicadSymbolki_description': 'Standex Meder DIP reed relay, SPST, Closing Contact', 'kicadSymbolki_fp_filters': 'Relay*StandexMeder*DIP*LowProfile*'}])
    newPart['name'].append('DIPxx-1Axx-11x')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

