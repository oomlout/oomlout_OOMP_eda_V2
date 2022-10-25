
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "H11L3"
    hexID = "SZKISOLATORH11L3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'H11L1', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'H11L3', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/H11L3M-D.PDF', 'kicadSymbolki_keywords': 'High Speed Schmitt Optocoupler', 'kicadSymbolki_description': 'Schmitt Trigger Output Optocoupler, High Speed, DIP-6, 5mA turn on threshold', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* DIP*W10.16mm* SMDIP*W9.53mm*'}])
    newPart['name'].append('Isolator : H11L3')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

