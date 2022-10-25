
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Calibration_Scale"
    oIndex = "Gauge_10mm_Type2_SilkScreenTop"
    hexID = "FZKCSGAUGE1TYPE2SILKSCREENTOP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Gauge_10mm_Type2_SilkScreenTop', 'description': 'Gauge, Massstab, 10mm, SilkScreenTop, Type 2,', 'tags': 'Gauge Massstab 10mm SilkScreenTop Type 2', 'attributeType': None, 'pins': {}})
    newPart['name'].append('Calibration_Scale : Gauge_10mm_Type2_SilkScreenTop')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

