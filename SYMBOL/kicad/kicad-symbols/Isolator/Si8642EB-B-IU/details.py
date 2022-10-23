
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "Si8642EB-B-IU"
    hexID = "SZKISOLATORSI8642EBBIU"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'Si8642BA-B-IU', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'Si8642EB-B-IU', 'kicadSymbolFootprint': 'Package_SO:QSOP-16_3.9x4.9mm_P0.635mm', 'kicadSymbolDatasheet': 'https://www.silabs.com/documents/public/data-sheets/si864x-datasheet.pdf', 'kicadSymbolki_keywords': '4Ch 2In 2Out Quad Digital Isolator 150Mbps', 'kicadSymbolki_description': 'Low-Power Quad-Channel Digital Isolator, 150Mbps, 2.5-5.5V, 2.5kV isolation, Fail-Safe High, QSOP-16', 'kicadSymbolki_fp_filters': 'QSOP*3.9x4.9mm*P0.635mm*'}])
    newPart['name'].append('Si8642EB-B-IU')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

