
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_BGA"
    oIndex = "BGA-16_1.92x1.92mm_Layout4x4_P0.5mm"
    hexID = "FZKBGABGA16192X192LAYOUT4X4P5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'BGA-16_1.92x1.92mm_Layout4x4_P0.5mm', 'description': 'BGA-16, http://www.st.com/content/ccc/resource/technical/document/datasheet/group2/bc/cd/62/9e/8f/30/47/69/CD00151267/files/CD00151267.pdf/jcr:content/translations/en.CD00151267.pdf', 'tags': 'BGA-16', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/BGA-16_1.92x1.92mm_Layout4x4_P0.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_BGA : BGA-16_1.92x1.92mm_Layout4x4_P0.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

