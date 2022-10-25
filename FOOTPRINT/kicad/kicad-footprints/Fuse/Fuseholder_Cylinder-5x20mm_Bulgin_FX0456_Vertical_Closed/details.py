
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Fuse"
    oIndex = "Fuseholder_Cylinder-5x20mm_Bulgin_FX0456_Vertical_Closed"
    hexID = "FZKFUFUHOLDERCYLINDER5X2BULGINFX456VERTICALCLOSED"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Fuseholder_Cylinder-5x20mm_Bulgin_FX0456_Vertical_Closed', 'description': 'Fuseholder, 5x20, closed, vertical, Bulgin, FX0456, https://www.bulgin.com/products/pub/media/bulgin/data/Fuseholders.pdf', 'tags': 'Fuseholder 5x20 closed vertical Bulgin FX0456 Sicherungshalter ', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Fuse.3dshapes/Fuseholder_Cylinder-5x20mm_Bulgin_FX0456_Vertical_Closed.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Fuse : Fuseholder_Cylinder-5x20mm_Bulgin_FX0456_Vertical_Closed')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

