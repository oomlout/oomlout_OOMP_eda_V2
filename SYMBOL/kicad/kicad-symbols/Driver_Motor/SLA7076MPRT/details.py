
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_Motor"
    oIndex = "SLA7076MPRT"
    hexID = "SZKDRIVERMOTORSLA776MPRT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SLA7075MPRT', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SLA7076MPRT', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.semicon.sanken-ele.co.jp/sk_content/sla7076mprt_ds_en.pdf', 'kicadSymbolki_keywords': 'Stepper driver', 'kicadSymbolki_description': 'Unipolar 2-phase stepper motor driver, Microstep, 1.5A', 'kicadSymbolki_fp_filters': 'ZIP23'}])
    newPart['name'].append('SLA7076MPRT')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

