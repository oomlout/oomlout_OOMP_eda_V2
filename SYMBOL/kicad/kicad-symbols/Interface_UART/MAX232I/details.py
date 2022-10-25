
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_UART"
    oIndex = "MAX232I"
    hexID = "SZKINTERFACEUARTMAX232I"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MAX232', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX232I', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/max232.pdf', 'kicadSymbolki_keywords': 'rs232 uart transceiver line-driver', 'kicadSymbolki_description': 'Dual RS232 driver/receiver, 5V supply, 120kb/s, -40C-80C', 'kicadSymbolki_fp_filters': 'SOIC*P1.27mm* DIP*W7.62mm* TSSOP*4.4x5mm*P0.65mm*'}])
    newPart['name'].append('Interface_UART : MAX232I')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

