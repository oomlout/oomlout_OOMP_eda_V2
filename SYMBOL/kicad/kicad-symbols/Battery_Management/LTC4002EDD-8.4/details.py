
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Battery_Management"
    oIndex = "LTC4002EDD-8.4"
    hexID = "SZKBATMANAGEMENTLTC42EDD84"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LTC4002EDD-4.2', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC4002EDD-8.4', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-10-1EP_3x3mm_P0.5mm_EP1.55x2.48mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/4002f.pdf', 'kicadSymbolki_keywords': 'lithium li-ion battery charger', 'kicadSymbolki_description': 'Standalone Li-Ion Switch Mode Battery Charger, 8.9-22V input, double cell, DFN-10', 'kicadSymbolki_fp_filters': 'DFN*10*1EP*3x3mm*P0.5mm*'}])
    newPart['name'].append('LTC4002EDD-8.4')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

