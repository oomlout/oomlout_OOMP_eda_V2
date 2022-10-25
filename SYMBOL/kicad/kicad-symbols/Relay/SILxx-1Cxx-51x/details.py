
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Relay"
    oIndex = "SILxx-1Cxx-51x"
    hexID = "SZKRELAYSILXX1CXX51X"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'K', 'kicadSymbolValue': 'SILxx-1Cxx-51x', 'kicadSymbolFootprint': 'Relay_THT:Relay_SPDT_StandexMeder_SIL_Form1C', 'kicadSymbolDatasheet': 'https://standexelectronics.com/wp-content/uploads/datasheet_reed_relay_SIL.pdf', 'kicadSymbolki_keywords': 'Single Pole Reed Relay SPDT', 'kicadSymbolki_description': 'Standex Meder SIL reed relay, SPDT', 'kicadSymbolki_fp_filters': 'Relay*SPDT*StandexMeder*SIL*Form1C*'}])
    newPart['name'].append('Relay : SILxx-1Cxx-51x')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

