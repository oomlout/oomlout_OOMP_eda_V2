
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Oscillator"
    oIndex = "KC2520Z"
    hexID = "SZKOCSKC252Z"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'KC2520Z', 'kicadSymbolFootprint': 'Oscillator:Oscillator_SMD_Kyocera_KC2520Z-4Pin_2.5x2.0mm', 'kicadSymbolDatasheet': 'https://global.kyocera.com/prdct/electro/product/pdf/clock_z_xz_e.pdf', 'kicadSymbolki_keywords': 'xo', 'kicadSymbolki_description': '1.8432MHz ~ 125MHz Crystal Oscillator', 'kicadSymbolki_fp_filters': 'Oscillator*SMD*Kyocera*KC2520Z*2.5x2.0mm*'}])
    newPart['name'].append('KC2520Z')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

