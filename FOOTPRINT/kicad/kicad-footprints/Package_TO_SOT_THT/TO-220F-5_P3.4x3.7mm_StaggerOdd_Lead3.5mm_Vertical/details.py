
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_TO_SOT_THT"
    oIndex = "TO-220F-5_P3.4x3.7mm_StaggerOdd_Lead3.5mm_Vertical"
    hexID = "FZKSOTTO22F5P34X37STAGGERODDLEAD35VERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TO-220F-5_P3.4x3.7mm_StaggerOdd_Lead3.5mm_Vertical', 'description': 'TO-220F-5, Vertical, RM 1.7mm, PentawattF-, MultiwattF-5, staggered type-1', 'tags': 'TO-220F-5 Vertical RM 1.7mm PentawattF- MultiwattF-5 staggered type-1', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_TO_SOT_THT.3dshapes/TO-220F-5_P3.4x3.7mm_StaggerOdd_Lead3.5mm_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Package_TO_SOT_THT : TO-220F-5_P3.4x3.7mm_StaggerOdd_Lead3.5mm_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

