
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Reference_Voltage"
    oIndex = "LM4030-4.096"
    hexID = "SZKREFERENCEVOLTAGELM43496"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM4030-4.096', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-5', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm4030.pdf', 'kicadSymbolki_keywords': 'diode device voltage reference shunt', 'kicadSymbolki_description': '4.096V Ultra-High Precision Shunt Voltage Reference, SOT-23-5', 'kicadSymbolki_fp_filters': 'SOT?23?5*'}])
    newPart['name'].append('Reference_Voltage : LM4030-4.096')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

