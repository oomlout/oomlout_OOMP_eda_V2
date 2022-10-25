
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Audio"
    oIndex = "THAT1583"
    hexID = "SZKAUDIOTHAT1583"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'THAT1580', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'THAT1583', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-16-1EP_4x4mm_P0.65mm_EP2.1x2.1mm_ThermalVias', 'kicadSymbolDatasheet': 'http://www.thatcorp.com/datashts/THAT_1583_Datasheet.pdf', 'kicadSymbolki_keywords': 'diff amp mic preamp', 'kicadSymbolki_description': 'Low-Noise, Differential Audio Preamplifier IC, 0.006% THD+N, -128.9dBu EIN, QFN-16', 'kicadSymbolki_fp_filters': 'QFN*1EP*4x4mm*P0.65mm*'}])
    newPart['name'].append('Audio : THAT1583')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

