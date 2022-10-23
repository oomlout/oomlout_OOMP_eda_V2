
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Oscillator"
    oIndex = "XUY51"
    hexID = "SZKOCSXUY51"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'XUY51', 'kicadSymbolFootprint': 'Oscillator:Oscillator_SMD_IDT_JS6-6_5.0x3.2mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.idt.com/document/dst/xu-family-datasheet', 'kicadSymbolki_keywords': 'OTP HCMOS 1.8V VCXO', 'kicadSymbolki_description': 'Low phase noise, quartz-based PLL oscillator, 0.016-1500 MHz, complementary output', 'kicadSymbolki_fp_filters': 'Oscillator*JS6*'}])
    newPart['name'].append('XUY51')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

