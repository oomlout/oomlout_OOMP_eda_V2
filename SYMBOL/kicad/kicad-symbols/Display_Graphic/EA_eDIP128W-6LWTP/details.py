
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Display_Graphic"
    oIndex = "EA_eDIP128W-6LWTP"
    hexID = "SZKDIGRAPHICEAEDIP128W6LWTP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'EA_eDIP128B-6LW', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'EA_eDIP128W-6LWTP', 'kicadSymbolFootprint': 'Display:EA-eDIP128B-XXX', 'kicadSymbolDatasheet': 'http://www.lcd-module.com/fileadmin/eng/pdf/grafik/edip128-6e.pdf', 'kicadSymbolki_keywords': 'display LCD graphic', 'kicadSymbolki_description': 'LCD-graphical display with LED backlight and touch panel positive mode FSTN, 3.3V - 5V VDD, RS-232. I2C or SPI', 'kicadSymbolki_fp_filters': '*EA*eDIP128B*'}])
    newPart['name'].append('Display_Graphic : EA_eDIP128W-6LWTP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

