
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "4N25"
    hexID = "SZKISOLATOR4N25"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '4N25', 'kicadSymbolFootprint': 'Package_DIP:DIP-6_W7.62mm', 'kicadSymbolDatasheet': 'https://www.vishay.com/docs/83725/4n25.pdf', 'kicadSymbolki_keywords': 'NPN DC Optocoupler Base Connected', 'kicadSymbolki_description': 'DC Optocoupler Base Connected, Vce 30V, CTR 20%, Viso 2500V, DIP6', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('Isolator : 4N25')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

