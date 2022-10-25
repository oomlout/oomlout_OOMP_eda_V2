
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "CNY17-4"
    hexID = "SZKISOLATORCNY174"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'CNY17-1', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CNY17-4', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.vishay.com/docs/83606/cny17.pdf', 'kicadSymbolki_keywords': 'NPN DC Optocoupler Base Connected', 'kicadSymbolki_description': 'DC Optocoupler Base Connected, Vce 70V, CTR 160-320%, Viso 5000V (RMS), DIP6', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* DIP*W10.16mm* SMDIP*W9.53mm*'}])
    newPart['name'].append('Isolator : CNY17-4')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

