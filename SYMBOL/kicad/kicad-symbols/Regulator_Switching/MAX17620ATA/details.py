
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "MAX17620ATA"
    hexID = "SZKREGULATORSWITCHINGMAX1762ATA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX17620ATA', 'kicadSymbolFootprint': 'Package_DFN_QFN:TDFN-8-1EP_2x2mm_P0.5mm_EP0.8x1.2mm', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/MAX17620.pdf', 'kicadSymbolki_keywords': 'switching-regulator', 'kicadSymbolki_description': '2.7-5.5V, 600mA, Synchronous Step-Down DC-DC Converter with Integrated MOSFETs, DFN-8', 'kicadSymbolki_fp_filters': 'TDFN*1EP*2x2mm*P0.5mm*'}])
    newPart['name'].append('Regulator_Switching : MAX17620ATA')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

