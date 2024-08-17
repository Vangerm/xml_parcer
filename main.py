import xml.etree.ElementTree as ET
import csv


def indent(elem: any, level: int = 0) -> None:
    '''создает красивый xml c отступами'''
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


def csv_dict() -> dict:
    result = {}
    with open('input.csv', encoding='utf-8') as f:
        csv_file = csv.DictReader(f, delimiter=',')
        for item in csv_file:
            result.setdefault(item['set'], []).append(item['code'])
    return result


def app_cis(elem: any) -> None:
    pack_content_item
    for k, v in csv_dict().items():
        new_item = ET.Element('cis')
        if flag_first_chek:
            new_item.text = line[0].strip()[1:]
            flag_first_chek = False
        else:
            new_item.text = line[0].strip()
        elem[0][1].insert(1, new_item)


if __name__ == '__main__':
    tree = ET.parse('Формирование_наборов.xml')
    root = tree.getroot()

    app_cis()

    indent(root)
    tree.write('output.xml', encoding="utf-8", xml_declaration=True)