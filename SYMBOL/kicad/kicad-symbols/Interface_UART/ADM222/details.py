
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_UART"
    oIndex = "ADM222"
    hexID = "SZKINTERFACEUARTADM222"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LT1080', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADM222', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/ADM222_232A_242.pdf', 'kicadSymbolki_keywords': 'rs232 uart transceiver', 'kicadSymbolki_description': 'Dual RS232 driver/receiver, 5V supply, 200kb/s', 'kicadSymbolki_fp_filters': 'SO* DIP*W7.62mm*'}])
    newPart['name'].append('ADM222')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

