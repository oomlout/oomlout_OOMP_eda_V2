
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Reference_Voltage"
    oIndex = "REF3030"
    hexID = "SZKREFERENCEVOLTAGEREF33"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'REF3012', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'REF3030', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/ref3033.pdf', 'kicadSymbolki_keywords': 'voltage reference', 'kicadSymbolki_description': '3.0V 50-ppm/°C Max, 50-μA, CMOS Voltage Reference, SOT-23-3', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Reference_Voltage : REF3030')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

