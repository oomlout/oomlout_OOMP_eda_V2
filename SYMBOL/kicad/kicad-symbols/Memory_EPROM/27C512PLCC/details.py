
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_EPROM"
    oIndex = "27C512PLCC"
    hexID = "SZKMEMORYEPROM27C512PLCC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '27C512PLCC', 'kicadSymbolFootprint': 'Package_LCC:PLCC-32_11.4x14.0mm_P1.27mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/doc0015.pdf', 'kicadSymbolki_keywords': 'OTP EPROM 512KiBit', 'kicadSymbolki_description': 'OTP EPROM 512 KiBit PLCC-32', 'kicadSymbolki_fp_filters': 'PLCC?32*11.4x14.0mm*P1.27mm*'}])
    newPart['name'].append('27C512PLCC')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

