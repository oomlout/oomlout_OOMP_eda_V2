
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "TPS61040DDC"
    hexID = "SZKREGULATORSWITCHINGTPS614DDC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TPS61041DDC', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPS61040DDC', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-5', 'kicadSymbolDatasheet': 'https://www.ti.com/lit/ds/symlink/tps61040.pdf', 'kicadSymbolki_keywords': 'Step-Up Boost DC-DC Regulator Adjustable', 'kicadSymbolki_description': 'Synchronous Boost Regulator, Adjustable Output up to 28V, 400 mA Switch Current Limit, SOT-23-5', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('TPS61040DDC')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

