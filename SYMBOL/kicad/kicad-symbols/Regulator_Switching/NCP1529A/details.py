
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "NCP1529A"
    hexID = "SZKREGULATORSWITCHINGNCP1529A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TLV62568DBV', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'NCP1529A', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-5', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/NCP1529-D.PDF', 'kicadSymbolki_keywords': 'Step-Down Buck DC-DC Regulator Adjustable', 'kicadSymbolki_description': '1.7MHz, 1A, High Efficiency, Low Ripple, Adjustable Output Voltage Step-down Converter, SOT-23-5', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('NCP1529A')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

