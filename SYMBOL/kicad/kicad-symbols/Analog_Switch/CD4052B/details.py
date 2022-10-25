
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_Switch"
    oIndex = "CD4052B"
    hexID = "SZKANALOGSWITCHCD452B"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CD4052B', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/cd4052b.pdf', 'kicadSymbolki_keywords': 'analog switch selector multiplexer', 'kicadSymbolki_description': 'CMOS double 4-channel analog multiplexer/demultiplexer, TSSOP-16/DIP-16/SOIC-16', 'kicadSymbolki_fp_filters': 'TSSOP*4.4x5mm*P0.65mm* DIP*W7.62* SOIC*3.9x9.9mm*P1.27mm* SO*5.3x10.2mm*P1.27mm*'}])
    newPart['name'].append('Analog_Switch : CD4052B')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

