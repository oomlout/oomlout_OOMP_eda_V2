
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Display_Graphic"
    oIndex = "EA_eDIPTFT70-ATC"
    hexID = "SZKDIGRAPHICEAEDIPTFT7ATC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'EA_eDIPTFT70-ATC', 'kicadSymbolFootprint': 'Display:EA_eDIPTFT70-ATC', 'kicadSymbolDatasheet': 'http://www.lcd-module.com/fileadmin/eng/pdf/grafik/ediptft70-ae.pdf', 'kicadSymbolki_keywords': 'display TFT LCD graphic', 'kicadSymbolki_description': 'TFT-graphical display with LED background and capacitive touch panel, 800x480, 16-bit colours, +5V VDD, RS-232, I2C or SPI', 'kicadSymbolki_fp_filters': '*EA*eDIPTFT70*ATC*'}])
    newPart['name'].append('Display_Graphic : EA_eDIPTFT70-ATC')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

