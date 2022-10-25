
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "H11AA1"
    hexID = "SZKISOLATORH11AA1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'H11AA1', 'kicadSymbolFootprint': 'Package_DIP:DIP-6_W7.62mm', 'kicadSymbolDatasheet': 'https://www.vishay.com/docs/83608/h11aa1.pdf', 'kicadSymbolki_keywords': 'NPN AC DC Optocoupler', 'kicadSymbolki_description': 'AC/DC NPN Optocoupler, DIP-6', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('Isolator : H11AA1')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

