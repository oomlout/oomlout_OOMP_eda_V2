
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Fuse"
    oIndex = "Fuseholder_Cylinder-5x20mm_Stelvio-Kontek_PTF78_Horizontal_Open"
    hexID = "FZKFUFUHOLDERCYLINDER5X2STELVIOKONTEKPTF78HORIZONTALOPEN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Fuseholder_Cylinder-5x20mm_Stelvio-Kontek_PTF78_Horizontal_Open', 'description': 'https://www.tme.eu/en/Document/3b48dbe2b9714a62652c97b08fcd464b/PTF78.pdf', 'tags': 'Fuseholder horizontal open 5x20 Stelvio-Kontek PTF/78', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Fuse.3dshapes/Fuseholder_Cylinder-5x20mm_Stelvio-Kontek_PTF78_Horizontal_Open.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Fuse : Fuseholder_Cylinder-5x20mm_Stelvio-Kontek_PTF78_Horizontal_Open')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

