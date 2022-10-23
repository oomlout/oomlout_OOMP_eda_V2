
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_UART"
    oIndex = "MAX491E"
    hexID = "SZKINTERFACEUARTMAX491E"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MAX489E', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX491E', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/MAX1487E-MAX491E.pdf', 'kicadSymbolki_keywords': 'Full duplex RS-485/RS-422, 2.5 Mbps, ±15kV electro-static discharge (ESD) protection, no slew-rate limited, no low-power shutdown, with receiver/driver enable, 32 receiver drive kapacitity, 0 to +70 degree Celsius, DIP-14 and SOIC-14', 'kicadSymbolki_description': 'Full duplex RS-485/RS-422, 2.5 Mbps, ±15kV electro-static discharge (ESD) protection, no slew-rate limited, no low-power shutdown, with receiver/driver enable, 32 receiver drive kapacitity, 0 to +70 degree Celsius, DIP-14 and SOIC-14', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SOIC*3.9x8.7mm*P1.27mm*'}])
    newPart['name'].append('MAX491E')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

