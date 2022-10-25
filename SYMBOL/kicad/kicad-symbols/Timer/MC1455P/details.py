
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Timer"
    oIndex = "MC1455P"
    hexID = "SZKTIMERMC1455P"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'NE555P', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MC1455P', 'kicadSymbolFootprint': 'Package_DIP:DIP-8_W7.62mm', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/MC1455-D.PDF', 'kicadSymbolki_keywords': 'single timer 555', 'kicadSymbolki_description': 'Timer, 555 compatible, PDIP-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('Timer : MC1455P')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

