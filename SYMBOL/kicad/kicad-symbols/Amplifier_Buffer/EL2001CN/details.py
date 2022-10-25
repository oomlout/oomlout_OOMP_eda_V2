
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Buffer"
    oIndex = "EL2001CN"
    hexID = "SZKAMPLIFIERBUFFEREL21CN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'EL2001CN', 'kicadSymbolFootprint': 'Package_DIP:DIP-8_W7.62mm', 'kicadSymbolDatasheet': 'http://www.datasheetlib.com/datasheet/677973/el2001_intersil.html#datasheet', 'kicadSymbolki_keywords': 'Monolithic high slew rate, buffer amplifier', 'kicadSymbolki_description': 'Monolithic high slew rate, buffer amplifier, DIP-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('Amplifier_Buffer : EL2001CN')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

