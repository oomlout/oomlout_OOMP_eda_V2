
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "74xx"
    oIndex = "74LCX07"
    hexID = "SZK74XX74LCX7"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '74LCX07', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'www.st.com/resource/en/datasheet/74lcx07.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'CMOS hex buffer', 'kicadSymbolki_description': 'CMOS hex buffer (open drain) with 5V tolerant inputs', 'kicadSymbolki_fp_filters': 'SOIC*3.9x8.7mm*P1.27mm* TSSOP*4.4x5mm*P0.65mm* DIP*W7.62mm*'}])
    newPart['name'].append('74LCX07')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

