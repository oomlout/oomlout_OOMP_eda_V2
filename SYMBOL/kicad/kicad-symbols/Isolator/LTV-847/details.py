
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "LTV-847"
    hexID = "SZKISOLATORLTV847"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PC847', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTV-847', 'kicadSymbolFootprint': 'Package_DIP:DIP-16_W7.62mm', 'kicadSymbolDatasheet': 'http://optoelectronics.liteon.com/upload/download/DS-70-96-0016/LTV-8X7%20series.PDF', 'kicadSymbolki_keywords': 'NPN DC Quad Optocoupler', 'kicadSymbolki_description': 'Quad DC Optocoupler, Vce 35V, CTR 50%, DIP-16', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('Isolator : LTV-847')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

