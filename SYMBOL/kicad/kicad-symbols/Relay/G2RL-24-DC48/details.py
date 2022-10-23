
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Relay"
    oIndex = "G2RL-24-DC48"
    hexID = "SZKRELAYG2RL24DC48"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'G2RL-2-DC5', 'kicadSymbolReference': 'RL', 'kicadSymbolValue': 'G2RL-24-DC48', 'kicadSymbolFootprint': 'Relay_THT:Relay_DPDT_Omron_G2RL', 'kicadSymbolDatasheet': 'https://omronfs.omron.com/en_US/ecb/products/pdf/en-g2rl.pdf', 'kicadSymbolki_keywords': 'Omron Relay Dual Pole', 'kicadSymbolki_description': 'General Purpose Relay DPDT (2 Form C) Through Hole, Omron G2RL series, sealed, 48V coil', 'kicadSymbolki_fp_filters': 'Relay*DPDT*Omron*G2RL*'}])
    newPart['name'].append('G2RL-24-DC48')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

