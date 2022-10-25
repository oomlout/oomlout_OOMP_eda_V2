
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Timer"
    oIndex = "LM556"
    hexID = "SZKTIMERLM556"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM556', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm556.pdf', 'kicadSymbolki_keywords': 'dual timer', 'kicadSymbolki_description': 'Dual Timer, DIP-14/SOIC-14', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* TSSOP*5.3x6.2mm*P0.65mm* SOIC*3.9x8.7mm*P1.27mm*'}])
    newPart['name'].append('Timer : LM556')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

