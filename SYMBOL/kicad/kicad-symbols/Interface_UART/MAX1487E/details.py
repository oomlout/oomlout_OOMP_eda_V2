
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_UART"
    oIndex = "MAX1487E"
    hexID = "SZKINTERFACEUARTMAX1487E"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MAX481E', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX1487E', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/MAX1487E-MAX491E.pdf', 'kicadSymbolki_keywords': 'Half duplex RS-485/RS-422, 2.5 Mbps, ±15kV electro-static discharge (ESD) protection, no slew-rate, no low-power shutdown, with receiver/driver enable, 128 receiver drive kapacitity, DIP-8 and SOIC-8', 'kicadSymbolki_description': 'Half duplex RS-485/RS-422, 2.5 Mbps, ±15kV electro-static discharge (ESD) protection, no slew-rate, no low-power shutdown, with receiver/driver enable, 128 receiver drive kapacitity, DIP-8 and SOIC-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('MAX1487E')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

