
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Audio"
    oIndex = "MAX9715ETE+"
    hexID = "SZKAMPLIFIERAUDIOMAX9715ETE+"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX9715ETE+', 'kicadSymbolFootprint': 'Package_DFN_QFN:TQFN-16-1EP_5x5mm_P0.8mm_EP3.1x3.1mm', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/MAX9715.pdf', 'kicadSymbolki_keywords': 'Class-D Stereo', 'kicadSymbolki_description': '2.8W, Low-EMI, Stereo, Filterless Class D Audio Amplifier, TQFN-16', 'kicadSymbolki_fp_filters': 'TQFN*1EP*5x5mm*P0.8mm*'}])
    newPart['name'].append('MAX9715ETE+')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

