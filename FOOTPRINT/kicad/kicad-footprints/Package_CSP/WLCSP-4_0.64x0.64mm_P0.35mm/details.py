
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_CSP"
    oIndex = "WLCSP-4_0.64x0.64mm_P0.35mm"
    hexID = "FZKCSPWLCSP464X64P35"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'WLCSP-4_0.64x0.64mm_P0.35mm', 'description': 'WLCSP-4, 0.64x0.64mm, 4 Ball, 2x2 Layout, 0.35mm Pitch, https://www.onsemi.com/pdf/datasheet/ncp163-d.pdf#page=23', 'tags': 'CSP 4 0.35', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_CSP.3dshapes/WLCSP-4_0.64x0.64mm_P0.35mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_CSP : WLCSP-4_0.64x0.64mm_P0.35mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

