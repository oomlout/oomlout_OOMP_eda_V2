
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "TLV62569DRL"
    hexID = "SZKREGULATORSWITCHINGTLV62569DRL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TLV62568DRL', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TLV62569DRL', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-563', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tlv62569.pdf', 'kicadSymbolki_keywords': 'Step-Down Buck DC-DC Regulator Adjustable', 'kicadSymbolki_description': 'High Efficiency Synchronous Buck Converter, Adjustable Output 0.6V-5.5V, 2A, SOT-563-6', 'kicadSymbolki_fp_filters': 'SOT*563*'}])
    newPart['name'].append('TLV62569DRL')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

