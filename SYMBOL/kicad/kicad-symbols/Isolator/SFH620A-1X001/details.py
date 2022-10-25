
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "SFH620A-1X001"
    hexID = "SZKISOLATORSFH62A1X1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SFH620A-1', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SFH620A-1X001', 'kicadSymbolFootprint': 'Package_DIP:DIP-4_W7.62mm', 'kicadSymbolDatasheet': 'http://www.vishay.com/docs/83675/sfh620a.pdf', 'kicadSymbolki_keywords': 'Optocoupler, Phototransistor Output, 5300 VRMS, VCEO 70V, CTR% 40-125', 'kicadSymbolki_description': 'Optocoupler, Phototransistor Output, 5300 VRMS, VCEO 70V, CTR% 40-125 VDE, UL, CUL, BSI, THT PDIP-4', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('Isolator : SFH620A-1X001')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

