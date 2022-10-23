
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_UART"
    oIndex = "ADM232A"
    hexID = "SZKINTERFACEUARTADM232A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MAX232', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADM232A', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/ADM222_232A_242.pdf', 'kicadSymbolki_keywords': 'rs232 uart transceiver line-driver', 'kicadSymbolki_description': 'Dual RS232 driver/receiver, 5V supply, 200kb/s', 'kicadSymbolki_fp_filters': 'SOIC*P1.27mm* DIP*W7.62mm* TSSOP*4.4x5mm*P0.65mm*'}])
    newPart['name'].append('ADM232A')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

