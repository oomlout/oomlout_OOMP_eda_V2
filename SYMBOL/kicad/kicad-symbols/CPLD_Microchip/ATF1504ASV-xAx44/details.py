
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "CPLD_Microchip"
    oIndex = "ATF1504ASV-xAx44"
    hexID = "SZKCPLDMCHIPATF154ASVXAX44"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ATF1502AS-xAx44', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATF1504ASV-xAx44', 'kicadSymbolFootprint': 'Package_QFP:TQFP-44_10x10mm_P0.8mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/ATF1504ASV-ATF1504ASVL-Data-Sheet-20006185A.pdf', 'kicadSymbolki_keywords': 'CPLD', 'kicadSymbolki_description': 'Microchip CPLD, 64 Macrocell, 3.3 V, TQFP-44', 'kicadSymbolki_fp_filters': 'TQFP*10x10mm*P0.8mm*'}])
    newPart['name'].append('ATF1504ASV-xAx44')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

