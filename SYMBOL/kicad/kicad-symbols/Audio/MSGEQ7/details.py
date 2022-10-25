
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Audio"
    oIndex = "MSGEQ7"
    hexID = "SZKAUDIOMSGEQ7"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MSGEQ7', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://mix-sig.com/images/datasheets/MSGEQ7.pdf', 'kicadSymbolki_keywords': 'equalizer filter', 'kicadSymbolki_description': 'Seven Band Graphic Equalizer, DIP-8/SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm* DIP*W7.62mm*'}])
    newPart['name'].append('Audio : MSGEQ7')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

