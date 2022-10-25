
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_ACDC"
    oIndex = "HLK-PM03"
    hexID = "SZKCONHLKPM3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'HLK-PM01', 'kicadSymbolReference': 'PS', 'kicadSymbolValue': 'HLK-PM03', 'kicadSymbolFootprint': 'Converter_ACDC:Converter_ACDC_HiLink_HLK-PMxx', 'kicadSymbolDatasheet': 'http://www.hlktech.net/product_detail.php?ProId=59', 'kicadSymbolki_keywords': 'AC/DC module power supply', 'kicadSymbolki_description': 'Compact AC/DC board mount power module 3W 3V3', 'kicadSymbolki_fp_filters': 'Converter*ACDC*HiLink*HLK?PM*'}])
    newPart['name'].append('Converter_ACDC : HLK-PM03')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

