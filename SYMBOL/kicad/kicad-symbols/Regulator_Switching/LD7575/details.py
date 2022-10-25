
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LD7575"
    hexID = "SZKREGULATORSWITCHINGLD7575"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LD7575', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.leadtrend.com.tw/archive/doc/product/sheets/LD7575-DS-04b.pdf', 'kicadSymbolki_keywords': 'smps controller', 'kicadSymbolki_description': 'Green-Mode PWM Controller with High-Voltage Start-Up Circuit, DIP-8/SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm* DIP*W7.62mm*'}])
    newPart['name'].append('Regulator_Switching : LD7575')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

