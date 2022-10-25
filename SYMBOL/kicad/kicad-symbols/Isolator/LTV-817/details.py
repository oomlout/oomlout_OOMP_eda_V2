
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "LTV-817"
    hexID = "SZKISOLATORLTV817"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTV-817', 'kicadSymbolFootprint': 'Package_DIP:DIP-4_W7.62mm', 'kicadSymbolDatasheet': 'http://www.us.liteon.com/downloads/LTV-817-827-847.PDF', 'kicadSymbolki_keywords': 'NPN DC Optocoupler', 'kicadSymbolki_description': 'DC Optocoupler, Vce 35V, CTR 50%, DIP-4', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('Isolator : LTV-817')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

