
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Comparator"
    oIndex = "LM2903"
    hexID = "SZKCOMPARATORLM293"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM2903', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm393.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'cmp open collector', 'kicadSymbolki_description': 'Low-Power, Low-Offset Voltage, Dual Comparators, DIP-8/SOIC-8/SOP-8/TSSOP-8/VSSOP-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm* DIP*W7.62mm* SOP*5.28x5.23mm*P1.27mm* VSSOP*3.0x3.0mm*P0.65mm* TSSOP*4.4x3mm*P0.65mm*'}])
    newPart['name'].append('Comparator : LM2903')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

