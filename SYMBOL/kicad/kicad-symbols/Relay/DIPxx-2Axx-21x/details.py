
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Relay"
    oIndex = "DIPxx-2Axx-21x"
    hexID = "SZKRELAYDIPXX2AXX21X"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'K', 'kicadSymbolValue': 'DIPxx-2Axx-21x', 'kicadSymbolFootprint': 'Relay_THT:Relay_StandexMeder_DIP_LowProfile', 'kicadSymbolDatasheet': 'https://standexelectronics.com/wp-content/uploads/datasheet_reed_relay_DIP.pdf', 'kicadSymbolki_keywords': 'Single Pole Reed Relay DPST', 'kicadSymbolki_description': 'Standex Meder DIP reed relay, DPST, Closing Contacts', 'kicadSymbolki_fp_filters': 'Relay*StandexMeder*DIP*LowProfile*'}])
    newPart['name'].append('Relay : DIPxx-2Axx-21x')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

