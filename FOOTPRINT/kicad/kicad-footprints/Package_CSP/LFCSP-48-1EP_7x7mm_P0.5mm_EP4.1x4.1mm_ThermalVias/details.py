
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_CSP"
    oIndex = "LFCSP-48-1EP_7x7mm_P0.5mm_EP4.1x4.1mm_ThermalVias"
    hexID = "FZKCSPLFCSP481EP7X7P5EP41X41THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LFCSP-48-1EP_7x7mm_P0.5mm_EP4.1x4.1mm_ThermalVias', 'description': 'LFCSP, 48 Pin (https://www.analog.com/media/en/package-pcb-resources/package/pkg_pdf/lfcspcp/cp_48_5.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'LFCSP NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_CSP.3dshapes/LFCSP-48-1EP_7x7mm_P0.5mm_EP4.1x4.1mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_CSP : LFCSP-48-1EP_7x7mm_P0.5mm_EP4.1x4.1mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

