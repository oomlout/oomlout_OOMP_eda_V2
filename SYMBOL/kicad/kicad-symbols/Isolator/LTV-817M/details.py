
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "LTV-817M"
    hexID = "SZKISOLATORLTV817M"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTV-817M', 'kicadSymbolFootprint': 'Package_DIP:DIP-4_W10.16mm', 'kicadSymbolDatasheet': 'http://www.us.liteon.com/downloads/LTV-817-827-847.PDF', 'kicadSymbolki_keywords': 'NPN DC Optocoupler', 'kicadSymbolki_description': 'DC Optocoupler, Vce 35V, CTR 50%, DIP-4', 'kicadSymbolki_fp_filters': 'DIP*W10.16mm*'}])
    newPart['name'].append('Isolator : LTV-817M')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

