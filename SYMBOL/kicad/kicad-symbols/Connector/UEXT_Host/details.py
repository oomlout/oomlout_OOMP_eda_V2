
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "UEXT_Host"
    hexID = "SZKCNUEXTHOST"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'UEXT_Host', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.olimex.com/Products/Modules/UEXT/resources/UEXT_rev_B.pdf', 'kicadSymbolki_keywords': 'UEXT, SPI, UART, I2C', 'kicadSymbolki_description': 'Universal EXTension (UEXT) is a connector layout which includes power and three serial buses: Asynchronous, I2C, and SPI', 'kicadSymbolki_fp_filters': '*Connector*:2x05*'}])
    newPart['name'].append('Connector : UEXT_Host')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

