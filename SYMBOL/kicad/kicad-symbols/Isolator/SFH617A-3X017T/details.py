
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "SFH617A-3X017T"
    hexID = "SZKISOLATORSFH617A3X17T"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SFH617A-1X007T', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SFH617A-3X017T', 'kicadSymbolFootprint': 'Package_DIP:SMDIP-4_W9.53mm_Clearance8mm', 'kicadSymbolDatasheet': 'http://www.vishay.com/docs/83740/sfh617a.pdf', 'kicadSymbolki_keywords': 'Optocoupler, Phototransistor Output, 5300 VRMS, VCEO 70V, CTR% 100-200', 'kicadSymbolki_description': 'Optocoupler, Phototransistor Output, 5300 VRMS, VCEO 70V, CTR% 100-200, -55 to +110 degree Celsius, VDE, UL, BSI, FIMKO, 8mm clearence SMD PDIP-4', 'kicadSymbolki_fp_filters': 'SMDIP*W9.53mm*Clearance8mm*'}])
    newPart['name'].append('Isolator : SFH617A-3X017T')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

