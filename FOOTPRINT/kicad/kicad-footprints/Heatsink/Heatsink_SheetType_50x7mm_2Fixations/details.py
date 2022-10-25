
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Heatsink"
    oIndex = "Heatsink_SheetType_50x7mm_2Fixations"
    hexID = "FZKHHSHEETTYPE5X72FIXATIONS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Heatsink_SheetType_50x7mm_2Fixations', 'description': 'Heatsink, Sheet type, 50x7mm, 2 fixations (solder),', 'tags': 'Heatsink sheet', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Heatsink.3dshapes/Heatsink_SheetType_50x7mm_2Fixations.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Heatsink : Heatsink_SheetType_50x7mm_2Fixations')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

