
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "UEXT_Slave"
    hexID = "SZKCNUEXTSLAVE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'UEXT_Slave', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.olimex.com/Products/Modules/UEXT/resources/UEXT_rev_B.pdf', 'kicadSymbolki_keywords': 'UEXT, SPI, UART, I2C', 'kicadSymbolki_description': 'Universal EXTension (UEXT) is a connector layout which includes power and three serial buses: Asynchronous, I2C, and SPI', 'kicadSymbolki_fp_filters': '*Connector*:2x05*'}])
    newPart['name'].append('UEXT_Slave')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

