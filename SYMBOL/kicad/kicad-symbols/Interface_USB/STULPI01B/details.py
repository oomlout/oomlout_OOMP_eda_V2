
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_USB"
    oIndex = "STULPI01B"
    hexID = "SZKINTERFACEUSTULPI1B"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'STULPI01A', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STULPI01B', 'kicadSymbolFootprint': 'Package_BGA:ST_uTFBGA-36_3.6x3.6mm_Layout6x6_P0.5mm', 'kicadSymbolDatasheet': 'https://www.st.com/resource/en/datasheet/stulpi01b.pdf', 'kicadSymbolki_keywords': 'USB OTG HS PHY ULPI Interface', 'kicadSymbolki_description': 'High-speed USB On-The-Go ULPI transceiver', 'kicadSymbolki_fp_filters': 'ST*uTFBGA*3.6x3.6mm*Layout6x6*P0.5mm*'}])
    newPart['name'].append('Interface_USB : STULPI01B')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

