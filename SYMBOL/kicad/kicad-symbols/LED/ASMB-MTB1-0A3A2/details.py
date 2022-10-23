
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "LED"
    oIndex = "ASMB-MTB1-0A3A2"
    hexID = "SZKLASMBMTB1A3A2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'ASMB-MTB1-0A3A2', 'kicadSymbolFootprint': 'LED_SMD:LED_Avago_PLCC4_3.2x2.8mm_CW', 'kicadSymbolDatasheet': 'https://docs.broadcom.com/docs/AV02-4194EN', 'kicadSymbolki_keywords': 'led rgb diode', 'kicadSymbolki_description': 'Tricolor Black Surface LED, Common Anode Pin 4, PLCC-4', 'kicadSymbolki_fp_filters': '*Avago*PLCC4*3.2x2.8mm*'}])
    newPart['name'].append('ASMB-MTB1-0A3A2')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

