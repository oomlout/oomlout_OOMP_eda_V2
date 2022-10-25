
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "74xx"
    oIndex = "74HC595"
    hexID = "SZK74XX74HC595"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '74HC595', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/sn74hc595.pdf', 'kicadSymbolki_keywords': 'HCMOS SR 3State', 'kicadSymbolki_description': '8-bit serial in/out Shift Register 3-State Outputs', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SOIC*3.9x9.9mm*P1.27mm* TSSOP*4.4x5mm*P0.65mm* SOIC*5.3x10.2mm*P1.27mm* SOIC*7.5x10.3mm*P1.27mm*'}])
    newPart['name'].append('74xx : 74HC595')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

