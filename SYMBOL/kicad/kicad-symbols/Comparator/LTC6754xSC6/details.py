
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Comparator"
    oIndex = "LTC6754xSC6"
    hexID = "SZKCOMPARATORLTC6754XSC6"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC6754xSC6', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/6754f.pdf', 'kicadSymbolki_keywords': 'cmp r2r rtr push-pull complementary', 'kicadSymbolki_description': 'Single High Speed Rail-to-Rail Input Comparator with LVDS Compatible Outputs, SC-70-6', 'kicadSymbolki_fp_filters': '*SC?70*'}])
    newPart['name'].append('Comparator : LTC6754xSC6')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

