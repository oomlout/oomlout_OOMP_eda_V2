
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "MAX17572"
    hexID = "SZKREGULATORSWITCHINGMAX17572"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX17572', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-12-1EP_3x3mm_P0.5mm_EP2.05x2.86mm', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/MAX17572.pdf', 'kicadSymbolki_keywords': 'Step-down dc-dc switching regulator', 'kicadSymbolki_description': '4.5V–60V, 1A, High-Efficiency, Synchronous Step-Down DC-DC Converter with Internal Compensation, DFN-12', 'kicadSymbolki_fp_filters': 'DFN*1EP*3x3mm*P0.5mm*'}])
    newPart['name'].append('Regulator_Switching : MAX17572')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

