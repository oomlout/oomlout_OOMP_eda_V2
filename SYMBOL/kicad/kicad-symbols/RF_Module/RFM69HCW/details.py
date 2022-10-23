
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Module"
    oIndex = "RFM69HCW"
    hexID = "SZKRFMORFM69HCW"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'RFM95W-868S2', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'RFM69HCW', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.hoperf.com/data/upload/portal/20181127/5bfcb8284d838.pdf', 'kicadSymbolki_keywords': 'low power Radio ISM Transceiver Module AES encryption SPI HopeRF', 'kicadSymbolki_description': 'Low power ISM Radio Transceiver Module, SPI interface, AES encryption, 434 or 915 MHz, up to 100mW, up to 300 kb/s, SMD-16, DIP-16', 'kicadSymbolki_fp_filters': 'HOPERF*RFM9XW*'}])
    newPart['name'].append('RFM69HCW')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

