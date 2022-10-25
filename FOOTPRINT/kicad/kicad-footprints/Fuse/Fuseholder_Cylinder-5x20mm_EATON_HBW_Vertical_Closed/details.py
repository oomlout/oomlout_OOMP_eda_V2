
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Fuse"
    oIndex = "Fuseholder_Cylinder-5x20mm_EATON_HBW_Vertical_Closed"
    hexID = "FZKFUFUHOLDERCYLINDER5X2EATONHBWVERTICALCLOSED"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Fuseholder_Cylinder-5x20mm_EATON_HBW_Vertical_Closed', 'description': '5 mm x 20 mm fuse holders; Vertical w/o Stability Pins; 250V; 6.3-16A (http://www.cooperindustries.com/content/dam/public/bussmann/Electronics/Resources/product-datasheets/Bus_Elx_DS_2118_HB_PCB_Series.pdf)', 'tags': 'fuse holder vertical 5x20mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Fuse.3dshapes/Fuseholder_Cylinder-5x20mm_EATON_HBW_Vertical_Closed.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Fuse : Fuseholder_Cylinder-5x20mm_EATON_HBW_Vertical_Closed')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

