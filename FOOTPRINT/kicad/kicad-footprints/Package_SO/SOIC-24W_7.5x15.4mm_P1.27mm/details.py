
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "SOIC-24W_7.5x15.4mm_P1.27mm"
    hexID = "FZKSOSOIC24W75X154P127"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SOIC-24W_7.5x15.4mm_P1.27mm', 'description': 'SOIC, 24 Pin (JEDEC MS-013AD, https://www.analog.com/media/en/package-pcb-resources/package/pkg_pdf/soic_wide-rw/RW_24.pdf), generated with kicad-footprint-generator ipc_gullwing_generator.py', 'tags': 'SOIC SO', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/SOIC-24W_7.5x15.4mm_P1.27mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_SO : SOIC-24W_7.5x15.4mm_P1.27mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

