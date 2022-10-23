
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Oscillator"
    oIndex = "XUX52"
    hexID = "SZKOCSXUX52"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'XUX51', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'XUX52', 'kicadSymbolFootprint': 'Oscillator:Oscillator_SMD_IDT_JS6-6_5.0x3.2mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.idt.com/document/dst/xu-family-datasheet', 'kicadSymbolki_keywords': 'OTP XHCMOS 2.5V VCXO', 'kicadSymbolki_description': 'Low phase noise, quartz-based PLL oscillator, 0.016-1500 MHz, complementary output', 'kicadSymbolki_fp_filters': 'Oscillator*JS6*'}])
    newPart['name'].append('XUX52')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

