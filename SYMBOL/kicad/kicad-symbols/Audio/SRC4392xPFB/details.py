
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Audio"
    oIndex = "SRC4392xPFB"
    hexID = "SZKAUDIOSRC4392XPFB"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SRC4392xPFB', 'kicadSymbolFootprint': 'Package_QFP:TQFP-48_7x7mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/src4392.pdf', 'kicadSymbolki_keywords': 'audio sample rate converter', 'kicadSymbolki_description': 'Two-Channel, Asynchronous Sample Rate Converter with Integrated Digital Audio Interface Receiver and Transmitter, TQFP-48', 'kicadSymbolki_fp_filters': 'TQFP*7x7mm*P0.5mm*'}])
    newPart['name'].append('Audio : SRC4392xPFB')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

