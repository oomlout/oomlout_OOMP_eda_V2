
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "TerminalBlock_TE-Connectivity"
    oIndex = "TerminalBlock_TE_1-282834-2_1x12_P2.54mm_Horizontal"
    hexID = "FZKTBTECONNECTIVITYTBTE128283421X12P254HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TerminalBlock_TE_1-282834-2_1x12_P2.54mm_Horizontal', 'description': 'Terminal Block TE 1-282834-2, 12 pins, pitch 2.54mm, size 30.94x6.5mm^2, drill diamater 1.1mm, pad diameter 2.1mm, see http://www.te.com/commerce/DocumentDelivery/DDEController?Action=showdoc&DocId=Customer+Drawing%7F282834%7FC1%7Fpdf%7FEnglish%7FENG_CD_282834_C1.pdf, script-generated using https://github.com/pointhi/kicad-footprint-generator/scripts/TerminalBlock_TE-Connectivity', 'tags': 'THT Terminal Block TE 1-282834-2 pitch 2.54mm size 30.94x6.5mm^2 drill 1.1mm pad 2.1mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/TerminalBlock_TE-Connectivity.3dshapes/TerminalBlock_TE_1-282834-2_1x12_P2.54mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('TerminalBlock_TE-Connectivity : TerminalBlock_TE_1-282834-2_1x12_P2.54mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

