
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Display_Graphic"
    oIndex = "EA_eDIPTFT43-ATP"
    hexID = "SZKDIGRAPHICEAEDIPTFT43ATP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'EA_eDIPTFT43-A', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'EA_eDIPTFT43-ATP', 'kicadSymbolFootprint': 'Display:EA_eDIPTFT43-XXX', 'kicadSymbolDatasheet': 'http://www.lcd-module.com/fileadmin/eng/pdf/grafik/ediptft43-ae.pdf', 'kicadSymbolki_keywords': 'display TFT LCD graphic', 'kicadSymbolki_description': 'TFT graphical display with resistive touch panel, 480x272, 16 bit colour, LED backlight, 5V VDD, RS-232, I2C or SPI', 'kicadSymbolki_fp_filters': 'EA*eDIPTFT43*XXX*'}])
    newPart['name'].append('EA_eDIPTFT43-ATP')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

