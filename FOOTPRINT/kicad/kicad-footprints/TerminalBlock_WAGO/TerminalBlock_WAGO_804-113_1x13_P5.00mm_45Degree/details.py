
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "TerminalBlock_WAGO"
    oIndex = "TerminalBlock_WAGO_804-113_1x13_P5.00mm_45Degree"
    hexID = "FZKTBWAGOTBWAGO841131X13P545DEGREE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TerminalBlock_WAGO_804-113_1x13_P5.00mm_45Degree', 'description': 'Terminal Block WAGO 804-113, 45Degree (cable under 45degree), 13 pins, pitch 5mm, size 66.5x15mm^2, drill diamater 1.2mm, pad diameter 3mm, see , script-generated with , script-generated using https://github.com/pointhi/kicad-footprint-generator/scripts/TerminalBlock_WAGO', 'tags': 'THT Terminal Block WAGO 804-113 45Degree pitch 5mm size 66.5x15mm^2 drill 1.2mm pad 3mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/TerminalBlock_WAGO.3dshapes/TerminalBlock_WAGO_804-113_1x13_P5.00mm_45Degree.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('TerminalBlock_WAGO : TerminalBlock_WAGO_804-113_1x13_P5.00mm_45Degree')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

