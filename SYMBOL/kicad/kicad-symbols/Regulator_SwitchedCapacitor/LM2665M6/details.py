
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_SwitchedCapacitor"
    oIndex = "LM2665M6"
    hexID = "SZKREGULATORSWITCHEDCAPACITORLM2665M6"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM2665M6', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-6', 'kicadSymbolDatasheet': 'https://www.ti.com/lit/ds/symlink/lm2665.pdf', 'kicadSymbolki_keywords': 'switched capacitor voltage converter doubler splitter', 'kicadSymbolki_description': 'Switched Capacitor Voltage Converter, Doubles or Splits Input Supply Voltage (2.5 V to 5.5 V or 1.8 V to 11 V), 40 mA, SOT-23-6', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Regulator_SwitchedCapacitor : LM2665M6')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

