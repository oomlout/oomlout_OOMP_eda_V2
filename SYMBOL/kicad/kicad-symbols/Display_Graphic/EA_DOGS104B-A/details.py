
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Display_Graphic"
    oIndex = "EA_DOGS104B-A"
    hexID = "SZKDIGRAPHICEADOGS14BA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'EA_DOGS104B-A', 'kicadSymbolFootprint': 'Display:EA_DOGS104X-A', 'kicadSymbolDatasheet': 'http://www.lcd-module.com/fileadmin/eng/pdf/doma/dogs104e.pdf', 'kicadSymbolki_keywords': 'display LCD graphic', 'kicadSymbolki_description': 'LCD 4x10 character display blue transmissive background, +3.3V VDD, I2C or SPI', 'kicadSymbolki_fp_filters': '*EA*DOGS104*'}])
    newPart['name'].append('Display_Graphic : EA_DOGS104B-A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

