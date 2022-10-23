
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Module"
    oIndex = "RFM95W-868S2"
    hexID = "SZKRFMORFM95W868S2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'RFM95W-868S2', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.hoperf.com/data/upload/portal/20181127/5bfcbea20e9ef.pdf', 'kicadSymbolki_keywords': 'Low power long range transceiver module', 'kicadSymbolki_description': 'Low power long range transceiver module, SPI and parallel interface, 868 MHz, spreading factor 6 to12, bandwidth 7.8 to 500kHz, -111 to -148 dBm, SMD-16, DIP-16', 'kicadSymbolki_fp_filters': 'HOPERF*RFM9XW*'}])
    newPart['name'].append('RFM95W-868S2')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

