
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_UART"
    oIndex = "ADM2687E"
    hexID = "SZKINTERFACEUARTADM2687E"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ADM2682E', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADM2687E', 'kicadSymbolFootprint': 'Package_SO:SOIC-16W_7.5x12.8mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/ADM2682E_2687E.pdf', 'kicadSymbolki_keywords': 'RS485 Transceiver, RS422 Transceiver, Isopower', 'kicadSymbolki_description': 'Isolated RS485/RS422 Transceiver, Integrated Isolated DC-DC Converter, 500kbps, SOIC-16W', 'kicadSymbolki_fp_filters': 'SOIC*7.5x12.8mm*P1.27mm*'}])
    newPart['name'].append('Interface_UART : ADM2687E')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

