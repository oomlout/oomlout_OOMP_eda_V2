
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "LED"
    oIndex = "SMLVN6RGB"
    hexID = "SZKLSMLVN6RGB"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'SMLVN6RGB', 'kicadSymbolFootprint': 'LED_SMD:LED_ROHM_SMLVN6', 'kicadSymbolDatasheet': 'https://www.rohm.com/datasheet/SMLVN6RGB1U', 'kicadSymbolki_keywords': 'LED RGB Diode', 'kicadSymbolki_description': 'High Brightness Tri-Color LED, RGB, 3.5x2.8mm', 'kicadSymbolki_fp_filters': 'LED*ROHM*SMLVN6*'}])
    newPart['name'].append('LED : SMLVN6RGB')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

