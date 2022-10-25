
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LP38512TS-1.8"
    hexID = "SZKREGULATORLINEARLP38512TS18"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LP38512TS-1.8', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-263-5_TabPin6', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lp38512.pdf', 'kicadSymbolki_keywords': 'LDO Linear Regulator DDPAK D2PAK', 'kicadSymbolki_description': '1.5A Fast-Transient Response Low-Dropout Linear Voltage Regulator with Error Flag, 1.8V Output, TO-263', 'kicadSymbolki_fp_filters': 'TO*263*TabPin6*'}])
    newPart['name'].append('Regulator_Linear : LP38512TS-1.8')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

