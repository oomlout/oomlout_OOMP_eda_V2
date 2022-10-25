
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "TPS62150A"
    hexID = "SZKREGULATORSWITCHINGTPS6215A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TPS62130', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPS62150A', 'kicadSymbolFootprint': 'Package_DFN_QFN:VQFN-16-1EP_3x3mm_P0.5mm_EP1.68x1.68mm_ThermalVias', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/TPS62150.pdf', 'kicadSymbolki_keywords': 'step-down dcdc', 'kicadSymbolki_description': '1A Step-Down Converter with DCS-Control, Adjustable Output Voltage, 3-17V Input Voltage, PG=LOW in Power-Down, QFN-16', 'kicadSymbolki_fp_filters': 'VQFN*1EP*3x3mm*P0.5mm*'}])
    newPart['name'].append('Regulator_Switching : TPS62150A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

