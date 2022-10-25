
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Audio"
    oIndex = "MAX9850xTI"
    hexID = "SZKAMPLIFIERAUDIOMAX985XTI"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX9850xTI', 'kicadSymbolFootprint': 'Package_DFN_QFN:TQFN-28-1EP_5x5mm_P0.5mm_EP3.25x3.25mm_ThermalVias', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/MAX9850.pdf', 'kicadSymbolki_keywords': 'audio ampflifier stereo i2s', 'kicadSymbolki_description': 'Stereo audio DAC with headphone amplifier, TQFN-28', 'kicadSymbolki_fp_filters': 'TQFN*1EP*5x5mm*P0.5mm*'}])
    newPart['name'].append('Amplifier_Audio : MAX9850xTI')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

