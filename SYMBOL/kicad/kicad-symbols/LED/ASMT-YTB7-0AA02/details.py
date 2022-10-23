
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "LED"
    oIndex = "ASMT-YTB7-0AA02"
    hexID = "SZKLASMTYTB7AA2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ASMT-YTC2-0AA02', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'ASMT-YTB7-0AA02', 'kicadSymbolFootprint': 'LED_SMD:LED_Avago_PLCC6_3x2.8mm', 'kicadSymbolDatasheet': 'https://docs.broadcom.com/docs/AV02-3793EN', 'kicadSymbolki_keywords': 'LED RGB', 'kicadSymbolki_description': 'Triple LED RVB (Avago Technology)', 'kicadSymbolki_fp_filters': 'LED?Avago?PLCC6?3x2.8mm*'}])
    newPart['name'].append('ASMT-YTB7-0AA02')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

