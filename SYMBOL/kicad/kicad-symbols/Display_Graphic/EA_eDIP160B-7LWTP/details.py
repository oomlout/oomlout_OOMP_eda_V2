
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Display_Graphic"
    oIndex = "EA_eDIP160B-7LWTP"
    hexID = "SZKDIGRAPHICEAEDIP16B7LWTP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'EA_eDIP160B-7LW', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'EA_eDIP160B-7LWTP', 'kicadSymbolFootprint': 'Display:EA_eDIP160-XXX', 'kicadSymbolDatasheet': 'http://www.lcd-module.com/fileadmin/eng/pdf/grafik/edip160-7e.pdf', 'kicadSymbolki_keywords': 'display LCD graphic', 'kicadSymbolki_description': 'LCD-graphical display 160x104 with LED backlight and touch panel, blue negative, 3.3V - 5V VDD, RS-232, I2C or SPI', 'kicadSymbolki_fp_filters': '*EA*eDIP160*'}])
    newPart['name'].append('EA_eDIP160B-7LWTP')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

