
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "LED"
    oIndex = "APFA3010"
    hexID = "SZKLAPFA31"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'APFA3010', 'kicadSymbolFootprint': 'LED_SMD:LED_Kingbright_APFA3010_3x1.5mm_Horizontal', 'kicadSymbolDatasheet': 'http://www.kingbrightusa.com/images/catalog/SPEC/APFA3010LSEEZGKQBKC.pdf', 'kicadSymbolki_keywords': 'LED RGB SMD Kingbright APFA3010 Horizontal', 'kicadSymbolki_description': 'LED RGB, Common Anode, SMD, 3.0x1.5mm, Horizontal', 'kicadSymbolki_fp_filters': '*Kingbright*APFA3010*3x1.5mm*Horizontal*'}])
    newPart['name'].append('APFA3010')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

