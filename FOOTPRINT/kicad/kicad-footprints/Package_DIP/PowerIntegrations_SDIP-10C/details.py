
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DIP"
    oIndex = "PowerIntegrations_SDIP-10C"
    hexID = "FZKDIPPOWERINTEGRATIONSSDIP1C"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PowerIntegrations_SDIP-10C', 'description': 'PowerIntegrations variant of 10-lead though-hole mounted DIP package, row spacing 7.62 mm (300 mils), LongPads, see https://www.power.com/sites/default/files/product-docs/tophx_family_datasheet.pdf', 'tags': 'THT DIP DIL PDIP 2.54mm 7.62mm 300mil LongPads', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DIP.3dshapes/PowerIntegrations_SDIP-10C.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Package_DIP : PowerIntegrations_SDIP-10C')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

