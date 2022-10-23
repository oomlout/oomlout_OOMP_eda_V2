
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_RFID"
    oIndex = "PN5120A0HN1"
    hexID = "SZKRFRFIDPN512AHN1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PN5120A0HN1', 'kicadSymbolFootprint': 'Package_DFN_QFN:HVQFN-32-1EP_5x5mm_P0.5mm_EP3.1x3.1mm', 'kicadSymbolDatasheet': 'https://www.nxp.com/docs/en/data-sheet/PN512.pdf', 'kicadSymbolki_keywords': 'PN512 RFID', 'kicadSymbolki_description': 'NFC frontend.  ISO/IEC 14443A&B, MIFARE®, FeliCa and NFC Forum tag types, HVQFN-32', 'kicadSymbolki_fp_filters': 'HVQFN*1EP*5x5mm*P0.5mm*'}])
    newPart['name'].append('PN5120A0HN1')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

