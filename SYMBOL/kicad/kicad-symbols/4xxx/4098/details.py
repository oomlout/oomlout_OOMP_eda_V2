
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "4xxx"
    oIndex = "4098"
    hexID = "SZK4XXX498"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '4098', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/cd4098b.pdf', 'kicadSymbolki_keywords': 'CMOS monostable multivibrator', 'kicadSymbolki_description': 'Dual Monostable Multivibrator', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SOIC*3.9x9.9mm*P1.27mm* TSSOP*4.4x5mm*P0.65mm*'}])
    newPart['name'].append('4xxx : 4098')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

