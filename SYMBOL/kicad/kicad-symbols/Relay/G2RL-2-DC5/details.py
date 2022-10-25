
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Relay"
    oIndex = "G2RL-2-DC5"
    hexID = "SZKRELAYG2RL2DC5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'RL', 'kicadSymbolValue': 'G2RL-2-DC5', 'kicadSymbolFootprint': 'Relay_THT:Relay_DPDT_Omron_G2RL', 'kicadSymbolDatasheet': 'https://omronfs.omron.com/en_US/ecb/products/pdf/en-g2rl.pdf', 'kicadSymbolki_keywords': 'Omron Relay Dual Pole', 'kicadSymbolki_description': 'General Purpose Relay DPDT (2 Form C) Through Hole, Omron G2RL series, 5V coil', 'kicadSymbolki_fp_filters': 'Relay*DPDT*Omron*G2RL*'}])
    newPart['name'].append('Relay : G2RL-2-DC5')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

