def lol_fun(lol_samp):
    mid = ['kayle', 'ziggs', 'nidalee']
    top = ['jax', 'fiora', 'nasus']
    alt = ['miss fortune', 'jinx', 'draven']
    jung = ['amumu', 'warwick', 'wukong']
    sup = ['morgana', 'zyra', 'braum']

    
    if lol_samp.lower() in mid:
        return 'orta koridor'
    elif lol_samp.lower() in top:
        return 'üst koridor'
    elif lol_samp.lower() in jung:
        return 'orman'
    elif lol_samp.lower() in sup:
        return 'destek'
    elif lol_samp.lower() in alt:
        return 'alt koridor'        
    else:
        return 'Bilemedim :('