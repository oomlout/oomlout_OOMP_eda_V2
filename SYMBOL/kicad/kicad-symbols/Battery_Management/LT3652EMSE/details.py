
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Battery_Management"
    oIndex = "LT3652EMSE"
    hexID = "SZKBATMANAGEMENTLT3652EMSE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LT3652EMSE', 'kicadSymbolFootprint': 'Package_SO:MSOP-12-1EP_3x4mm_P0.65mm_EP1.65x2.85mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/3652fe.pdf', 'kicadSymbolki_keywords': 'Step-down  battery charger, Lithium Phosphate ( LiFePO4), Lead (Pb), Lithium+ (Li+) , 4.95V to 32V VDD, -40 to +125 degree Celsius, MSOP-12', 'kicadSymbolki_description': 'Step-down  battery charger, Lithium Phosphate ( LiFePO4), Lead (Pb), Lithium+ (Li+) , 4.95V to 32V VDD, -40 to +125 degree Celsius, MSOP-12', 'kicadSymbolki_fp_filters': 'MSOP*1EP*3x4mm*P0.65mm*'}])
    newPart['name'].append('LT3652EMSE')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

