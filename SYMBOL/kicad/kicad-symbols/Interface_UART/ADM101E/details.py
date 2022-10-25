
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_UART"
    oIndex = "ADM101E"
    hexID = "SZKINTERFACEUARTADM11E"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADM101E', 'kicadSymbolFootprint': 'Package_SO:MSOP-10_3x3mm_P0.5mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/ADM101E.pdf', 'kicadSymbolki_keywords': 'rs232 uart transceiver line-driver', 'kicadSymbolki_description': 'Single RS232 driver/receiver, 5V supply, 460kb/s', 'kicadSymbolki_fp_filters': 'MSOP*'}])
    newPart['name'].append('Interface_UART : ADM101E')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

