
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "74xGxx"
    oIndex = "74LVC1GU04DRL"
    hexID = "SZK74XGXX74LVC1GU4DRL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '74LVC1GU04DRL', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-553', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/sn74lvc1gu04.pdf', 'kicadSymbolki_keywords': 'inverter cmos', 'kicadSymbolki_description': 'Single Inverter Gate, SOT-553', 'kicadSymbolki_fp_filters': 'SOT*553*'}])
    newPart['name'].append('74LVC1GU04DRL')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

