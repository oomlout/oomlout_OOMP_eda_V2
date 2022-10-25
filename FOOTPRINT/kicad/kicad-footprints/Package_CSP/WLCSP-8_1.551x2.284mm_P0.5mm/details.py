
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_CSP"
    oIndex = "WLCSP-8_1.551x2.284mm_P0.5mm"
    hexID = "FZKCSPWLCSP81551X2284P5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'WLCSP-8_1.551x2.284mm_P0.5mm', 'description': 'WLCSP-8, 2.284x1.551mm, 8 Ball, 2x4 Layout, 0.5mm Pitch, https://www.adestotech.com/wp-content/uploads/AT25SL321_112.pdf#page=75', 'tags': 'CSP 8 0.5', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_CSP.3dshapes/WLCSP-8_1.551x2.284mm_P0.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_CSP : WLCSP-8_1.551x2.284mm_P0.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

