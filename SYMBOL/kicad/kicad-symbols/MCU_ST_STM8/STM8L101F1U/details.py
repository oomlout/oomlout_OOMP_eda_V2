
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_ST_STM8"
    oIndex = "STM8L101F1U"
    hexID = "SZKMCUSTSTM8STM8L11F1U"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'STM8L101F1U', 'kicadSymbolFootprint': 'Package_DFN_QFN:ST_UFQFPN-20_3x3mm_P0.5mm', 'kicadSymbolDatasheet': 'https://www.st.com/resource/en/datasheet/stm8l101f1.pdf', 'kicadSymbolki_keywords': 'STM8L Microcontroller Value Line Low Power', 'kicadSymbolki_description': '16MHz, 2K Flash, 1.5K RAM, 2K EEPROM, USART,  I²C, SPI, ADC, UFQFPN-20', 'kicadSymbolki_fp_filters': 'ST?UFQFPN*3x3mm*P0.5mm*'}])
    newPart['name'].append('STM8L101F1U')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

