
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DIP"
    oIndex = "PowerIntegrations_eDIP-12B"
    hexID = "FZKDIPPOWERINTEGRATIONSEDIP12B"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PowerIntegrations_eDIP-12B', 'description': 'Power Integrations eDIP-12B, see https://www.power.com/sites/default/files/product-docs/linkswitch-pl_family_datasheet.pdf', 'tags': 'THT DIP DIL PDIP 2.54mm 7.62mm 300mil', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DIP.3dshapes/PowerIntegrations_eDIP-12B.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Package_DIP : PowerIntegrations_eDIP-12B')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

