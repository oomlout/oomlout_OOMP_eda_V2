
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "EL814"
    hexID = "SZKISOLATOREL814"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'EL814', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.everlight.com/file/ProductFile/EL814.pdf', 'kicadSymbolki_keywords': 'NPN AC DC Optocoupler', 'kicadSymbolki_description': 'AC/DC NPN Optocoupler, DIP4/SMD4', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* DIP*W10.16mm* SMDIP*W9.53mm*'}])
    newPart['name'].append('Isolator : EL814')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

