
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_ACDC"
    oIndex = "HLK-PM01"
    hexID = "SZKCONHLKPM1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'PS', 'kicadSymbolValue': 'HLK-PM01', 'kicadSymbolFootprint': 'Converter_ACDC:Converter_ACDC_HiLink_HLK-PMxx', 'kicadSymbolDatasheet': 'http://www.hlktech.net/product_detail.php?ProId=54', 'kicadSymbolki_keywords': 'AC/DC module power supply', 'kicadSymbolki_description': 'Compact AC/DC board mount power module 3W 5V', 'kicadSymbolki_fp_filters': 'Converter*ACDC*HiLink*HLK?PM*'}])
    newPart['name'].append('HLK-PM01')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

