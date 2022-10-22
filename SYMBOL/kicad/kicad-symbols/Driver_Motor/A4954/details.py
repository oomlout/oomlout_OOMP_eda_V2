
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_Motor"
    oIndex = "A4954"
    hexID = "SZKDRIVERMOTORA4954"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'A4954', 'kicadSymbolFootprint': 'Package_SO:TSSOP-16-1EP_4.4x5mm_P0.65mm_EP3x3mm', 'kicadSymbolDatasheet': 'https://www.allegromicro.com/-/media/Files/Datasheets/A4954-Datasheet.ashx', 'kicadSymbolki_keywords': 'Fullbridge, Stepper Driver', 'kicadSymbolki_description': 'Fullbridge PWM Motor Driver, UVLO, OCP, Current Limit, Short Circuit Protection, TSSOP-16', 'kicadSymbolki_fp_filters': 'TSSOP*1EP*4.4x5mm*P0.65mm*'}])
    newPart['name'].append('A4954')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

