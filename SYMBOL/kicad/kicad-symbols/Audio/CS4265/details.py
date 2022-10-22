
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Audio"
    oIndex = "CS4265"
    hexID = "SZKAUDIOCS4265"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CS4265', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-32-1EP_5x5mm_P0.5mm_EP3.6x3.6mm', 'kicadSymbolDatasheet': 'https://statics.cirrus.com/pubs/proDatasheet/CS4265_F5.pdf', 'kicadSymbolki_keywords': 'Audio codec 24bit 192khz stereo', 'kicadSymbolki_description': '104 dB, 24-Bit, 192 kHz Stereo Audio CODEC, QFN-32', 'kicadSymbolki_fp_filters': 'QFN*1EP*5x5mm*0.5mm*'}])
    newPart['name'].append('CS4265')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

