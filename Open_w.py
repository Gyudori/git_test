#w(wirte)

file = open('i love python.txt', 'w', encoding= 'utf-8')
file.write('Hello, world!\n')
file.write('Welcome to Python!!\n')
file.close() # file.close()�� �Ⱦ��� ���α׷��� ����ɶ����� �ش� ���Ͽ� ���� �Ұ���

# r(read)
file = open('i love python.txt', 'r', encoding= 'utf-8')
data = file.read()
print(data)
# ������ �о� �鿩�� data��� ������ ������ data ������ ����ϴ� �⺻���� ����
file.close()