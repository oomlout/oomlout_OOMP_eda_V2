
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "Si8640ED-B-IS"
    hexID = "SZKISOLATORSI864EDBIS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'Si8640BB-B-IS', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'Si8640ED-B-IS', 'kicadSymbolFootprint': 'Package_SO:SOIC-16W_7.5x10.3mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.silabs.com/documents/public/data-sheets/si864x-datasheet.pdf', 'kicadSymbolki_keywords': '4Ch 4In Quad Digital Isolator 150Mbps', 'kicadSymbolki_description': 'Low-Power Quad-Channel Digital Isolator, 150Mbps, 2.5-5.5V, 5.0kV isolation, Fail-Safe High, SOIC-16W', 'kicadSymbolki_fp_filters': 'SOIC*7.5x10.3mm*P1.27mm*'}])
    newPart['name'].append('Si8640ED-B-IS')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

