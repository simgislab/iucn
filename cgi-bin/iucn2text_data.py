﻿#-*- encoding: utf-8 -*-
def iucndata():
    data = {
        ('EX',):"EX - нет никаких обоснованных сомнений в том, что его последняя особь погибла",
        ('CR',):"CR - Находящийся на грани полного исчезновения",
        ('EN',):"EN - Исчезающий",
        ('VU',):"VU - Уязвимый",
        ('CR','A'):"A - Сокращение численности",
        ('CR','A','1'):"1 - На основе наблюдений, экспертных оценок, заключений или предположений установлено, что сокращение численности не менее чем на 90% происходило за последние 10 лет или 3 поколения, что больше по продолжительности. При этом причины такого сокращения, будучи вполне обратимыми и объяснимыми, уже устранены. Это определяется на основании: ",
        ('CR','A','2'):"2 - На основе наблюдений, экспертных оценок, заключений или предположений установлено, что сокращение численности не менее чем на 80% происходило за последние 10 лет или 3 поколения, что больше по продолжительности. При этом само сокращение или его причины могут быть ещё не устранены, или не объяснимы, или не обратимы. Это определяется на основании: ",
        ('CR','A','3'):"3 - На основе прогнозов или предположений установлено, что сокращение численности не менее чем на 80% будет происходить за последующие 10 лет или 3 поколения, что больше по продолжительности (максимально до 100 лет). Это определяется на основании: ",
        ('CR','A','4'):"4 - На основе наблюдений, экспертных оценок, заключений, прогнозов или предположений установлено, что сокращение численности не менее чем на 80% происходило, и будет происходить за временной период, включающий прошлое и будущее, а именно – за любые 10 лет или 3 поколения, что больше по продолжительности (максимально до 100 лет в будущем). При этом само сокращение или его причины могут быть ещё не устранены, или не объяснимы, или не обратимы. Это определяется на основании: ",
        ('CR','A','1','a'):"a - Прямое наблюдение",
        ('CR','A','1','b'):"b - индекс обилия, приемлемый для таксона",
        ('CR','A','1','c'):"c - сокращение области распространения, области обитания и/или качества среды обитания",
        ('CR','A','1','d'):"d - реальный или потенциальный уровня эксплуатации",
        ('CR','A','1','e'):"e - влияние интродуцентов, гибридизации, патогенов, поллютантов, конкурентов или паразитов",
        ('CR','A','2','a'):"a - Прямое наблюдение",
        ('CR','A','2','b'):"b - индекс обилия, приемлемый для таксона",
        ('CR','A','2','c'):"c - сокращение области распространения, области обитания и/или качества среды обитания",
        ('CR','A','2','d'):"d - реальный или потенциальный уровня эксплуатации",
        ('CR','A','2','e'):"e - влияние интродуцентов, гибридизации, патогенов, поллютантов, конкурентов или паразитов",
        ('CR','A','3','b'):"b - индекс обилия, приемлемый для таксона",
        ('CR','A','3','c'):"c - сокращение области распространения, области обитания и/или качества среды обитания",
        ('CR','A','3','d'):"d - реальный или потенциальный уровня эксплуатации",
        ('CR','A','3','e'):"e - влияние интродуцентов, гибридизации, патогенов, поллютантов, конкурентов или паразитов",
        ('CR','A','4','a'):"a - Прямое наблюдение",
        ('CR','A','4','b'):"b - индекс обилия, приемлемый для таксона",
        ('CR','A','4','c'):"c - сокращение области распространения, области обитания и/или качества среды обитания",
        ('CR','A','4','d'):"d - реальный или потенциальный уровня эксплуатации",
        ('CR','A','4','e'):"e - влияние интродуцентов, гибридизации, патогенов, поллютантов, конкурентов или паразитов",
        ('CR','B'):"B - Ограничение ареала при наличии:",
        ('CR','B','1'):"1 - На основе экспертных оценок установлено, что область распространения составляет менее чем 100 км2. При этом: ",
        ('CR','B','1','a'):"a - сильно фрагментирована или состоит лишь из 1 локалитета",
        ('CR','B','1','b'):"b - На основе наблюдений, заключений или прогнозов установлено продолжающееся снижение любых из следующих показателей:",
        ('CR','B','1','b','i'):"i - области распространения",
        ('CR','B','1','b','ii'):"ii - области обитания",
        ('CR','B','1','b','iii'):"iii - площади, протяжённости и/или качества среды обитания",
        ('CR','B','1','b','iv'):"iv - количества локалитетов или популяций",
        ('CR','B','1','b','v'):"v - количества половозрелых особей",
        ('CR','B','1','c'):"c - Экстремальные колебания любых из следующих показателей",        ('CR','B','1','c','i'):"i - области распространения",
        ('CR','B','1','c','ii'):"ii - области обитания",
        ('CR','B','1','c','iii'):"iii - количества локалитетов или популяций",
        ('CR','B','1','c','iv'):"iv - количества половозрелых особей",
        ('CR','B','2'):"2 - На основе экспертных оценок установлено, что область распространения составляет менее чем 500 км2. При этом: ",
        ('CR','B','2','a'):"a - сильно фрагментирована или состоит не более чем из 5 локалитетов",
        ('CR','B','2','b'):"b - На основе наблюдений, заключений или прогнозов установлено продолжающееся снижение любых из следующих показателей:",
        ('CR','B','2','c'):"c - Экстремальные колебания любых из следующих показателей",
        ('CR','B','2','b','i'):"i - области распространения",
        ('CR','B','2','b','ii'):"ii - области обитания",
        ('CR','B','2','b','iii'):"iii - площади, протяжённости и/или качества среды обитания",
        ('CR','B','2','b','iv'):"iv - количества локалитетов или популяций",
        ('CR','B','2','b','v'):"v - количества половозрелых особей",
        ('CR','B','2','c','i'):"i - области распространения",
        ('CR','B','2','c','ii'):"ii - области обитания",
        ('CR','B','2','c','iii'):"iii - количества локалитетов или популяций",
        ('CR','B','2','c','iv'):"iv - количества половозрелых особей",
        ('CR','C'):"C - Ограничение численности, когда на основе экспертных оценок установлено, что численность составляет менее чем 250 половозрелых особей при наличии любых из следующих условий: ",
        ('CR','C','1'):"1 - На основе экспертных оценок установлено продолжающееся снижение численности не менее чем на 25% за 3 года или 1 поколение, что больше по продолжительности (максимально до 100 лет в будущем).",
        ('CR','C','2'):"2 - На основе наблюдений, заключений или прогнозов установлено продолжающееся снижение численности при наличии:",
        ('CR','C','2','a'):"a - Структура популяций:",
        ('CR','C','2','a','i'):"i - на основе экспертных оценок установлено, что не существует популяций, состоящих более чем из 50 половозрелых особей",
        ('CR','C','2','a','i'):"i - не менее 90% половозрелых особей находится в одной популяции",
        ('CR','C','2','b'):"b - Сильные колебания количества половозрелых особей",
        ('CR','D'):"D - Сильное ограничение численности, когда на основе экспертных оценок установлено, что численность составляет менее 50 половозрелых особей",
        ('CR','E'):"E - Количественный анализ показывает не менее 50% вероятности исчезновения таксона в дикой природе за 10 лет или 3 поколения, что больше по продолжительности (максимально до 100 лет)",
        
        ('EN','A'):"A - Сокращение численности",
        ('EN','A','1'):"1 - На основе наблюдений, экспертных оценок, заключений или предположений установлено, что сокращение численности не менее чем на 70% происходило за последние 10 лет или 3 поколения, что больше по продолжительности. При этом причины такого сокращения, будучи вполне обратимыми и объяснимыми, уже устранены. Это определяется на основании: ",
        ('EN','A','2'):"2 - На основе наблюдений, экспертных оценок, заключений или предположений установлено, что сокращение численности не менее чем на 50% происходило за последние 10 лет или 3 поколения, что больше по продолжительности. При этом само сокращение или его причины могут быть ещё не устранены, или не объяснимы, или не обратимы. Это определяется на основании: ",
        ('EN','A','3'):"3 - На основе прогнозов или предположений установлено, что сокращение численности не менее чем на 50% будет происходить за последующие 10 лет или 3 поколения, что больше по продолжительности (максимально до 100 лет). Это определяется на основании: ",
        ('EN','A','4'):"4 - На основе наблюдений, экспертных оценок, заключений, прогнозов или предположений установлено, что сокращение численности не менее чем на 50% происходило, и будет происходить за временной период, включающий прошлое и будущее, а именно – за любые 10 лет или 3 поколения, что больше по продолжительности (максимально до 100 лет в будущем). При этом само сокращение или его причины могут быть ещё не устранены, или не объяснимы, или не обратимы. Это определяется на основании: ",
        ('EN','A','1','a'):"a - Прямое наблюдение",
        ('EN','A','1','b'):"b - индекс обилия, приемлемый для таксона",
        ('EN','A','1','c'):"c - сокращение области распространения, области обитания и/или качества среды обитания",
        ('EN','A','1','d'):"d - реальный или потенциальный уровня эксплуатации",
        ('EN','A','1','e'):"e - влияние интродуцентов, гибридизации, патогенов, поллютантов, конкурентов или паразитов",
        ('EN','A','2','a'):"a - Прямое наблюдение",
        ('EN','A','2','b'):"b - индекс обилия, приемлемый для таксона",
        ('EN','A','2','c'):"c - сокращение области распространения, области обитания и/или качества среды обитания",
        ('EN','A','2','d'):"d - реальный или потенциальный уровня эксплуатации",
        ('EN','A','2','e'):"e - влияние интродуцентов, гибридизации, патогенов, поллютантов, конкурентов или паразитов",
        ('EN','A','3','b'):"b - индекс обилия, приемлемый для таксона",
        ('EN','A','3','c'):"c - сокращение области распространения, области обитания и/или качества среды обитания",
        ('EN','A','3','d'):"d - реальный или потенциальный уровня эксплуатации",
        ('EN','A','3','e'):"e - влияние интродуцентов, гибридизации, патогенов, поллютантов, конкурентов или паразитов",
        ('EN','A','4','a'):"a - Прямое наблюдение",
        ('EN','A','4','b'):"b - индекс обилия, приемлемый для таксона",
        ('EN','A','4','c'):"c - сокращение области распространения, области обитания и/или качества среды обитания",
        ('EN','A','4','d'):"d - реальный или потенциальный уровня эксплуатации",
        ('EN','A','4','e'):"e - влияние интродуцентов, гибридизации, патогенов, поллютантов, конкурентов или паразитов",
        ('EN','B'):"B - Ограничение ареала",
        ('EN','B','1'):"1 - На основе экспертных оценок установлено, что область распространения составляет менее чем 5000 км2. При этом: ",
        ('EN','B','2'):"2 - На основе экспертных оценок установлено, что область распространения составляет менее чем 500 км2. При этом: ",
        ('EN','B','1','a'):"a - сильно фрагментирована или состоит не более чем из 5 локалитетов",
        ('EN','B','1','b'):"b - На основе наблюдений, заключений или прогнозов установлено продолжающееся снижение любых из следующих показателей:",
        ('EN','B','1','c'):"c - Экстремальные флуктуации любых из следующих показателей",
        ('EN','B','1','b','i'):"i - области распространения",
        ('EN','B','1','b','ii'):"ii - области обитания",
        ('EN','B','1','b','iii'):"iii - площади, протяжённости и/или качества среды обитания",
        ('EN','B','1','b','iv'):"iv - количества локалитетов или популяций",
        ('EN','B','1','b','v'):"v - количества половозрелых особей",
        ('EN','B','1','c','i'):"i - области распространения",
        ('EN','B','1','c','ii'):"ii - области обитания",
        ('EN','B','1','c','iii'):"iii - количества локалитетов или популяций",
        ('EN','B','1','c','iv'):"iv - количества половозрелых особей",
        ('EN','B','2','a'):"a - сильно фрагментирована или состоит не более чем из 5 локалитетов",
        ('EN','B','2','b'):"b - На основе наблюдений, заключений или прогнозов установлено продолжающееся снижение любых из следующих показателей:",
        ('EN','B','2','b','i'):"i - области распространения",
        ('EN','B','2','b','ii'):"ii - области обитания",
        ('EN','B','2','b','iii'):"iii - площади, протяжённости и/или качества среды обитания",
        ('EN','B','2','b','iv'):"iv - количества локалитетов или популяций",
        ('EN','B','2','b','v'):"v - количества половозрелых особей",
        ('EN','B','2','c'):"c - Экстремальные флуктуации любых из следующих показателей",
        ('EN','B','2','c','i'):"i - области распространения",
        ('EN','B','2','c','ii'):"ii - области обитания",
        ('EN','B','2','c','iii'):"iii - количества локалитетов или популяций",
        ('EN','B','2','c','iv'):"iv - количества половозрелых особей",
        ('EN','C'):"C - Ограничение численности, когда на основе экспертных оценок установлено, что численность составляет менее чем 2500 половозрелых особей при наличии любых из следующих условий: ",
        ('EN','C','1'):"1 - На основе экспертных оценок установлено продолжающееся снижение численности не менее чем на 20% за 5 лет  или 2 поколения, что больше по продолжительности (максимально до 100 лет в будущем).",
        ('EN','C','2'):"2 - На основе наблюдений, заключений или прогнозов установлено продолжающееся снижение численности при наличии:",
        ('EN','C','2','a'):"a - Структура популяций:",
        ('EN','C','2','a','i'):"i - на основе экспертных оценок установлено, что не существует популяций, состоящих более чем из 250 половозрелых особей",
        ('EN','C','2','a','i'):"i - не менее 95% половозрелых особей находится в одной популяции",
        ('EN','C','2','b'):"b - Сильные колебания количества половозрелых особей",
        ('EN','D'):"D - Сильное ограничение численности, когда на основе экспертных оценок установлено, что численность составляет менее 250 половозрелых особей",
        ('EN','E'):"E - Количественный анализ показывает не менее 20% вероятности исчезновения таксона в дикой природе за 20 лет или 5 поколения, что больше по продолжительности (максимально до 100 лет)",
        
        ('VU','A'):"A - Сокращение численности",
        ('VU','A','1'):"1 - На основе наблюдений, экспертных оценок, заключений или предположений установлено, что сокращение численности не менее чем на 50% происходило за последние 10 лет или 3 поколения, что больше по продолжительности. При этом причины такого сокращения, будучи вполне обратимыми и объяснимыми, уже устранены. Это определяется на основании: ",
        ('VU','A','2'):"2 - На основе наблюдений, экспертных оценок, заключений или предположений установлено, что сокращение численности не менее чем на 30% происходило за последние 10 лет или 3 поколения, что больше по продолжительности. При этом само сокращение или его причины могут быть ещё не устранены, или не объяснимы, или не обратимы. Это определяется на основании: ",
        ('VU','A','3'):"3 - На основе прогнозов или предположений установлено, что сокращение численности не менее чем на 30% будет происходить за последующие 10 лет или 3 поколения, что больше по продолжительности (максимально до 100 лет). Это определяется на основании: ",
        ('VU','A','4'):"4 - На основе наблюдений, экспертных оценок, заключений, прогнозов или предположений установлено, что сокращение численности не менее чем на 30% происходило, и будет происходить за временной период, включающий прошлое и будущее, а именно – за любые 10 лет или 3 поколения, что больше по продолжительности (максимально до 100 лет в будущем). При этом само сокращение или его причины могут быть ещё не устранены, или не объяснимы, или не обратимы. Это определяется на основании: ",
        ('VU','A','1','a'):"a - Прямое наблюдение",
        ('VU','A','1','b'):"b - индекс обилия, приемлемый для таксона",
        ('VU','A','1','c'):"c - сокращение области распространения, области обитания и/или качества среды обитания",
        ('VU','A','1','d'):"d - реальный или потенциальный уровня эксплуатации",
        ('VU','A','1','e'):"e - влияние интродуцентов, гибридизации, патогенов, поллютантов, конкурентов или паразитов",
        ('VU','A','2','a'):"a - Прямое наблюдение",
        ('VU','A','2','b'):"b - индекс обилия, приемлемый для таксона",
        ('VU','A','2','c'):"c - сокращение области распространения, области обитания и/или качества среды обитания",
        ('VU','A','2','d'):"d - реальный или потенциальный уровня эксплуатации",
        ('VU','A','2','e'):"e - влияние интродуцентов, гибридизации, патогенов, поллютантов, конкурентов или паразитов",
        ('VU','A','3','b'):"b - индекс обилия, приемлемый для таксона",
        ('VU','A','3','c'):"c - сокращение области распространения, области обитания и/или качества среды обитания",
        ('VU','A','3','d'):"d - реальный или потенциальный уровня эксплуатации",
        ('VU','A','3','e'):"e - влияние интродуцентов, гибридизации, патогенов, поллютантов, конкурентов или паразитов",
        ('VU','A','4','a'):"a - Прямое наблюдение",
        ('VU','A','4','b'):"b - индекс обилия, приемлемый для таксона",
        ('VU','A','4','c'):"c - сокращение области распространения, области обитания и/или качества среды обитания",
        ('VU','A','4','d'):"d - реальный или потенциальный уровня эксплуатации",
        ('VU','A','4','e'):"e - влияние интродуцентов, гибридизации, патогенов, поллютантов, конкурентов или паразитов",
        ('VU','B'):"B - Ограничение ареала",
        ('VU','B','1'):"1 - На основе экспертных оценок установлено, что область распространения составляет менее чем 10000 км2. При этом: ",
        ('VU','B','1','a'):"a - сильно фрагментирована или состоит не более чем из 10 локалитетов",
        ('VU','B','1','b'):"b - На основе наблюдений, заключений или прогнозов установлено продолжающееся снижение любых из следующих показателей:",
        ('VU','B','1','c'):"c - Экстремальные флуктуации любых из следующих показателей",
        ('VU','B','1','b','i'):"i - области распространения",
        ('VU','B','1','b','ii'):"ii - области обитания",
        ('VU','B','1','b','iii'):"iii - площади, протяжённости и/или качества среды обитания",
        ('VU','B','1','b','iv'):"iv - количества локалитетов или популяций",
        ('VU','B','1','b','v'):"v - количества половозрелых особей",
        ('VU','B','1','c','i'):"i - области распространения",
        ('VU','B','1','c','ii'):"ii - области обитания",
        ('VU','B','1','c','iii'):"iii - количества локалитетов или популяций",
        ('VU','B','1','c','iv'):"iv - количества половозрелых особей",
        ('VU','B','2'):"2 - На основе экспертных оценок установлено, что область распространения составляет менее чем 2000 км2. При этом: ",
        ('VU','B','2','a'):"a - сильно фрагментирована или состоит не более чем из 10 локалитетов",
        ('VU','B','2','b'):"b - На основе наблюдений, заключений или прогнозов установлено продолжающееся снижение любых из следующих показателей:",
        ('VU','B','2','c'):"c - Экстремальные флуктуации любых из следующих показателей",
        ('VU','B','2','b','i'):"i - области распространения",
        ('VU','B','2','b','ii'):"ii - области обитания",
        ('VU','B','2','b','iii'):"iii - площади, протяжённости и/или качества среды обитания",
        ('VU','B','2','b','iv'):"iv - количества локалитетов или популяций",
        ('VU','B','2','b','v'):"v - количества половозрелых особей",
        ('VU','B','2','c','i'):"i - области распространения",
        ('VU','B','2','c','ii'):"ii - области обитания",
        ('VU','B','2','c','iii'):"iii - количества локалитетов или популяций",
        ('VU','B','2','c','iv'):"iv - количества половозрелых особей",
        ('VU','C'):"C - Ограничение численности, когда на основе экспертных оценок установлено, что численность составляет менее чем 10000 половозрелых особей при наличии любых из следующих условий: ",
        ('VU','C','1'):"1 - На основе экспертных оценок установлено продолжающееся снижение численности не менее чем на 10% за 10 лет  или 3 поколения, что больше по продолжительности (максимально до 100 лет в будущем).",
        ('VU','C','2'):"2 - На основе наблюдений, заключений или прогнозов установлено продолжающееся снижение численности при наличии:",
        ('VU','C','2','a'):"a - Структура популяций:",
        ('VU','C','2','a','i'):"i - на основе экспертных оценок установлено, что не существует популяций, состоящих более чем из 1000 половозрелых особей",
        ('VU','C','2','a','ii'):"ii - все половозрелые особи находятся в одной популяции",
        ('VU','C','2','b'):"b - Сильные колебания количества половозрелых особей",
        ('VU','D'):"D - Ограничение численности и/или ареала при наличие:",
        ('VU','D','1'):"1 - На основе экспертных оценок установлено, что численность составляет менее чем 1000 половозрелых особей",
        ('VU','D','2'):"2 - Область обитания составляет обычно менее чем 20 км2 или состоит обычно не более чем из 5 локалитетов, что способно под воздействием антропогенных или случайных факторов привести к критическому состоянию или даже исчезновению таксона за небольшой период времени в будущем.",
        ('VU','E'):"E - Количественный анализ показывает не менее 10% вероятности исчезновения таксона в дикой природе за 100 лет",
    }
    return data