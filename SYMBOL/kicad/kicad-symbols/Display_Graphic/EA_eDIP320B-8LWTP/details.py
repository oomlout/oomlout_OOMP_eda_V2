
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Display_Graphic"
    oIndex = "EA_eDIP320B-8LWTP"
    hexID = "SZKDIGRAPHICEAEDIP32B8LWTP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'EA_eDIP320B-8LW', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'EA_eDIP320B-8LWTP', 'kicadSymbolFootprint': 'Display:EA_eDIP320X-XXX', 'kicadSymbolDatasheet': 'http://www.lcd-module.com/fileadmin/eng/pdf/grafik/edip320-8e.pdf', 'kicadSymbolki_keywords': 'display LCD graphic', 'kicadSymbolki_description': 'LCD graphical display 320x240 white LED backlight with touch panel blue negative, +5V VDD, RS-232, I2C or SPI', 'kicadSymbolki_fp_filters': '*EA*eDIP320*'}])
    newPart['name'].append('Display_Graphic : EA_eDIP320B-8LWTP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

