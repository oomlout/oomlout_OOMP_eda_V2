
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_EPROM"
    oIndex = "27C256"
    hexID = "SZKMEMORYEPROM27C256"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '27C256', 'kicadSymbolFootprint': 'Package_DIP:DIP-28_W15.24mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/doc0014.pdf', 'kicadSymbolki_keywords': 'OTP EPROM 256 KiBit', 'kicadSymbolki_description': 'OTP EPROM 256 KiBit', 'kicadSymbolki_fp_filters': 'DIP*W15.24mm*'}])
    newPart['name'].append('Memory_EPROM : 27C256')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

