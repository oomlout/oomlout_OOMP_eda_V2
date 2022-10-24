
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DIP"
    oIndex = "PowerIntegrations_SMD-8C"
    hexID = "FZKDIPPOWERINTEGRATIONSSM8C"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PowerIntegrations_SMD-8C', 'description': 'PowerIntegrations variant of 8-lead surface-mounted (SMD) DIP package, row spacing 7.62 mm (300 mils), see https://ac-dc.power.com/sites/default/files/product-docs/tinyswitch-iii_family_datasheet.pdf', 'tags': 'SMD DIP DIL PDIP SMDIP 2.54mm 7.62mm 300mil', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DIP.3dshapes/PowerIntegrations_SMD-8C.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_DIP : PowerIntegrations_SMD-8C')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

