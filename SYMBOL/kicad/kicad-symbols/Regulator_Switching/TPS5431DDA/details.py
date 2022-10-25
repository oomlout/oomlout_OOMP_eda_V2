
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "TPS5431DDA"
    hexID = "SZKREGULATORSWITCHINGTPS5431DDA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TPS5430DDA', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPS5431DDA', 'kicadSymbolFootprint': 'Package_SO:TI_SO-PowerPAD-8_ThermalVias', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tps5430.pdf', 'kicadSymbolki_keywords': 'Step-Down DC-DC Switching Regulator', 'kicadSymbolki_description': '3A, Step Down Swift Converter, Adjustable Output Voltage, 5.5-23V Input Voltage, PowerSO-8', 'kicadSymbolki_fp_filters': 'TI*SO*PowerPAD*ThermalVias*'}])
    newPart['name'].append('Regulator_Switching : TPS5431DDA')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

