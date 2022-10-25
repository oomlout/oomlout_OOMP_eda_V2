
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "TLV1117-50"
    hexID = "SZKREGULATORLINEARTLV11175"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM1117-1.8', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TLV1117-50', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tlv1117.pdf', 'kicadSymbolki_keywords': 'linear regulator ldo fixed positive', 'kicadSymbolki_description': '800mA Low-Dropout Linear Regulator, 5.0V fixed output, TO-220/TO-252/TO-263/SOT-223', 'kicadSymbolki_fp_filters': 'SOT?223* TO?263* TO?252* TO?220*'}])
    newPart['name'].append('Regulator_Linear : TLV1117-50')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

