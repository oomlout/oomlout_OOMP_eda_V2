
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Audio"
    oIndex = "MA12040"
    hexID = "SZKAMPLIFIERAUDIOMA124"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MA12040', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-64-1EP_9x9mm_P0.5mm_EP5.45x5.45mm', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/Infineon-MA12040-DS-v01_00-EN.pdf?fileId=5546d46264a8de7e0164b7467a3d617c', 'kicadSymbolki_keywords': 'integrated class d amplifier', 'kicadSymbolki_description': 'Filterless and High-Efficiency +4V to +18V Audio Amplifier with Analog Input, QFN-64', 'kicadSymbolki_fp_filters': 'QFN*1EP*9x9mm*P0.5mm*'}])
    newPart['name'].append('MA12040')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

