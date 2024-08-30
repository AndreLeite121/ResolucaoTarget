import json

with open('/Users/andreleite/Desktop/ResolucaoTarget/3/Faturamento.json', 'r') as file:
    dados = json.load(file)

faturamentos = dados['faturamentos']


dias_com_faturamento = [valor for valor in faturamentos if valor > 0]

menor_valor = min(dias_com_faturamento) if dias_com_faturamento else None
maior_valor = max(dias_com_faturamento) if dias_com_faturamento else None

media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento) if dias_com_faturamento else 0

dias_acima_da_media = sum(1 for valor in dias_com_faturamento if valor > media_mensal)

print(f"Menor valor de faturamento: R${menor_valor:.2f}" if menor_valor is not None else "Nenhum dado de faturamento disponível")
print(f"Maior valor de faturamento: R${maior_valor:.2f}" if maior_valor is not None else "Nenhum dado de faturamento disponível")
print(f"Número de dias acima da média: {dias_acima_da_media}")
