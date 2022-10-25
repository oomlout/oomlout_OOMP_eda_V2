
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_Display"
    oIndex = "CR2013-MI2120"
    hexID = "SZKDRIVERDICR213MI212"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CR2013-MI2120', 'kicadSymbolFootprint': 'Display:CR2013-MI2120', 'kicadSymbolDatasheet': 'http://pan.baidu.com/s/11Y990', 'kicadSymbolki_keywords': 'driver display', 'kicadSymbolki_description': 'ILI9341 controller, SPI TFT LCD Display, 9-pin breakout PCB, 4-pin SD card interface, 5V/3.3V', 'kicadSymbolki_fp_filters': '*CR2013*MI2120*'}])
    newPart['name'].append('Driver_Display : CR2013-MI2120')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

