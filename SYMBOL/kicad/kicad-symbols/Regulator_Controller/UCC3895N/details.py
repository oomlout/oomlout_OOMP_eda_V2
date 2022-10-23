
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Controller"
    oIndex = "UCC3895N"
    hexID = "SZKREGULATORCONTROLLERUCC3895N"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'UCC3895N', 'kicadSymbolFootprint': 'Package_DIP:DIP-20_W7.62mm_LongPads', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/ucc3895.pdf', 'kicadSymbolki_keywords': 'Phase-shift full-bridge converter', 'kicadSymbolki_description': 'BiCMOS, Advanced Phase-ShiftPWM Controller, DIP-20', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('UCC3895N')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

