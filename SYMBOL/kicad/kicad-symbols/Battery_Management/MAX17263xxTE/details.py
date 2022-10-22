
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Battery_Management"
    oIndex = "MAX17263xxTE"
    hexID = "SZKBATMANAGEMENTMAX17263XXTE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX17263xxTE', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-14-1EP_3x3mm_P0.4mm_EP1.78x2.35mm', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/MAX17263.pdf', 'kicadSymbolki_keywords': 'fuel-gauge', 'kicadSymbolki_description': 'Single/Multi-Cell Fuel Gauge, ModelGauge m5 EZ, Integrated LED Control, TDFN-14', 'kicadSymbolki_fp_filters': 'DFN*1EP*3x3mm*P0.4mm*'}])
    newPart['name'].append('MAX17263xxTE')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

