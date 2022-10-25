
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Module"
    oIndex = "Maple_Mini"
    hexID = "SZKMCUMOMAPLEM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'A', 'kicadSymbolValue': 'Maple_Mini', 'kicadSymbolFootprint': 'Module:Maple_Mini', 'kicadSymbolDatasheet': 'http://docs.leaflabs.com/static.leaflabs.com/pub/leaflabs/maple-docs/0.0.12/hardware/maple-mini.html', 'kicadSymbolki_keywords': 'Maple Mini Microcontroller Module LeafLabs STM32 STM32F103', 'kicadSymbolki_description': 'Maple Mini Microcontroller Module by LeafLabs', 'kicadSymbolki_fp_filters': 'Maple*Mini*'}])
    newPart['name'].append('MCU_Module : Maple_Mini')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

