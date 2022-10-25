
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Controller"
    oIndex = "UCC1895J"
    hexID = "SZKREGULATORCONTROLLERUCC1895J"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'UCC3895N', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'UCC1895J', 'kicadSymbolFootprint': 'Package_DIP:DIP-20_W7.62mm_LongPads', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/ucc3895.pdf', 'kicadSymbolki_keywords': 'Phase-shift full-bridge converter', 'kicadSymbolki_description': 'BiCMOS, Advanced Phase-ShiftPWM Controller, CDIP-20', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('Regulator_Controller : UCC1895J')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

