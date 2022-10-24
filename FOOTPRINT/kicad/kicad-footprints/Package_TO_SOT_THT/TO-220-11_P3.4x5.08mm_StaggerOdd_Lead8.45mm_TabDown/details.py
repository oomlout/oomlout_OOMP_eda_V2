
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_TO_SOT_THT"
    oIndex = "TO-220-11_P3.4x5.08mm_StaggerOdd_Lead8.45mm_TabDown"
    hexID = "FZKSOTTO2211P34X58STAGGERODDLEAD845TABDOWN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TO-220-11_P3.4x5.08mm_StaggerOdd_Lead8.45mm_TabDown', 'description': 'TO-220-11, Horizontal, RM 1.7mm, staggered type-1, see http://www.ti.com/lit/ds/symlink/lmd18200.pdf', 'tags': 'TO-220-11 Horizontal RM 1.7mm staggered type-1', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_TO_SOT_THT.3dshapes/TO-220-11_P3.4x5.08mm_StaggerOdd_Lead8.45mm_Tab-Down.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'oval'}})
    newPart['name'].append('Package_TO_SOT_THT : TO-220-11_P3.4x5.08mm_StaggerOdd_Lead8.45mm_TabDown')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

