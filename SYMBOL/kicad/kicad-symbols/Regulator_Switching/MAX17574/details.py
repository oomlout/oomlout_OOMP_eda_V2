
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "MAX17574"
    hexID = "SZKREGULATORSWITCHINGMAX17574"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX17574', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-24-1EP_4x5mm_P0.5mm_EP2.65x3.65mm', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/MAX17574.pdf', 'kicadSymbolki_keywords': 'Step-down dc-dc switching regulator', 'kicadSymbolki_description': '4.5V–60V, 3A, High-Efficiency, Synchronous Step-Down DC-DC Converter with Internal Compensation, QFN-24', 'kicadSymbolki_fp_filters': 'QFN*1EP*4x5mm*P0.5mm*'}])
    newPart['name'].append('MAX17574')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

