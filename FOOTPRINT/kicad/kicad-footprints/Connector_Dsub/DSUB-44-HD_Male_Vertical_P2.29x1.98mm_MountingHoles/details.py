
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Dsub"
    oIndex = "DSUB-44-HD_Male_Vertical_P2.29x1.98mm_MountingHoles"
    hexID = "FZKCNDSUBDSUB44HDMALEVERTICALP229X198HOLS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'DSUB-44-HD_Male_Vertical_P2.29x1.98mm_MountingHoles', 'description': '44-pin D-Sub connector, straight/vertical, THT-mount, male, pitch 2.29x1.98mm, distance of mounting holes 47.1mm, see https://disti-assets.s3.amazonaws.com/tonar/files/datasheets/16730.pdf', 'tags': '44-pin D-Sub connector straight vertical THT male pitch 2.29x1.98mm mounting holes distance 47.1mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Dsub.3dshapes/DSUB-44-HD_Male_Vertical_P2.29x1.98mm_MountingHoles.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_Dsub : DSUB-44-HD_Male_Vertical_P2.29x1.98mm_MountingHoles')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

