
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Crystal"
    oIndex = "Resonator-3Pin_W8.0mm_H3.5mm"
    hexID = "FZKXR3PINW8H35"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Resonator-3Pin_W8.0mm_H3.5mm', 'description': 'Ceramic Resomator/Filter 8.0x3.5mm^2, length*width=8.0x3.5mm^2 package, package length=8.0mm, package width=3.5mm, 3 pins', 'tags': 'THT ceramic resonator filter', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Crystal.3dshapes/Resonator-3Pin_W8.0mm_H3.5mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Crystal : Resonator-3Pin_W8.0mm_H3.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

