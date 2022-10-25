
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Crystal"
    oIndex = "Resonator-3Pin_W6.0mm_H3.0mm"
    hexID = "FZKXR3PINW6H3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Resonator-3Pin_W6.0mm_H3.0mm', 'description': 'Ceramic Resomator/Filter 6.0x3.0mm^2, length*width=6.0x3.0mm^2 package, package length=6.0mm, package width=3.0mm, 3 pins', 'tags': 'THT ceramic resonator filter', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Crystal.3dshapes/Resonator-3Pin_W6.0mm_H3.0mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Crystal : Resonator-3Pin_W6.0mm_H3.0mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

