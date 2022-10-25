
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SON"
    oIndex = "Texas_DRC0010J_ThermalVias"
    hexID = "FZKSONTEXASDRC1JTHERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Texas_DRC0010J_ThermalVias', 'description': 'Texas DRC0010J, VSON10 3x3mm Body, 0.5mm Pitch,  http://www.ti.com/lit/ds/symlink/tps63000.pdf', 'tags': 'Texas VSON10 3x3mm', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SON.3dshapes/Texas_DRC0010J.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_SON : Texas_DRC0010J_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

