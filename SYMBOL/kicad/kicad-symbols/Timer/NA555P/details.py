
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Timer"
    oIndex = "NA555P"
    hexID = "SZKTIMERNA555P"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'NE555P', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'NA555P', 'kicadSymbolFootprint': 'Package_DIP:DIP-8_W7.62mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/ne555.pdf', 'kicadSymbolki_keywords': 'single timer 555', 'kicadSymbolki_description': 'Precision Timers, 555 compatible, PDIP-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('Timer : NA555P')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

