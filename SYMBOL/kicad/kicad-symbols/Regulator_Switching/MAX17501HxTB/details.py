
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "MAX17501HxTB"
    hexID = "SZKREGULATORSWITCHINGMAX1751HXTB"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MAX17501GxTB', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX17501HxTB', 'kicadSymbolFootprint': 'Package_DFN_QFN:TDFN-10-1EP_2x3mm_P0.5mm_EP0.9x2mm', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/MAX17501.pdf', 'kicadSymbolki_keywords': 'Step-down dc-dc switching regulator', 'kicadSymbolki_description': '4.5V–60Vin, 500mA, High-Efficiency, Adjustable Synchronous Step-Down DC-DC Converter, 300KHz, DFN-10', 'kicadSymbolki_fp_filters': 'TDFN*1EP*2x3mm*P0.5mm*'}])
    newPart['name'].append('Regulator_Switching : MAX17501HxTB')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

