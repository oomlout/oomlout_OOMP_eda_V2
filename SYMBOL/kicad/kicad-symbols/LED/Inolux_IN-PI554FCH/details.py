
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "LED"
    oIndex = "Inolux_IN-PI554FCH"
    hexID = "SZKLINOLUXINPI554FCH"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'Inolux_IN-PI554FCH', 'kicadSymbolFootprint': 'LED_SMD:LED_Inolux_IN-PI554FCH_PLCC4_5.0x5.0mm_P3.2mm', 'kicadSymbolDatasheet': 'http://www.inolux-corp.com/datasheet/SMDLED/Addressable%20LED/IN-PI554FCH.pdf', 'kicadSymbolki_keywords': 'RGB LED NeoPixel addressable', 'kicadSymbolki_description': '5050 RGB LED 4-Pin with integrated IC', 'kicadSymbolki_fp_filters': 'LED*IN-PI554FCH*PLCC*5.0x5.0mm*P3.2mm*'}])
    newPart['name'].append('LED : Inolux_IN-PI554FCH')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

