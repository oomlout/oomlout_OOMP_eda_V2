
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "74xx"
    oIndex = "MC74LCX16245DT"
    hexID = "SZK74XXMC74LCX16245DT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MC74LCX16245DT', 'kicadSymbolFootprint': 'Package_SO:TSSOP-48_6.1x12.5mm_P0.5mm', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pdf/datasheet/mc74lcx16245-d.pdf', 'kicadSymbolki_keywords': 'transceiver', 'kicadSymbolki_description': 'Low Voltage 16-Bit Bidirectional Transceiver with 5V Tolerant Inputs and Outputs, TSSOP-48', 'kicadSymbolki_fp_filters': 'TSSOP*6.1x12.5mm*P0.5mm*'}])
    newPart['name'].append('74xx : MC74LCX16245DT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

