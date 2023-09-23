# escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
mt = int(input('Digite uma distancia em metros: '))
hm = mt / 100
dam = mt / 10
dm = mt * 10
cm = mt * 100
mm = mt * 1000

print('A medida de {:.1f}m corresponde a: {:.3f}km, {:.2f}hm, {:.2f}dam, {:.2f}dm, {:.2f}cm e {:.2f}mm' .format(mt, mt/1000, hm, dam, dm, cm, mm))