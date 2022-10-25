
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "SOP-24_7.5x15.4mm_P1.27mm"
    hexID = "FZKSOS2475X154P127"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SOP-24_7.5x15.4mm_P1.27mm', 'description': 'SOP, 24 Pin (http://www.issi.com/WW/pdf/31FL3218.pdf#page=14), generated with kicad-footprint-generator ipc_gullwing_generator.py', 'tags': 'SOP SO', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/SOP-24_7.5x15.4mm_P1.27mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_SO : SOP-24_7.5x15.4mm_P1.27mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

