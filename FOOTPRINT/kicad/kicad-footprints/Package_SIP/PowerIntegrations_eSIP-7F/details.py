
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SIP"
    oIndex = "PowerIntegrations_eSIP-7F"
    hexID = "FZKSIPPOWERINTEGRATIONSESIP7F"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PowerIntegrations_eSIP-7F', 'description': 'eSIP-7F Flat Package with Heatsink Tab https://ac-dc.power.com/sites/default/files/product-docs/linkswitch-ph_family_datasheet.pdf', 'tags': 'Power Integrations L Package', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SIP.3dshapes/PowerIntegrations_eSIP-7F.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Package_SIP : PowerIntegrations_eSIP-7F')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

