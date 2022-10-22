
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Battery_Management"
    oIndex = "LT3652IDD"
    hexID = "SZKBATMANAGEMENTLT3652IDD"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LT3652EDD', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LT3652IDD', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-12-1EP_3x3mm_P0.45mm_EP1.66x2.38mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/3652fe.pdf', 'kicadSymbolki_keywords': 'Step-down  battery charger, Lithium Phosphate ( LiFePO4), Lead (Pb), Lithium+ (Li+) , 4.95V to 32V VDD, -40 to +125 degree Celsius, DFN-12', 'kicadSymbolki_description': 'Step-down  battery charger, Lithium Phosphate ( LiFePO4), Lead (Pb), Lithium+ (Li+) , 4.95V to 32V VDD, -40 to +125 degree Celsius, DFN-12', 'kicadSymbolki_fp_filters': 'DFN*1EP*3x3mm*P0.45mm*'}])
    newPart['name'].append('LT3652IDD')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

