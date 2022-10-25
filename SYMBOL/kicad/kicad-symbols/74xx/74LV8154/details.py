
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "74xx"
    oIndex = "74LV8154"
    hexID = "SZK74XX74LV8154"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '74LV8154', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/sn74lv8154.pdf', 'kicadSymbolki_keywords': 'counter binary', 'kicadSymbolki_description': 'Dual 16-bit binary counter', 'kicadSymbolki_fp_filters': 'TSSOP*4.4x6.5mm*P0.65mm* DIP*W7.62mm*'}])
    newPart['name'].append('74xx : 74LV8154')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

