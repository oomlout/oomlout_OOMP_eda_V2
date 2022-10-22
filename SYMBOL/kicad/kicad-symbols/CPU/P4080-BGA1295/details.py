
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "CPU"
    oIndex = "P4080-BGA1295"
    hexID = "SZKCPUP48BGA1295"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'P4080-BGA1295', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.nxp.com/jp/products/microcontrollers-and-processors/power-architecture-processors/qoriq-platforms/p-series/qoriq-p4080-p4040-p4081-multicore-communications-processors:P4080?&tab=Documentation_Tab&linkline=Data-Sheet', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'Communications Processor', 'kicadSymbolki_description': 'QorIQ P4080 Communications Processor, BGA-1295'}])
    newPart['name'].append('P4080-BGA1295')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

