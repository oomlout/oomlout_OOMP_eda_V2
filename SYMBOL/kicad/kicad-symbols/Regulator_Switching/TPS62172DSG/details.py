
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "TPS62172DSG"
    hexID = "SZKREGULATORSWITCHINGTPS62172DSG"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TPS62170DSG', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPS62172DSG', 'kicadSymbolFootprint': 'Package_SON:WSON-8-1EP_2x2mm_P0.5mm_EP0.9x1.6mm_ThermalVias', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tps62170.pdf', 'kicadSymbolki_keywords': 'step-down dc-dc buck regulator', 'kicadSymbolki_description': '500mA Step-Down Converter with DCS-Control, fixed 3.3V output, 3-17V input voltage, WSON-8', 'kicadSymbolki_fp_filters': 'WSON*EP*2x2mm*P0.5mm*'}])
    newPart['name'].append('Regulator_Switching : TPS62172DSG')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

