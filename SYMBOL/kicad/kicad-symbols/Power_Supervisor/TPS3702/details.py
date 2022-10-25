
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Supervisor"
    oIndex = "TPS3702"
    hexID = "SZKPOWERSUPERVISORTPS372"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPS3702', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-6', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tps3702.pdf', 'kicadSymbolki_keywords': 'protection overvoltage unvervoltage monitor', 'kicadSymbolki_description': 'High-Accuracy, Overvoltage and Undervoltage Monitor, SOT-23-6', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Power_Supervisor : TPS3702')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

