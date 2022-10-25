
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "TC1017R-xLT"
    hexID = "SZKREGULATORLINEARTC117RXLT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TC1017R-xLT', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-353_SC-70-5', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/21813F.pdf', 'kicadSymbolki_keywords': 'LDO Linear Voltage Regulator', 'kicadSymbolki_description': '150mA, Tiny CMOS LDO With Shutdown, SC-70-5', 'kicadSymbolki_fp_filters': 'SOT*353*'}])
    newPart['name'].append('Regulator_Linear : TC1017R-xLT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

