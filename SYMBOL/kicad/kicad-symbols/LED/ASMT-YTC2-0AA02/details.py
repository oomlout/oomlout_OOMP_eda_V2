
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "LED"
    oIndex = "ASMT-YTC2-0AA02"
    hexID = "SZKLASMTYTC2AA2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'ASMT-YTC2-0AA02', 'kicadSymbolFootprint': 'LED_SMD:LED_Avago_PLCC6_3x2.8mm', 'kicadSymbolDatasheet': 'http://www.avagotech.com/docs/AV02-2589EN', 'kicadSymbolki_keywords': 'LED RGB', 'kicadSymbolki_description': 'Triple LED RVB (Avago Technology)', 'kicadSymbolki_fp_filters': 'LED?Avago?PLCC6?3x2.8mm*'}])
    newPart['name'].append('LED : ASMT-YTC2-0AA02')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

