
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Oscillator"
    oIndex = "XUY73"
    hexID = "SZKOCSXUY73"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'XUY71', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'XUY73', 'kicadSymbolFootprint': 'Oscillator:Oscillator_SMD_IDT_JU6-6_7.0x5.0mm_P2.54mm', 'kicadSymbolDatasheet': 'https://www.idt.com/document/dst/xu-family-datasheet', 'kicadSymbolki_keywords': 'OTP XHCMOS 3.3V VCXO', 'kicadSymbolki_description': 'Low phase noise, quartz-based PLL oscillator, 0.016-1500 MHz, complementary output', 'kicadSymbolki_fp_filters': 'Oscillator*JU6*'}])
    newPart['name'].append('XUY73')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

