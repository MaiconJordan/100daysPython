# PRojeto python usando expressões regulares
import re

texto = ''' 
Celo, você é foda
Tonight every street in the city
Ends up where I don't wanna be
Signs tell me how far I am from you
Even though you're all that I see
Yeah, yeah, yeah
Air Force Low, eu não fodo com Mid
I keep it low, eu mal posto no feed
Ela é minha boo, ela ama meu drip
Toda de Gucci, ela só anda chique
Atira nesse mano até dar tendinite
Se eu pegar moscando não vai ter revide
'To na pracinha do Campana City (Yeah)
Igual Super Mario, aqui nós tem Luigi
Ela 'tá na minha mão pique Nintendo Switch
Both hands on my dick, ela faz sanduíche
Eu só amo esse dinheiro, eu não amo essa bitch
Sua bad trip eu corto igual no Bleach
Eles querem copiar meu drip, yeah, yeah (Drip)
Stussy Preme é o que tem no cabide
Fazendo skrr pique Need for Speed
Pelé no ROCAM, passei fazendo drift (Uh)
Air Force Low, eu não fodo com Mid
I keep it low, eu mal posto no feed
Ela é minha boo, ela ama meu drip (Uh, yeah, yeah)
Toda de Gucci, ela só anda chique
Atira nesse mano até dar tendinite
Se eu pegar moscando não vai ter revide
'To na pracinha do Campana City (Yeah)
Igual Super Mario, aqui nós tem Luigi (eu pago silicones)
ela não tem peito grande
Ela tem piercing no mamilo, a bunda mó gigante
'Tá com mano aqui porque eu tenho grana
Got racks on me, essa mina ama
Eu 'to bebendo codein' com refrigerante (Lean)
Fumo skunk e me deixa nós na paz de Gandhi
Eu boto fogo no stu', apaga o microfone
Então taca a bag ali que 'tá vindo os homi
Meu mano, eu sou rapper, não me chame de trapper
Esses mano só fala, mas eles são capper
'To sentado na mesa com Ne, Emicida, Fióti, falando de business
Minha bitch é mó fitness nós fuma esse picles
Skin care na suíte
E o boi no Twitter falando bullshit
Eu e os amigo 'tá rindo do print
Negão palhaço pagando de bitch
Já 'tá flopado, nunca mais eu vi
Derrubei Xan no meu copo de lean
A codeína fudendo o meu rim
Mano falido querendo o meu fim
Vejo que isso 'tá longe do fim
Mãe, continue orando por mim
Mãe, continue orando por mim
Air Force Low, eu não fodo com Mid (Yeah, yeah, yeah)
I keep it low, eu mal posto no feed (Yeah)
Ela é minha boo, ela ama meu drip
Toda de Gucci, ela só anda chique
Atira nesse mano até dar tendinite (Oh, oh, oh)
Se eu pegar moscando não vai ter revide
'To na pracinha do Campana City (Yeah)
Igual Super Mario, aqui nós tem Luigi
Ela 'tá na minha mão pique Nintendo Switch
'''

match = re.findall("a", texto)
count = len(match)
print(f"A palavra 'a' aparece {count} vezes no texto")



resultado = len(re.findall(r'\bluigi\b', texto, re.IGNORECASE))
print(resultado)
