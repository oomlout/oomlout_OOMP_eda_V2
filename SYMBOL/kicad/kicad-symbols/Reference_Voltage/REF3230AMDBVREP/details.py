
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Reference_Voltage"
    oIndex = "REF3230AMDBVREP"
    hexID = "SZKREFERENCEVOLTAGEREF323AMDBVREP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'REF3212AMDBVREP', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'REF3230AMDBVREP', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-6', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/ref3240-ep.pdf', 'kicadSymbolki_keywords': 'Micropower Precision Voltage Reference 3V', 'kicadSymbolki_description': '3V 100μA Micropower Precision Voltage Reference, SOT-23-6', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Reference_Voltage : REF3230AMDBVREP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

