
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "ACPL-214-500E"
    hexID = "SZKISOLATORACPL2145E"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TLP290', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ACPL-214-500E', 'kicadSymbolFootprint': 'Package_SO:SOP-4_4.4x2.6mm_P1.27mm', 'kicadSymbolDatasheet': 'https://docs.broadcom.com/doc/AV02-0469EN', 'kicadSymbolki_keywords': 'npn ac dc ac-dc acdc phototransistor optocoupler optoisolator', 'kicadSymbolki_description': 'AC/DC Phototransistor Optocoupler, Vce 80V, CTR 20-400%, SOP-4', 'kicadSymbolki_fp_filters': 'SOP*4*4.4x2.6mm*P1.27mm*'}])
    newPart['name'].append('ACPL-214-500E')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

