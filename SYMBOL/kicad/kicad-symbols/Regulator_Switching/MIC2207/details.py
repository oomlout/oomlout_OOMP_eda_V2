
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "MIC2207"
    hexID = "SZKREGULATORSWITCHINGMIC227"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MIC2207', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-12-1EP_3x3mm_P0.5mm_EP1.7x2.4mm', 'kicadSymbolDatasheet': 'https://ww1.microchip.com/downloads/aemDocuments/documents/APID/ProductDocuments/DataSheets/MIC2207-2MHz-3A-PWM-Buck-Regulator-DS20006470A.pdf', 'kicadSymbolki_keywords': 'adjustable switching regulator', 'kicadSymbolki_description': '3A 2MHz Non-Synchronous Buck Regulator, DFN-12', 'kicadSymbolki_fp_filters': 'DFN*1EP*3x3mm*P0.5mm*'}])
    newPart['name'].append('Regulator_Switching : MIC2207')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

