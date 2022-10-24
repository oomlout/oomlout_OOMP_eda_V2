
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_TO_SOT_THT"
    oIndex = "TO-220-4_P5.08x2.54mm_StaggerOdd_Lead5.84mm_TabDown"
    hexID = "FZKSOTTO224P58X254STAGGERODDLEAD584TABDOWN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TO-220-4_P5.08x2.54mm_StaggerOdd_Lead5.84mm_TabDown', 'description': 'TO-220-4, Horizontal, RM 2.54mm, staggered type-1', 'tags': 'TO-220-4 Horizontal RM 2.54mm staggered type-1', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_TO_SOT_THT.3dshapes/TO-220-4_P5.08x2.54mm_StaggerOdd_Lead5.84mm_TabDown.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'oval'}})
    newPart['name'].append('Package_TO_SOT_THT : TO-220-4_P5.08x2.54mm_StaggerOdd_Lead5.84mm_TabDown')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

