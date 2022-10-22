
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Audio"
    oIndex = "MAX98306xDT"
    hexID = "SZKAMPLIFIERAUDIOMAX9836XDT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX98306xDT', 'kicadSymbolFootprint': 'Package_DFN_QFN:TDFN-14-1EP_3x3mm_P0.4mm_EP1.78x2.35mm', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/MAX98306.pdf', 'kicadSymbolki_keywords': 'Class-D stereo amplifier', 'kicadSymbolki_description': 'Stereo 3.7 W Class D Amplifier, TDFN-14', 'kicadSymbolki_fp_filters': 'TDFN*1EP*3x3mm*P0.4mm*'}])
    newPart['name'].append('MAX98306xDT')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

