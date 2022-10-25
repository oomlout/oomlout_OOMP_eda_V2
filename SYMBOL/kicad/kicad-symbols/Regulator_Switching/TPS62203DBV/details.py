
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "TPS62203DBV"
    hexID = "SZKREGULATORSWITCHINGTPS6223DBV"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TPS62200DBV', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPS62203DBV', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-5', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tps62201.pdf', 'kicadSymbolki_keywords': 'Step-Down DC-DC Converter', 'kicadSymbolki_description': '300mA High-Efficiency Step-Down DC-DC Converter, fixed 3.3V output voltage, 2.5-6V input voltage, SOT-23-5', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Regulator_Switching : TPS62203DBV')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

