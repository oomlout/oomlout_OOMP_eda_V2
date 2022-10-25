
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_BGA"
    oIndex = "Lattice_caBGA-756_27.0x27.0mm_Layout32x32_P0.8mm"
    hexID = "FZKBGALATTICECABGA75627X27LAYOUT32X32P8"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Lattice_caBGA-756_27.0x27.0mm_Layout32x32_P0.8mm', 'description': 'Lattice caBGA-756, ECP5 FPGAs, 27.0x27.0mm, 756 Ball, 32x32 Layout, 0.8mm Pitch, http://www.latticesemi.com/view_document?document_id=213', 'tags': 'BGA 756 0.8', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/Lattice_caBGA-756_27.0x27.0mm_Layout32x32_P0.8mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_BGA : Lattice_caBGA-756_27.0x27.0mm_Layout32x32_P0.8mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

