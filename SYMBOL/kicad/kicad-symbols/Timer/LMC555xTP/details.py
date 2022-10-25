
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Timer"
    oIndex = "LMC555xTP"
    hexID = "SZKTIMERLMC555XTP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LMC555xTP', 'kicadSymbolFootprint': 'Package_BGA:Texas_DSBGA-8_1.43x1.41mm_Layout3x3_P0.5mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lmc555.pdf', 'kicadSymbolki_keywords': 'single timer 555', 'kicadSymbolki_description': 'CMOS Timer, DSBGA-8', 'kicadSymbolki_fp_filters': 'Texas*DSBGA*P0.5mm*'}])
    newPart['name'].append('Timer : LMC555xTP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

