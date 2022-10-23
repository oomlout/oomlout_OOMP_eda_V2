
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Timer"
    oIndex = "82C54_PLCC"
    hexID = "SZKTIMER82C54PLCC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '82C54_PLCC', 'kicadSymbolFootprint': 'Package_LCC:PLCC-28', 'kicadSymbolDatasheet': 'http://download.intel.com/design/archives/periphrl/docs/23124406.pdf', 'kicadSymbolki_keywords': 'Timer Counter', 'kicadSymbolki_description': 'CHMOS Programmable Interval Timer, PLCC-28', 'kicadSymbolki_fp_filters': '*PLCC?28*'}])
    newPart['name'].append('82C54_PLCC')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

