
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_USB"
    oIndex = "FE1.1s"
    hexID = "SZKINTERFACEUFE11S"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'FE1.1s', 'kicadSymbolFootprint': 'Package_SO:SSOP-28_3.9x9.9mm_P0.635mm', 'kicadSymbolDatasheet': 'https://cdn-shop.adafruit.com/product-files/2991/FE1.1s+Data+Sheet+(Rev.+1.0).pdf', 'kicadSymbolki_keywords': '4-Port, EEPROM, High Speed, Hub, USB2.0', 'kicadSymbolki_description': 'USB 2.0 High Speed 4-Port Hub Controller, SSOP-28', 'kicadSymbolki_fp_filters': 'SSOP*3.9x9.9mm*P0.635mm*'}])
    newPart['name'].append('Interface_USB : FE1.1s')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

