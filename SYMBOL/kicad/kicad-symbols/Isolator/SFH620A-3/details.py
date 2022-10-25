
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "SFH620A-3"
    hexID = "SZKISOLATORSFH62A3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SFH620A-1', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SFH620A-3', 'kicadSymbolFootprint': 'Package_DIP:DIP-4_W7.62mm', 'kicadSymbolDatasheet': 'http://www.vishay.com/docs/83675/sfh620a.pdf', 'kicadSymbolki_keywords': 'Optocoupler, Phototransistor Output, 5300 VRMS, VCEO 70V, CTR% 100-320', 'kicadSymbolki_description': 'Optocoupler, Phototransistor Output, 5300 VRMS, VCEO 70V, CTR% 100-320 UL, cUL, BSI, THT PDIP-4', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('Isolator : SFH620A-3')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

