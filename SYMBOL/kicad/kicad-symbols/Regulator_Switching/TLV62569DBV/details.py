
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "TLV62569DBV"
    hexID = "SZKREGULATORSWITCHINGTLV62569DBV"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TLV62568DBV', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TLV62569DBV', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-5', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tlv62569.pdf', 'kicadSymbolki_keywords': 'Step-Down Buck DC-DC Regulator Adjustable', 'kicadSymbolki_description': 'High Efficiency Synchronous Buck Converter, Adjustable Output 0.6V-5.5V, 2A, SOT-23-5', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Regulator_Switching : TLV62569DBV')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

