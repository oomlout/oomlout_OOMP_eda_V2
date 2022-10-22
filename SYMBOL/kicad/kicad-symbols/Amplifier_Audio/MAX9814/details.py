
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Audio"
    oIndex = "MAX9814"
    hexID = "SZKAMPLIFIERAUDIOMAX9814"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX9814', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-14-1EP_3x3mm_P0.4mm_EP1.78x2.35mm', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/MAX9814.pdf', 'kicadSymbolki_keywords': 'audio microphone amplifier', 'kicadSymbolki_description': 'Microphone Amplifier with AGC and Low-Noise Microphone Bias, TDFN-14', 'kicadSymbolki_fp_filters': '*DFN*EP*3x3mm*P0.4mm*'}])
    newPart['name'].append('MAX9814')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

