# r(read)
file = open('i love python.txt', 'r', encoding='utf-8')
data = file.read()
print(data)
# ������ �о� �鿩�� data��� ������ ������ data ������ ����ϴ� �⺻���� ����
file.close()