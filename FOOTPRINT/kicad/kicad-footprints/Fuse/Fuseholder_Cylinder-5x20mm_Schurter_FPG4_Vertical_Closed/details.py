
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Fuse"
    oIndex = "Fuseholder_Cylinder-5x20mm_Schurter_FPG4_Vertical_Closed"
    hexID = "FZKFUFUHOLDERCYLINDER5X2SCHURTERFPG4VERTICALCLOSED"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Fuseholder_Cylinder-5x20mm_Schurter_FPG4_Vertical_Closed', 'description': 'Shock-Safe Fuseholder, 5 x 20 mm, Slotted Cap/Fingergrip, vertical, IEC 60335-1; 250VAC/10A VDE; 500V/16A UL/CSA (https://us.schurter.com/bundles/snceschurter/epim/_ProdPool_/newDS/en/typ_FPG4.pdf)', 'tags': 'fuse holder vertical 5x20mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Fuse.3dshapes/Fuseholder_Cylinder-5x20mm_Schurter_FPG4_Vertical_Closed.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Fuse : Fuseholder_Cylinder-5x20mm_Schurter_FPG4_Vertical_Closed')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

