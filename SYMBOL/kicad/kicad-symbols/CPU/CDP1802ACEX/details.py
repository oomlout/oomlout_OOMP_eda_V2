
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "CPU"
    oIndex = "CDP1802ACEX"
    hexID = "SZKCPUCDP182ACEX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'CDP1802ACE', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CDP1802ACEX', 'kicadSymbolFootprint': 'Package_DIP:DIP-40_W15.24mm', 'kicadSymbolDatasheet': 'http://www.cosmacelf.com/publications/data-sheets/cdp1802.pdf', 'kicadSymbolki_keywords': 'CPU Processor', 'kicadSymbolki_description': '8-bit, General Purpose, 5V, 3.2 MHz, Burned-In, DIP-40', 'kicadSymbolki_fp_filters': 'DIP*W15.24mm*'}])
    newPart['name'].append('CDP1802ACEX')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

