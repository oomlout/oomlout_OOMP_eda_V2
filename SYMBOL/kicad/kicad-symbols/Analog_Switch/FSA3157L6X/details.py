
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_Switch"
    oIndex = "FSA3157L6X"
    hexID = "SZKANALOGSWITCHFSA3157L6X"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'NC7SB3157L6X', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'FSA3157L6X', 'kicadSymbolFootprint': 'Package_SON:Fairchild_MicroPak-6_1.0x1.45mm_P0.5mm', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/NC7SB3157-D.PDF', 'kicadSymbolki_keywords': 'CMOS Analog Switch', 'kicadSymbolki_description': 'Single SPDT Low-Voltage Analog Switch or 2:1 Multiplexer/De-Multiplexer Bus Switch, 10Ohm Ron, MicroPak-6', 'kicadSymbolki_fp_filters': 'Fairchild*MicroPak*1.0x1.45mm*P0.5mm*'}])
    newPart['name'].append('FSA3157L6X')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

