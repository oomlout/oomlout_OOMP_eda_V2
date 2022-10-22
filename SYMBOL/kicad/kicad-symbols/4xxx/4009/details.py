
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "4xxx"
    oIndex = "4009"
    hexID = "SZK4XXX49"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '4009', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.sycelectronica.com.ar/semiconductores/CD4009.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'CMOS INV BUFFER high sink, VCC and VDD sep. VDD>VI>VCC!', 'kicadSymbolki_description': 'Hex Buffer Inverter', 'kicadSymbolki_fp_filters': 'DIP?16*'}])
    newPart['name'].append('4009')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

