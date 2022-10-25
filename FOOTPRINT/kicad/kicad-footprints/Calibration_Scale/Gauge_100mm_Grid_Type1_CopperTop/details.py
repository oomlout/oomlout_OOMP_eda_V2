
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Calibration_Scale"
    oIndex = "Gauge_100mm_Grid_Type1_CopperTop"
    hexID = "FZKCSGAUGE1GRIDTYPE1CTOP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Gauge_100mm_Grid_Type1_CopperTop', 'description': 'Gauge, Massstab, 100mm, Gitter, Grid, CopperTop, Type 1,', 'tags': 'Gauge Massstab 100mm Gitter Grid CopperTop Type 1', 'attributeType': None, 'pins': {}})
    newPart['name'].append('Calibration_Scale : Gauge_100mm_Grid_Type1_CopperTop')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

