
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_Motor"
    oIndex = "DRV8711"
    hexID = "SZKDRIVERMOTORDRV8711"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DRV8711', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/slvsc40f/slvsc40f.pdf', 'kicadSymbolki_keywords': 'Stepper driver', 'kicadSymbolki_description': 'Stepper motor controller, external N-channel MOSFET, single bipolar stepper motor, dual brushed DC motors', 'kicadSymbolki_fp_filters': 'HTSSOP-38'}])
    newPart['name'].append('Driver_Motor : DRV8711')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

