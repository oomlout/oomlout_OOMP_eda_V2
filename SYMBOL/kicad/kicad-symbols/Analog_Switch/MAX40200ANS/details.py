
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_Switch"
    oIndex = "MAX40200ANS"
    hexID = "SZKANALOGSWITCHMAX42ANS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX40200ANS', 'kicadSymbolFootprint': 'Package_BGA:WLP-4_0.73x0.73mm_Layout2x2_P0.35mm_Ball0.22mm_Pad0.2mm_NSMD', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/MAX40200.pdf', 'kicadSymbolki_keywords': 'current switch', 'kicadSymbolki_description': 'Ideal Diode, Ultra-Low Voltage Drop, 1.5-5.5V, 1A, WLP-4', 'kicadSymbolki_fp_filters': 'WLP*0.73x0.73mm*Layout2x2*P0.35mm*'}])
    newPart['name'].append('Analog_Switch : MAX40200ANS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

