
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_DCDC"
    oIndex = "BD8314NUV"
    hexID = "SZKCONBD8314NUV"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'BD8314NUV', 'kicadSymbolFootprint': 'Package_SON:VSON-10-1EP_3x3mm_P0.5mm_EP1.2x2mm', 'kicadSymbolDatasheet': 'http://rohmfs.rohm.com/en/products/databook/datasheet/ic/power/switching_regulator/bd8314nuv-e.pdf', 'kicadSymbolki_keywords': 'DCDC converter', 'kicadSymbolki_description': '3.0V to 12V, Integrated 2.5A MOSFET 1ch Boost Converter, VSON-10', 'kicadSymbolki_fp_filters': 'VSON*1EP*3x3mm*P0.5mm*'}])
    newPart['name'].append('Converter_DCDC : BD8314NUV')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

