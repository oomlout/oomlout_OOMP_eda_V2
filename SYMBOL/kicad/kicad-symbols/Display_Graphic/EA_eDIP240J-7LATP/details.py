
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Display_Graphic"
    oIndex = "EA_eDIP240J-7LATP"
    hexID = "SZKDIGRAPHICEAEDIP24J7LATP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'EA_eDIP240B-7LW', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'EA_eDIP240J-7LATP', 'kicadSymbolFootprint': 'Display:EA_eDIP240-XXX', 'kicadSymbolDatasheet': 'http://www.lcd-module.com/fileadmin/eng/pdf/grafik/edip240-7e.pdf', 'kicadSymbolki_keywords': 'display LCD graphic', 'kicadSymbolki_description': 'LCD graphical display with amber LED background and touch panel blue positive mode FSTN, 240x128, +5V VDD, RS-232, I2C or SPI', 'kicadSymbolki_fp_filters': '*EA*eDIP240*'}])
    newPart['name'].append('EA_eDIP240J-7LATP')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

