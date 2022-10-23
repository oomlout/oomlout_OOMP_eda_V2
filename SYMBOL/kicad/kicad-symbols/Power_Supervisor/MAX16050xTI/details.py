
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Supervisor"
    oIndex = "MAX16050xTI"
    hexID = "SZKPOWERSUPERVISORMAX165XTI"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX16050xTI', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-28-1EP_4x4mm_P0.4mm_EP2.6x2.6mm', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/MAX16050-MAX16051.pdf', 'kicadSymbolki_keywords': 'power sequencing', 'kicadSymbolki_description': '5 Voltage Monitor/Sequencer with Reverse-Sequencing Capability, QFN-28', 'kicadSymbolki_fp_filters': 'QFN*1EP*4x4mm*P0.4mm*'}])
    newPart['name'].append('MAX16050xTI')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

