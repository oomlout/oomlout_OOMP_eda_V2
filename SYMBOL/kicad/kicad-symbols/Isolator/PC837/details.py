
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "PC837"
    hexID = "SZKISOLATORPC837"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PC837', 'kicadSymbolFootprint': 'Package_DIP:DIP-12_W7.62mm', 'kicadSymbolDatasheet': 'http://www.soselectronic.cz/a_info/resource/d/pc817.pdf', 'kicadSymbolki_keywords': 'NPN DC Triple Optocoupler', 'kicadSymbolki_description': 'DC Triple Optocoupler, Vce 35V, CTR 50-300%, DIP12', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('Isolator : PC837')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

