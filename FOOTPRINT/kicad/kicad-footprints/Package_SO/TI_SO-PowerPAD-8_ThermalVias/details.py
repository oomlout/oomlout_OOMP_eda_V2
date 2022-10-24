
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "TI_SO-PowerPAD-8_ThermalVias"
    hexID = "FZKSOTISOPOWERPAD8THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TI_SO-PowerPAD-8_ThermalVias', 'description': '8-pin HTSOP package with 1.27mm pin pitch, compatible with SOIC-8, 3.9x4.9mm² body, exposed pad, thermal vias with large copper area, as proposed in http://www.ti.com/lit/ds/symlink/tps5430.pdf', 'tags': 'HTSOP 1.27', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/HTSOP-8-1EP_3.9x4.9mm_Pitch1.27mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SO : TI_SO-PowerPAD-8_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

