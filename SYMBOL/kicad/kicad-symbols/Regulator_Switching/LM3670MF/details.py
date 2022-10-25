
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LM3670MF"
    hexID = "SZKREGULATORSWITCHINGLM367MF"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ADP2108AUJ-1.0', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM3670MF', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TSOT-23-5', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm3670.pdf', 'kicadSymbolki_keywords': 'DC-DC buck converter step down voltage regulator', 'kicadSymbolki_description': 'Miniature Step-Down DC-DC Converter for Ultralow Voltage Circuits, 2.5V < Vin < 5.5V, adjustable output voltage, SOT-23-5', 'kicadSymbolki_fp_filters': 'TSOT?23*'}])
    newPart['name'].append('Regulator_Switching : LM3670MF')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

