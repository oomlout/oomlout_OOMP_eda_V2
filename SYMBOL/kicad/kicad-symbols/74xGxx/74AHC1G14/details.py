
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "74xGxx"
    oIndex = "74AHC1G14"
    hexID = "SZK74XGXX74AHC1G14"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '74LVC1G14', 'kicadSymbolReference': 'U', 'kicadSymbolValue': '74AHC1G14', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.ti.com/lit/ds/symlink/sn74lvc1g14.pdf', 'kicadSymbolki_keywords': 'Single Gate NOT Schmitt LVC CMOS', 'kicadSymbolki_description': 'Single Schmitt NOT Gate, Low-Voltage CMOS', 'kicadSymbolki_fp_filters': 'SOT* SG-*'}])
    newPart['name'].append('74AHC1G14')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

