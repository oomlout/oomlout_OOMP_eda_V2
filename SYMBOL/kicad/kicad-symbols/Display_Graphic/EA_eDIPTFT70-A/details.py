
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Display_Graphic"
    oIndex = "EA_eDIPTFT70-A"
    hexID = "SZKDIGRAPHICEAEDIPTFT7A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'EA_eDIPTFT70-A', 'kicadSymbolFootprint': 'Display:EA_eDIPTFT70-XXX', 'kicadSymbolDatasheet': 'http://www.lcd-module.com/fileadmin/eng/pdf/grafik/ediptft70-ae.pdf', 'kicadSymbolki_keywords': 'display TFT LCD graphic', 'kicadSymbolki_description': 'TFT-graphical display with LED background, 800x480, 16-bit colours, +5V VDD, RS-232, I2C or SPI', 'kicadSymbolki_fp_filters': '*EA*eDIPTFT70*XXX*'}])
    newPart['name'].append('EA_eDIPTFT70-A')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

