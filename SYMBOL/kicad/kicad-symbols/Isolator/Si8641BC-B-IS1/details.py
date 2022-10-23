
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "Si8641BC-B-IS1"
    hexID = "SZKISOLATORSI8641BCBIS1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'Si8641BB-B-IS1', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'Si8641BC-B-IS1', 'kicadSymbolFootprint': 'Package_SO:SOIC-16_3.9x9.9mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.silabs.com/documents/public/data-sheets/si864x-datasheet.pdf', 'kicadSymbolki_keywords': '4Ch 3In 1Out Quad Digital Isolator 150Mbps', 'kicadSymbolki_description': 'Low-Power Quad-Channel Digital Isolator, 150Mbps, 2.5-5.5V, 3.75kV isolation, Fail-Safe Low, SOIC-16', 'kicadSymbolki_fp_filters': 'SOIC*3.9x9.9mm*P1.27mm*'}])
    newPart['name'].append('Si8641BC-B-IS1')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

