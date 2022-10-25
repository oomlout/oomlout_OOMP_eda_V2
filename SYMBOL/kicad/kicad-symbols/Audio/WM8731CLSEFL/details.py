
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Audio"
    oIndex = "WM8731CLSEFL"
    hexID = "SZKAUDIOWM8731CLSEFL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'WM8731CLSEFL', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-28-1EP_5x5mm_P0.5mm_EP3.35x3.35mm', 'kicadSymbolDatasheet': 'https://statics.cirrus.com/pubs/proDatasheet/WM8731_v4.9.pdf', 'kicadSymbolki_keywords': 'wolfson stereo audio codec adc dac headphone', 'kicadSymbolki_description': 'Portable Internet Audio CODEC with Headphone Driver and Programmable Sample Rates, QFN-28', 'kicadSymbolki_fp_filters': 'QFN*1EP*5x5mm*P0.5mm*'}])
    newPart['name'].append('Audio : WM8731CLSEFL')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

