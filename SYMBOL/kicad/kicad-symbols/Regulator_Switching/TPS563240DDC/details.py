
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "TPS563240DDC"
    hexID = "SZKREGULATORSWITCHINGTPS56324DDC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TPS562200', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPS563240DDC', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-6', 'kicadSymbolDatasheet': 'www.ti.com/lit/ds/symlink/tps563240.pdf', 'kicadSymbolki_keywords': 'step-down dcdc voltage regulator', 'kicadSymbolki_description': '3A Synchronous Step-Down Voltage Regulator, Adjustable Output Voltage, 4.5-17V Input Voltage, SOT-23-6', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('TPS563240DDC')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

