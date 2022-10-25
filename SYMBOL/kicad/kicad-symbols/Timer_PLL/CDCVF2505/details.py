
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Timer_PLL"
    oIndex = "CDCVF2505"
    hexID = "SZKTIMERPLLCDCVF255"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CDCVF2505', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/cdcvf2505.pdf', 'kicadSymbolki_keywords': 'pll clock driver', 'kicadSymbolki_description': 'Clock Phase-Lock Loop Clock Driver, 24-200MHz, 3.3V, SOIC-8/TSSOP-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm* TSSOP*4.4x3mm*P0.65mm*'}])
    newPart['name'].append('Timer_PLL : CDCVF2505')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

