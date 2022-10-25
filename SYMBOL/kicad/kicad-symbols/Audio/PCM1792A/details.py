
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Audio"
    oIndex = "PCM1792A"
    hexID = "SZKAUDIOPCM1792A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PCM1792A', 'kicadSymbolFootprint': 'Package_SO:SSOP-28_5.3x10.2mm_P0.65mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/pcm1792a.pdf', 'kicadSymbolki_keywords': 'audio dac 2ch 24bit 192kHz', 'kicadSymbolki_description': '24-Bit, 192-kHz Sampling, Advanced Segment, Audio Stereo Digital-to-Analog Converter, SW Control, SSOP-28', 'kicadSymbolki_fp_filters': 'SSOP*5.3x10.2mm*P0.65mm*'}])
    newPart['name'].append('Audio : PCM1792A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

