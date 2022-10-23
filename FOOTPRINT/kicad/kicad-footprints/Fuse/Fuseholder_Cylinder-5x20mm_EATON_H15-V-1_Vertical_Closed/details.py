
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Fuse"
    oIndex = "Fuseholder_Cylinder-5x20mm_EATON_H15-V-1_Vertical_Closed"
    hexID = "FZKFUFUHOLDERCYLINDER5X2EATONH15V1VERTICALCLOSED"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Fuseholder_Cylinder-5x20mm_EATON_H15-V-1_Vertical_Closed', 'description': 'PCB fuse holders for 5 mm x 20 mm fuses; 250V; 10A (http://www.cooperindustries.com/content/dam/public/bussmann/Electronics/Resources/product-datasheets/bus-elx-ds-4426-h15.pdf)', 'tags': 'fuse holder vertical 5x20mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Fuse.3dshapes/Fuseholder_Cylinder-5x20mm_EATON_H15-V-1_Vertical_Closed.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Fuse : Fuseholder_Cylinder-5x20mm_EATON_H15-V-1_Vertical_Closed')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

