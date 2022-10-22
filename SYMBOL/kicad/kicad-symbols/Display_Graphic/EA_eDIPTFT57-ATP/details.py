
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Display_Graphic"
    oIndex = "EA_eDIPTFT57-ATP"
    hexID = "SZKDIGRAPHICEAEDIPTFT57ATP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'EA_eDIPTFT57-A', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'EA_eDIPTFT57-ATP', 'kicadSymbolFootprint': 'Display:EA_eDIPTFT57-XXX', 'kicadSymbolDatasheet': 'http://www.lcd-module.com/fileadmin/eng/pdf/grafik/ediptft57-ae.pdf', 'kicadSymbolki_keywords': 'display TFT LCD graphic', 'kicadSymbolki_description': 'TFT-graphical display with touch panel. 640x480, LED backlight, +5V VDD, RS-232, I2C or SPI', 'kicadSymbolki_fp_filters': '*EA*eDIPTFT57*'}])
    newPart['name'].append('EA_eDIPTFT57-ATP')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

