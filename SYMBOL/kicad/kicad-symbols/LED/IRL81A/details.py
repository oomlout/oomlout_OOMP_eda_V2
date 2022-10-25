
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "LED"
    oIndex = "IRL81A"
    hexID = "SZKLIRL81A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'IRL81A', 'kicadSymbolFootprint': 'LED_THT:LED_SideEmitter_Rectangular_W4.5mm_H1.6mm', 'kicadSymbolDatasheet': 'http://www.osram-os.com/Graphics/XPic0/00203825_0.pdf', 'kicadSymbolki_keywords': 'IR LED', 'kicadSymbolki_description': '850nm High Power Infrared Emitter, Side-Emitter package', 'kicadSymbolki_fp_filters': 'LED*SideEmitter*Rectangular*W4.5mm*H1.6mm*'}])
    newPart['name'].append('LED : IRL81A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

