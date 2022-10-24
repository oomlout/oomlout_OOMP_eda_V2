
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_LGA"
    oIndex = "Texas_SIL0008D_MicroSiP-8-1EP_2.8x3mm_P0.65mm_EP1.1x1.9mm_ThermalVias"
    hexID = "FZKLGATEXASSIL8DMSIP81EP28X3P65EP11X19THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Texas_SIL0008D_MicroSiP-8-1EP_2.8x3mm_P0.65mm_EP1.1x1.9mm_ThermalVias', 'description': 'Texas SIL0008D MicroSiP, 8 Pin (http://www.ti.com/lit/ds/symlink/tps82130.pdf#page=19), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'Texas MicroSiP NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_LGA.3dshapes/Texas_SIL0008D_MicroSiP-8-1EP_2.8x3mm_P0.65mm_EP1.1x1.9mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_LGA : Texas_SIL0008D_MicroSiP-8-1EP_2.8x3mm_P0.65mm_EP1.1x1.9mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

