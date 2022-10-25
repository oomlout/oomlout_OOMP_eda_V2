
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_Switch"
    oIndex = "CD4097B"
    hexID = "SZKANALOGSWITCHCD497B"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CD4097B', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/cd4097b.pdf', 'kicadSymbolki_keywords': 'analog switch selector multiplexer', 'kicadSymbolki_description': 'CMOS double 8-channel analog multiplexer/demultiplexer, TSSOP-24/DIP-24/SOIC-24', 'kicadSymbolki_fp_filters': 'TSSOP*4.4x7.8mm*P0.65mm* SOIC*7.5*15.4*1.27mm* SO*5.3x15.0mm*P1.27mm* DIP*15.24mm*'}])
    newPart['name'].append('Analog_Switch : CD4097B')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

