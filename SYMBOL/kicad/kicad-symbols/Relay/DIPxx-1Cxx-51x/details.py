
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Relay"
    oIndex = "DIPxx-1Cxx-51x"
    hexID = "SZKRELAYDIPXX1CXX51X"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'K', 'kicadSymbolValue': 'DIPxx-1Cxx-51x', 'kicadSymbolFootprint': 'Relay_THT:Relay_StandexMeder_DIP_LowProfile', 'kicadSymbolDatasheet': 'https://standexelectronics.com/wp-content/uploads/datasheet_reed_relay_DIP.pdf', 'kicadSymbolki_keywords': 'Single Pole Reed Relay SPDT', 'kicadSymbolki_description': 'Standex Meder DIP reed relay, SPDT', 'kicadSymbolki_fp_filters': 'Relay*StandexMeder*DIP*LowProfile*'}])
    newPart['name'].append('Relay : DIPxx-1Cxx-51x')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

