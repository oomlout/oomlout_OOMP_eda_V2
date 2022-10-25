
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "PowerIntegrations_SO-8"
    hexID = "FZKSOPOWERINTEGRATIONSSO8"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PowerIntegrations_SO-8', 'description': 'Power-Integrations variant of 8-Lead Plastic Small Outline (SN) - Narrow, 3.90 mm Body [SOIC], see https://ac-dc.power.com/sites/default/files/product-docs/senzero_family_datasheet.pdf', 'tags': 'SOIC 1.27', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/PowerIntegrations_SO-8.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SO : PowerIntegrations_SO-8')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

