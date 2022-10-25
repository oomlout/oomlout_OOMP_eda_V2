
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "CPLD_Microchip"
    oIndex = "ATF1502ASL-xAx44"
    hexID = "SZKCPLDMCHIPATF152ASLXAX44"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ATF1502AS-xAx44', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATF1502ASL-xAx44', 'kicadSymbolFootprint': 'Package_QFP:TQFP-44_10x10mm_P0.8mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-0995-CPLD-ATF1502AS(L)-Datasheet.pdf', 'kicadSymbolki_keywords': 'CPLD', 'kicadSymbolki_description': 'Microchip CPLD, 32 Macrocell, 5 V, Low Power, TQFP-44', 'kicadSymbolki_fp_filters': 'TQFP*10x10mm*P0.8mm*'}])
    newPart['name'].append('CPLD_Microchip : ATF1502ASL-xAx44')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

