
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_EPROM"
    oIndex = "27C020"
    hexID = "SZKMEMORYEPROM27C2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '27C020', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/devicedoc/doc0570.pdf', 'kicadSymbolki_keywords': 'OTP EPROM 2MiBit', 'kicadSymbolki_description': 'OTP EPROM 2 MiBit (256 Ki x 8 Bit)', 'kicadSymbolki_fp_filters': 'DIP*W15.24mm* PLCC*'}])
    newPart['name'].append('Memory_EPROM : 27C020')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

