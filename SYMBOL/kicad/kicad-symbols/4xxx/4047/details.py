
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "4xxx"
    oIndex = "4047"
    hexID = "SZK4XXX447"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '4047', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.ti.com/lit/ds/symlink/cd4047b.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'CMOS monostable astable multivibrator', 'kicadSymbolki_description': 'Monostable/Astable Multivibrator', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SOIC*3.9x8.7mm*P1.27mm*'}])
    newPart['name'].append('4xxx : 4047')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

