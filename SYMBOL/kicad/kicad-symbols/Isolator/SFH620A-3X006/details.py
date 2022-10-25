
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "SFH620A-3X006"
    hexID = "SZKISOLATORSFH62A3X6"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SFH620A-1X006', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SFH620A-3X006', 'kicadSymbolFootprint': 'Package_DIP:DIP-4_W10.16mm', 'kicadSymbolDatasheet': 'http://www.vishay.com/docs/83675/sfh620a.pdf', 'kicadSymbolki_keywords': 'Optocoupler, Phototransistor Output, 5300 VRMS, VCEO 70V, CTR% 100-320', 'kicadSymbolki_description': 'Optocoupler, Phototransistor Output, 5300 VRMS, VCEO 70V, CTR% 100-320 UL, cUL, BSI, THT PDIP-4', 'kicadSymbolki_fp_filters': 'DIP*W10.16mm*'}])
    newPart['name'].append('Isolator : SFH620A-3X006')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

