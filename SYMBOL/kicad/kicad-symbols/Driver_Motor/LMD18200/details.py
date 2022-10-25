
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_Motor"
    oIndex = "LMD18200"
    hexID = "SZKDRIVERMOTORLMD182"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LMD18200', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-220-11_P3.4x5.08mm_StaggerOdd_Lead4.85mm_Vertical', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lmd18200.pdf', 'kicadSymbolki_keywords': 'H-Bridge DC stepper servo motor driver Motion Control Applications', 'kicadSymbolki_description': '3A, 55V H-Bridge, Motion Control Applications, TO-220-11', 'kicadSymbolki_fp_filters': 'TO?220*'}])
    newPart['name'].append('Driver_Motor : LMD18200')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

