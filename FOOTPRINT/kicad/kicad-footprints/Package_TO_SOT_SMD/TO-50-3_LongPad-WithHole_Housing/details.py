
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_TO_SOT_SMD"
    oIndex = "TO-50-3_LongPad-WithHole_Housing"
    hexID = "FZKPACKAGETOSOTSMTO53LONGPADWITHHOLEHOUSING"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TO-50-3_LongPad-WithHole_Housing', 'description': 'TO-50-3 Macro T Package Style M236', 'tags': 'TO-50-3 Macro T Package Style M236', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_TO_SOT_SMD.3dshapes/TO-50-3_LongPad-WithHole_Housing.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Package_TO_SOT_SMD : TO-50-3_LongPad-WithHole_Housing')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

