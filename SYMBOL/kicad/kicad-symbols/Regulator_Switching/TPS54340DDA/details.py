
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "TPS54340DDA"
    hexID = "SZKREGULATORSWITCHINGTPS5434DDA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TPS54360DDA', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPS54340DDA', 'kicadSymbolFootprint': 'Package_SO:TI_SO-PowerPAD-8_ThermalVias', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tps54340.pdf', 'kicadSymbolki_keywords': 'Step-Down DC-DC Switching Regulator High Voltage High Frequency', 'kicadSymbolki_description': '3.5A, Step Down DC-DC Converter with Eco-mode, 4.5-42V Input Voltage, PowerSO-8', 'kicadSymbolki_fp_filters': 'TI*SO*PowerPAD*ThermalVias*'}])
    newPart['name'].append('Regulator_Switching : TPS54340DDA')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

