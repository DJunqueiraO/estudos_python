import os.path

extract = ''
extract_path = '../../input/extract.txt'

if os.path.exists(extract_path):
    with open(extract_path, 'r') as f:
        extract = f.read()

    def calcular_soma(lista):

        result = 0

        for a, b in lista:
            valor_to_add = eval(a.replace(',', '.'))
            current_result = result + valor_to_add
            sentence = f'{str(round(result, 2)).rjust(10)}'
            sentence += f'\t+\t{str(round(valor_to_add, 2)).rjust(5)}'
            sentence += f'\t= {str(round(current_result, 2)).rjust(10)}'
            sentence += f' ->\t** {a}\t{b} **'
            print(sentence)
            result = current_result

        return result

    def convert_valores_to_list(valores_):

        def on_map(x):
            x = x.split(';')

            return x[0].replace(' ', '').replace('\t', ''), x[1].replace(' ', '') if len(x) > 1 else None

        return list(filter(lambda x: x[0] != '', map(on_map, valores_.split('\n'))))

    print(f"Dívida total: {calcular_soma(convert_valores_to_list(extract))}")






