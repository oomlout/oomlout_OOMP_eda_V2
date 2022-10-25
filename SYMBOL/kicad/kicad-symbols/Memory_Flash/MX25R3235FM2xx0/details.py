
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_Flash"
    oIndex = "MX25R3235FM2xx0"
    hexID = "SZKMEMORYFLASHMX25R3235FM2XX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MX25R3235FM2xx0', 'kicadSymbolFootprint': 'Package_SO:SOP-8_5.28x5.23mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.macronix.com/Lists/Datasheet/Attachments/7534/MX25R3235F,%20Wide%20Range,%2032Mb,%20v1.6.pdf', 'kicadSymbolki_keywords': 'SPI 32Mbit 1.65V-3.6V', 'kicadSymbolki_description': '32-Mbit, Wide Range Voltage SPI Serial Flash Memory, SOP-8', 'kicadSymbolki_fp_filters': 'SOP*5.28x5.23mm*P1.27mm*'}])
    newPart['name'].append('Memory_Flash : MX25R3235FM2xx0')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

