
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Dsub"
    oIndex = "DSUB-37_Female_Horizontal_P2.77x2.84mm_EdgePinOffset7.70mm_Housed_MountingHolesOffset9.12mm"
    hexID = "FZKCNDSUBDSUB37FEMALEHORIZONTALP277X284EDGEPINOFFSET77HOUSEDHOLSOFFSET912"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'DSUB-37_Female_Horizontal_P2.77x2.84mm_EdgePinOffset7.70mm_Housed_MountingHolesOffset9.12mm', 'description': '37-pin D-Sub connector, horizontal/angled (90 deg), THT-mount, female, pitch 2.77x2.84mm, pin-PCB-offset 7.699999999999999mm, distance of mounting holes 63.5mm, distance of mounting holes to PCB edge 9.12mm, see https://disti-assets.s3.amazonaws.com/tonar/files/datasheets/16730.pdf', 'tags': '37-pin D-Sub connector horizontal angled 90deg THT female pitch 2.77x2.84mm pin-PCB-offset 7.699999999999999mm mounting-holes-distance 63.5mm mounting-hole-offset 63.5mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Dsub.3dshapes/DSUB-37_Female_Horizontal_P2.77x2.84mm_EdgePinOffset7.70mm_Housed_MountingHolesOffset9.12mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Dsub : DSUB-37_Female_Horizontal_P2.77x2.84mm_EdgePinOffset7.70mm_Housed_MountingHolesOffset9.12mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

