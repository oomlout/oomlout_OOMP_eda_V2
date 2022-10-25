
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_BGA"
    oIndex = "Texas_MicroStar_Junior_BGA-12_2.0x2.5mm_Layout4x3_P0.5mm"
    hexID = "FZKBGATEXASMSTARJUNIORBGA122X25LAYOUT4X3P5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Texas_MicroStar_Junior_BGA-12_2.0x2.5mm_Layout4x3_P0.5mm', 'description': 'Texas Instruments, BGA Microstar Junior, 2x2.5mm, 12 bump 4x3 grid, NSMD pad definition (http://www.ti.com/lit/ds/symlink/txb0104.pdf, http://www.ti.com/lit/wp/ssyz015b/ssyz015b.pdf)', 'tags': 'Texas_Junior_BGA-12', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/Texas_MicroStar_Junior_BGA-12_2.0x2.5mm_Layout4x3_P0.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_BGA : Texas_MicroStar_Junior_BGA-12_2.0x2.5mm_Layout4x3_P0.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

