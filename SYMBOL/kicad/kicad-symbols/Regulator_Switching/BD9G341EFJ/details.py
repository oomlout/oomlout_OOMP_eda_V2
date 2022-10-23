
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "BD9G341EFJ"
    hexID = "SZKREGULATORSWITCHINGBD9G341EFJ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'BD9G341EFJ', 'kicadSymbolFootprint': 'Package_SO:HTSOP-8-1EP_3.9x4.9mm_P1.27mm_EP2.4x3.2mm_ThermalVias', 'kicadSymbolDatasheet': 'https://media.digikey.com/pdf/Data%20Sheets/Rohm%20PDFs/BD9G341EFJ.pdf', 'kicadSymbolki_keywords': 'Buck Converter', 'kicadSymbolki_description': '12V-76V input voltage range 3A output current, Buck Converter, Integrated FET, HTSOP-8', 'kicadSymbolki_fp_filters': 'HTSOP*EP*3.9x4.9mm*P1.27mm*ThermalVias*'}])
    newPart['name'].append('BD9G341EFJ')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

