
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Display_Graphic"
    oIndex = "EA_eDIPTFT32-A"
    hexID = "SZKDIGRAPHICEAEDIPTFT32A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'EA_eDIPTFT32-A', 'kicadSymbolFootprint': 'Display:EA_eDIPTFT32-XXX', 'kicadSymbolDatasheet': 'http://www.lcd-module.com/fileadmin/eng/pdf/grafik/ediptft43-ae.pdf', 'kicadSymbolki_keywords': 'display TFT LCD graphic', 'kicadSymbolki_description': 'TFT graphical display, 320x240, 16 bit colour, LED backlight, 3.3V - 5V VDD, RS-232, I2C or SPI', 'kicadSymbolki_fp_filters': '*EA*eDIPTFT32*'}])
    newPart['name'].append('Display_Graphic : EA_eDIPTFT32-A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

