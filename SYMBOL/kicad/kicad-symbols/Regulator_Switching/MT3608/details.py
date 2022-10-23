
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "MT3608"
    hexID = "SZKREGULATORSWITCHINGMT368"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MT3608', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-6', 'kicadSymbolDatasheet': 'https://www.olimex.com/Products/Breadboarding/BB-PWR-3608/resources/MT3608.pdf', 'kicadSymbolki_keywords': 'Step-Up Boost DC-DC Regulator Adjustable', 'kicadSymbolki_description': 'High Efficiency 1.2MHz 2A Step Up Converter, 2-24V Vin, 28V Vout, 4A current limit, 1.2MHz, SOT23-6', 'kicadSymbolki_fp_filters': 'SOT*23*'}])
    newPart['name'].append('MT3608')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

