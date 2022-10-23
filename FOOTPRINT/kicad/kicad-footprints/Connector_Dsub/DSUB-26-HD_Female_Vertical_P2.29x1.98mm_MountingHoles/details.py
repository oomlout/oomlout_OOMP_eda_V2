
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Dsub"
    oIndex = "DSUB-26-HD_Female_Vertical_P2.29x1.98mm_MountingHoles"
    hexID = "FZKCNDSUBDSUB26HDFEMALEVERTICALP229X198HOLS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'DSUB-26-HD_Female_Vertical_P2.29x1.98mm_MountingHoles', 'description': '26-pin D-Sub connector, straight/vertical, THT-mount, female, pitch 2.29x1.98mm, distance of mounting holes 33.3mm, see https://disti-assets.s3.amazonaws.com/tonar/files/datasheets/16730.pdf', 'tags': '26-pin D-Sub connector straight vertical THT female pitch 2.29x1.98mm mounting holes distance 33.3mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Dsub.3dshapes/DSUB-26-HD_Female_Vertical_P2.29x1.98mm_MountingHoles.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Dsub : DSUB-26-HD_Female_Vertical_P2.29x1.98mm_MountingHoles')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

