
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_Motor"
    oIndex = "SN754410NE"
    hexID = "SZKDRIVERMOTORSN75441NE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SN754410NE', 'kicadSymbolFootprint': 'Package_DIP:DIP-16_W7.62mm', 'kicadSymbolDatasheet': 'https://www.ti.com/lit/ds/symlink/sn754410.pdf', 'kicadSymbolki_keywords': 'h-bridge motor driver', 'kicadSymbolki_description': 'Quadruple Half-H Driver, DIP-16', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('Driver_Motor : SN754410NE')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

