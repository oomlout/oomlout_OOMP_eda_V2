
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Reference_Voltage"
    oIndex = "LM4040DBZ-4.1"
    hexID = "SZKREFERENCEVOLTAGELM44DBZ41"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM4040DBZ-2.0', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM4040DBZ-4.1', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm4040-n.pdf', 'kicadSymbolki_keywords': 'diode device voltage reference shunt', 'kicadSymbolki_description': '4.096V Precision Micropower Shunt Voltage Reference, SOT-23', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Reference_Voltage : LM4040DBZ-4.1')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

