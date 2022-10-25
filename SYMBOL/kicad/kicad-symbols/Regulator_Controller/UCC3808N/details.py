
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Controller"
    oIndex = "UCC3808N"
    hexID = "SZKREGULATORCONTROLLERUCC388N"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'UCC3808N', 'kicadSymbolFootprint': 'Package_DIP:DIP-8_W7.62mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/ucc3808-2.pdf', 'kicadSymbolki_keywords': 'SMPS PWM Controller', 'kicadSymbolki_description': 'Low Power Current Mode Push-Pull PWM, PDIP-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('Regulator_Controller : UCC3808N')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

