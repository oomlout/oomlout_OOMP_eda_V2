
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "74xx"
    oIndex = "74HCT4051"
    hexID = "SZK74XX74HCT451"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '74HC4051', 'kicadSymbolReference': 'U', 'kicadSymbolValue': '74HCT4051', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/cd74hct4051.pdf', 'kicadSymbolki_keywords': 'TTL Multiplexer Demultiplexer Analog', 'kicadSymbolki_description': '8-channel analog multiplexer/demultiplexer, DIP-16/SOIC-16/TSSOP-16', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SOIC*3.9x9.9mm*P1.27mm* SOIC*5.3x10.2mm*P1.27mm* TSSOP*4.4x5mm*P0.65mm*'}])
    newPart['name'].append('74xx : 74HCT4051')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

