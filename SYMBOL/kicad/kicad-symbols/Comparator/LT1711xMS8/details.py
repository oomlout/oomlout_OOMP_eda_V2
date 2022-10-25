
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Comparator"
    oIndex = "LT1711xMS8"
    hexID = "SZKCOMPARATORLT1711XMS8"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LT1711xMS8', 'kicadSymbolFootprint': 'Package_SO:MSOP-8_3x3mm_P0.65mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/171112f.pdf', 'kicadSymbolki_keywords': 'cmp latch push-pull complementary', 'kicadSymbolki_description': 'Single ultrafast 4.5 ns rail-to-rail comparator, MSOP-8', 'kicadSymbolki_fp_filters': 'MSOP*3x3mm*P0.65mm*'}])
    newPart['name'].append('Comparator : LT1711xMS8')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

