
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_QFP"
    oIndex = "EQFP-144-1EP_20x20mm_P0.5mm_EP6.61x5.615mm_ThermalVias"
    hexID = "FZKQFPEQFP1441EP2X2P5EP661X5615THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'EQFP-144-1EP_20x20mm_P0.5mm_EP6.61x5.615mm_ThermalVias', 'description': 'EQFP, 144 Pin (https://www.intel.com/content/dam/www/programmable/us/en/pdfs/literature/packaging/04r00485-02.pdf), generated with kicad-footprint-generator ipc_gullwing_generator.py', 'tags': 'EQFP QFP', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_QFP.3dshapes/EQFP-144-1EP_20x20mm_P0.5mm_EP6.61x5.615mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_QFP : EQFP-144-1EP_20x20mm_P0.5mm_EP6.61x5.615mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

