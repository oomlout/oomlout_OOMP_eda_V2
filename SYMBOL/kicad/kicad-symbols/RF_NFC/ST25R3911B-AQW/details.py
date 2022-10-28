
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_NFC"
    oIndex = "ST25R3911B-AQW"
    hexID = "SZKRFNFCST25R3911BAQW"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ST25R3911B-AQW', 'kicadSymbolFootprint': 'Package_DFN_QFN:VQFN-32-1EP_5x5mm_P0.5mm_EP3.5x3.5mm_ThermalVias', 'kicadSymbolDatasheet': 'https://www.st.com/resource/en/datasheet/st25r3911b.pdf', 'kicadSymbolki_keywords': 'NFC', 'kicadSymbolki_description': 'High performance HR reader/NFC initiator with 1.4W supporting VHBR and AAT, VFQFPN32', 'kicadSymbolki_fp_filters': '*QFN*1EP*5x5mm*P0.5mm*'}])
    newPart['name'].append('RF_NFC : ST25R3911B-AQW')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

