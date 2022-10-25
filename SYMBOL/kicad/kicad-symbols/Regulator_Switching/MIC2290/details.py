
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "MIC2290"
    hexID = "SZKREGULATORSWITCHINGMIC229"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MIC2290', 'kicadSymbolFootprint': 'Package_DFN_QFN:Micrel_MLF-8-1EP_2x2mm_P0.5mm_EP0.8x1.3mm_ThermalVias', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/mic2290.pdf', 'kicadSymbolki_keywords': 'boost switching voltage converter regulator', 'kicadSymbolki_description': '1.2 Mhz PWM Boost Regulator with Internal Schotty Diode, MLF-8', 'kicadSymbolki_fp_filters': 'Micrel*MLF*8*2x2mm*'}])
    newPart['name'].append('Regulator_Switching : MIC2290')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

