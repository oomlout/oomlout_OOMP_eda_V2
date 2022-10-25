
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "TPS62143"
    hexID = "SZKREGULATORSWITCHINGTPS62143"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TPS62130', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPS62143', 'kicadSymbolFootprint': 'Package_DFN_QFN:VQFN-16-1EP_3x3mm_P0.5mm_EP1.68x1.68mm_ThermalVias', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/TPS62140.pdf', 'kicadSymbolki_keywords': 'step-down dcdc', 'kicadSymbolki_description': '2A Step-Down Converter with DCS-Control, Fixed 5.0V Output Voltage, 3-17V Input Voltage, QFN-16', 'kicadSymbolki_fp_filters': 'VQFN*1EP*3x3mm*P0.5mm*'}])
    newPart['name'].append('Regulator_Switching : TPS62143')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

