
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SON"
    oIndex = "Texas_S-PVSON-N10"
    hexID = "FZKSONTEXASSPVSONN1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Texas_S-PVSON-N10', 'description': '3x3mm Body, 0.5mm Pitch, S-PVSON-N10, DRC, http://www.ti.com/lit/ds/symlink/tps61201.pdf', 'tags': '0.5 S-PVSON-N10 DRC', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SON.3dshapes/Texas_S-PVSON-N10.wrl', 'pins': {'type': 'smd', 'shape': 'oval'}})
    newPart['name'].append('Package_SON : Texas_S-PVSON-N10')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

