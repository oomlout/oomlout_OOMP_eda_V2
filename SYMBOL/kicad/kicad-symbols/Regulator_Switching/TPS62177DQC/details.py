
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "TPS62177DQC"
    hexID = "SZKREGULATORSWITCHINGTPS62177DQC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPS62177DQC', 'kicadSymbolFootprint': 'Package_SON:WSON-10-1EP_2x3mm_P0.5mm_EP0.84x2.4mm_ThermalVias', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tps62177.pdf', 'kicadSymbolki_keywords': 'step-down dc-dc buck regulator', 'kicadSymbolki_description': '500mA Step-Down Converter with Sleep Mode, fixed 3.3V Output Voltage, 4.75-28V input voltage, WSON-10', 'kicadSymbolki_fp_filters': 'WSON*EP*2x3mm*P0.5mm*'}])
    newPart['name'].append('Regulator_Switching : TPS62177DQC')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

