
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface"
    oIndex = "PCI9030-PQFP176"
    hexID = "SZKINTERFACEPCI93PQFP176"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PCI9030-PQFP176', 'kicadSymbolFootprint': 'Package_QFP:LQFP-176_24x24mm_P0.5mm', 'kicadSymbolDatasheet': 'http://lhcb-online.web.cern.ch/lhcb-online/ecs/ccpc/docs/plc-9030-databook.pdf', 'kicadSymbolki_keywords': 'PCI', 'kicadSymbolki_description': 'PCI SMARTarget I/O Accelerator', 'kicadSymbolki_fp_filters': 'LQFP*24x24mm*P0.5mm*'}])
    newPart['name'].append('PCI9030-PQFP176')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

