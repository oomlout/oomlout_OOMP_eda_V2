
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "MIC2025-2YMM"
    hexID = "SZKPOWERMANAGEMENTMIC2252Y"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MIC2025-1YMM', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MIC2025-2YMM', 'kicadSymbolFootprint': 'Package_SO:MSOP-8_3x3mm_P0.65mm', 'kicadSymbolDatasheet': 'https://ww1.microchip.com/downloads/en/DeviceDoc/MIC2025-2075-Single-Channel-Power-Distribution-Switch-DS20006030A.pdf', 'kicadSymbolki_keywords': 'mosfet distribution', 'kicadSymbolki_description': 'Single-channel, high side, power distribution switch, 2.7V-5.5V, Active Low Output, MSOP-8', 'kicadSymbolki_fp_filters': 'MSOP*3x3mm*P0.65mm*'}])
    newPart['name'].append('Power_Management : MIC2025-2YMM')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

