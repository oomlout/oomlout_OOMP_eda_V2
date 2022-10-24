
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "PowerIntegrations_eSOP-12B"
    hexID = "FZKSOPOWERINTEGRATIONSES12B"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PowerIntegrations_eSOP-12B', 'description': 'eSOP-12B SMT Flat Package with Heatsink Tab, see https://ac-dc.power.com/sites/default/files/product-docs/topswitch-jx_family_datasheet.pdf', 'tags': 'Power Integrations K Package', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/PowerIntegrations_eSOP-12B.wrl', 'pins': {'type': 'smd', 'shape': 'oval'}})
    newPart['name'].append('Package_SO : PowerIntegrations_eSOP-12B')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

