
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "SFH6206-3T"
    hexID = "SZKISOLATORSFH6263T"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SFH620A-2X007T', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SFH6206-3T', 'kicadSymbolFootprint': 'Package_DIP:SMDIP-4_W9.53mm_Clearance8mm', 'kicadSymbolDatasheet': 'http://www.vishay.com/docs/83675/sfh620a.pdf', 'kicadSymbolki_keywords': 'Optocoupler, Phototransistor Output, 5300 VRMS, VCEO 70V, CTR% 100-320', 'kicadSymbolki_description': 'Optocoupler, Phototransistor Output, 5300 VRMS, VCEO 70V, CTR% 100-320, UL, cUL, BSI, SMD-4', 'kicadSymbolki_fp_filters': 'SMDIP*W9.53mm?Clearance8mm*'}])
    newPart['name'].append('Isolator : SFH6206-3T')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

