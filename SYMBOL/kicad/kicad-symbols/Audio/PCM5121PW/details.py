
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Audio"
    oIndex = "PCM5121PW"
    hexID = "SZKAUDIOPCM5121PW"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PCM5122PW', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PCM5121PW', 'kicadSymbolFootprint': 'Package_SO:TSSOP-28_4.4x9.7mm_P0.65mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/pcm5121.pdf', 'kicadSymbolki_keywords': 'audio dac 2ch 32bit 384kHz', 'kicadSymbolki_description': '2VRMS DirectPath, 106dB Audio Stereo DAC with 32-bit, 384kHz PCM Interface, TSSOP-28', 'kicadSymbolki_fp_filters': 'TSSOP*4.4x9.7mm*P0.65mm*'}])
    newPart['name'].append('Audio : PCM5121PW')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

