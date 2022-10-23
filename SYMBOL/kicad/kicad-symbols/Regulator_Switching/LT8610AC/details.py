
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LT8610AC"
    hexID = "SZKREGULATORSWITCHINGLT861AC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LT8610AC', 'kicadSymbolFootprint': 'Package_SO:LTC_MSOP-16-1EP_3x4mm_P0.5mm_EP2.15x3.26mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/8610acfa.pdf', 'kicadSymbolki_keywords': 'high efficiency speed synchronous monolithic buck step-down switching regulator 42V 3.5A lower feedback voltage minimum vin', 'kicadSymbolki_description': '42V, 3.5A Synchronous Step-Down Regulator with 2.5uA Quiescent Current, 0.8V Feedback Voltage, 3.0V Minimum Vin, MSOP-16', 'kicadSymbolki_fp_filters': 'LTC*MSOP*16*1EP*3x4mm*P0.5mm*EP2.15x3.26mm*'}])
    newPart['name'].append('LT8610AC')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

