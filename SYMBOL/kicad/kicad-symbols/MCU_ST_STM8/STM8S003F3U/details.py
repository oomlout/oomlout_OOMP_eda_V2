
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM8"
    oIndex = "STM8S003F3U"
    hexID = "SZKMCUSTSTM8STM8S3F3U"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM8S003F3U', 'kicadSymbolFootprint': 'Package_DFN_QFN:ST_UFQFPN-20_3x3mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00024550.pdf', 'kicadSymbolki_keywords': 'STM8S Mainstream Value line 8-bit, 16MHz, 1k RAM, 128 EEPROM', 'kicadSymbolki_description': '16MHz, 8K Flash, 1K RAM, 128 EEPROM, USART, I²C, SPI, UFQFPN-20', 'kicadSymbolki_fp_filters': 'ST?UFQFPN*3x3mm*P0.5mm*'}])
    newPart['name'].append('MCU_ST_STM8 : STM8S003F3U')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

