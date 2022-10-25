
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_Motor"
    oIndex = "L293"
    hexID = "SZKDRIVERMOTORL293"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'L293', 'kicadSymbolFootprint': 'Package_DIP:DIP-16_W7.62mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/l293.pdf', 'kicadSymbolki_keywords': 'Half-H Driver Motor', 'kicadSymbolki_description': 'Quadruple Half-H Drivers', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('Driver_Motor : L293')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

