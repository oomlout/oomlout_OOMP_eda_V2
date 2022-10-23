
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Module"
    oIndex = "RFM98W-433S2"
    hexID = "SZKRFMORFM98W433S2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'RFM95W-868S2', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'RFM98W-433S2', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.hoperf.com/data/upload/portal/20181127/5bfcdb5e17543.pdf', 'kicadSymbolki_keywords': 'Low power long range transceiver module', 'kicadSymbolki_description': 'Low power long range transceiver module, SPI and parallel interface, 433 MHz, spreading factor 6 to12, bandwidth 7.8 to 500kHz, -111 to -148 dBm, SMD-16, DIP-16', 'kicadSymbolki_fp_filters': 'HOPERF*RFM9XW*'}])
    newPart['name'].append('RFM98W-433S2')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

