
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Relay"
    oIndex = "JW2"
    hexID = "SZKRELAYJW2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'RL', 'kicadSymbolValue': 'JW2', 'kicadSymbolFootprint': 'Relay_THT:Relay_DPDT_Panasonic_JW2', 'kicadSymbolDatasheet': 'http://www3.panasonic.biz/ac/e_download/control/relay/power/catalog/mech_eng_jw.pdf?via=ok', 'kicadSymbolki_keywords': 'Panasonic Relay Dual Pole', 'kicadSymbolki_description': 'General Purpose Relay DPDT (2 Form C) Through Hole, Panasonic JW series', 'kicadSymbolki_fp_filters': 'Relay*DPDT*Panasonic*JW2*'}])
    newPart['name'].append('Relay : JW2')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

