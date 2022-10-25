
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_Motor"
    oIndex = "A4950K"
    hexID = "SZKDRIVERMOTORA495K"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'A4950E', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'A4950K', 'kicadSymbolFootprint': 'Package_SO:SOIC-8-1EP_3.9x4.9mm_P1.27mm_EP2.41x3.3mm', 'kicadSymbolDatasheet': 'http://www.allegromicro.com/~/media/Files/Datasheets/A4950-Datasheet.ashx', 'kicadSymbolki_keywords': 'full-bridge h-bridge', 'kicadSymbolki_description': 'Full-Bridge, DMOS PWM, Motor Driver, 40V, 3.5A, -40 to +125C', 'kicadSymbolki_fp_filters': 'SOIC-*1EP*'}])
    newPart['name'].append('Driver_Motor : A4950K')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

