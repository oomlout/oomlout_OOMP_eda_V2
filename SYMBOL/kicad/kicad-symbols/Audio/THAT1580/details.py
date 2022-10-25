
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Audio"
    oIndex = "THAT1580"
    hexID = "SZKAUDIOTHAT158"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'THAT1580', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-16-1EP_4x4mm_P0.65mm_EP2.1x2.1mm_ThermalVias', 'kicadSymbolDatasheet': 'http://www.thatcorp.com/datashts/THAT_1580_Datasheet.pdf', 'kicadSymbolki_keywords': 'diff amp mic preamp', 'kicadSymbolki_description': 'Low-Noise, Differential Audio Preamplifier IC, 0.005% THD+N, -134.8dBu EIN, QFN-16', 'kicadSymbolki_fp_filters': 'QFN*1EP*4x4mm*P0.65mm*'}])
    newPart['name'].append('Audio : THAT1580')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

