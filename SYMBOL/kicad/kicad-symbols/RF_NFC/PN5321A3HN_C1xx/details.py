
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_NFC"
    oIndex = "PN5321A3HN_C1xx"
    hexID = "SZKRFNFCPN5321A3HNC1XX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PN5321A3HN_C1xx', 'kicadSymbolFootprint': 'Package_DFN_QFN:HVQFN-40-1EP_6x6mm_P0.5mm_EP4.1x4.1mm', 'kicadSymbolDatasheet': 'https://www.nxp.com/docs/en/nxp/data-sheets/PN532_C1.pdf', 'kicadSymbolki_keywords': 'NFC', 'kicadSymbolki_description': 'Near Field Communication (NFC) controller, QFN-40', 'kicadSymbolki_fp_filters': 'HVQFN*1EP*6x6mm*P0.5mm*'}])
    newPart['name'].append('RF_NFC : PN5321A3HN_C1xx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

