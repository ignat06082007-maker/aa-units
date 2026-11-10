return {
	['Special_Effect_List'] = {
		["Bleed Amplification"] = {
			note = 'Bleed Amplification:<br>Makes enemies take x5 bleed damage for the duration of the effect.',
			link = "Effects#Bleed_Amplification"
		},
		["Slow"] = {
			note = 'Slow:<br>The speed of enemies is reduced for the duration of the effect.',
			link = "Effects#Slow"
		},
		["Stun"] = {
			note = 'Stun:<br>Freezes enemies for the duration of the effect.',
			link = "Effects#Stun"
		},
		["Cursed (15%)"] = {
			note = 'Cursed:<br>Makes enemies take 15% more {{Tower_Infobox/Damage_type|magic}} damage.',
			link = "Effects#Cursed"
		},
		["Cursed (30%)"] = {
			note = 'Cursed:<br>Makes enemies take 30% more {{Tower_Infobox/Damage_type|magic}} damage.',
			link = "Effects#Cursed"
		},
		["Confused"] = {
			note = 'Confused:<br>Makes all enemies in range walk backwards for 5 seconds.',
			link = "Effects#Confused"
		},
		["Knockback"] = {
			note = 'Knockback:<br>Pushes enemies towards their spawn.', 
			link = "Effects#Knockback"
		},
		["Freeze"] = {
			note = 'Freeze:<br>Freezes enemies for the duration of the effect (Has a cooldown of 10-12 seconds).<br><br>Conflicts with [[Lulu (Geass)|Confusion]] ability (by [[Lulu (Geass)|Lulu]]), and other users dealing Freeze/Timestop.',
			link = "Effects#Freeze"
		},
		["Timestop"] = {
			note = 'Timestop:<br>Freezes enemy for duration of the effect (Has a cooldown of 10-12 seconds).<br><br>Conflicts with [[Lulu (Geass)|Confusion]] ability (by [[Lulu (Geass)|Lulu]]), and other users dealing Freeze/Timestop.',
			link = "Effects#Timestop"
		},
		["Dismembered"] = {
			note = 'Dismembered:<br>Brutally removes a random limb from the enemy and causes the enemy to take 20% more {{Tower_Infobox/Damage_type|physical}} damage permanently (does not stack)', link = "Effects#Dismembered"
		},
		["Motivate"] = {
			note = 'Motivate:<br>Each attack buffs all allies in range by 15% damage or 10% range for 10 seconds, same effects do not stack.', 
			link = "Effects#Motivate"
		},
		["Battlelust"] = {
			note = 'Battlelust:<br>Each attack increases damage by 5% up to 25% as long as the unit has a target.',
			link = "Effects#Battlelust"
		},
		["Shatter"] = {
			note = 'Shatter:<br>Removes all shield instances on enemies when hit.',
			link = "Effects#Shatter"
		},
		["Snatched"] = {
			note = 'Snatched:<br>Each attack increases damage by 3% up to 33% (99% on a max upgrade) for 90 seconds.',
			link = 'Effects#Snatched'
		},
		["Mind Control"] = {
			note = 'Walk Back:<br>Forces enemies with a 10% chance in range to walk back for 1.5 seconds.', 
			link = 'Effects#Mind_Control'
		},
		["Hexed (20%)"] = {
			note = 'Hexed:<br>Curses enemy and debuffs which causes the enemy to take 30% more {{Tower_Infobox/Damage_type|magic}} damage permanently (does not stack)',
			link = "Effects#Hexed"
		},
		["Hexed (25%)"] = 	{
			note = 'Hexed:<br>Curses enemy and debuffs which causes the enemy to take 30% more {{Tower_Infobox/Damage_type|magic}} damage permanently (does not stack)',
			link = "Effects#Hexed"
		},
		["Sunshine"] = {
			note = 'Sunshine:<br>Damage and range increases every wave. Up to 15 waves. Receives 2.25x more damage and 1.67x range at maximum sunshine.',
			link = "Effects#Sunshine"
		},
		["Wither"] = {
			note = 'Wither:<br>Prevents regen enemies from healing.',
			link = "Effects#Wither"
		},
		["OverCrit"] = {
			note = 'OverCrit:<br>Guarantees a crit on enemies that are currently bleeding.',
			link = "Effects#OverCrit"
		},
		["Unconscious"] = {
			note = 'Unconscious:<br>Makes the enemy unconscious for 0.5s.',
			link = "Effects#Stun"},
		["Wild Card"] = {
			note = 'Applies fire, slow, bleed, freeze, or knockback randomly.',
			link = "Effects"
		}
	},
 --[[
		['Effect'] = {
			['Name'] = 'Burn Bleed',
			['Ticks'] = 10,
			['Multiplier'] = 0.025
		}
,
		['Special_Effect'] = {
			['Name'] = 'Stun',
		}
	--]]
	
	["kasuga:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6,
	},
    ["kasuga:two"] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 12,
		['Hits'] = 3
	},
    ["kasuga:three"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 12,
		['Hits'] = 1
	},
	["dokuro:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8,
	},
    ["dokuro:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 13,
	},
    ["rikka:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 12,
	},
    ["rikka:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 16,
		['Hits'] = 4,
	},
    ["rikka:three"] = {
		['AOE_TYPE'] = 'AoE (Full)',
		['Hits'] = 4,
	},
    ["rokuhira:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10,
		['Hits'] = 3
	},
    ["rokuhira:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 12,
		['Hits'] = 3
	},
    ["rokuhira:three"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 14,
		['Hits'] = 1
	},
    ["rokuhira:four"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 18,
		['Hits'] = 1
	},
	["hei:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 7,
	},
	["hei:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10,
		['Hits'] = 2
	},
	["hei:three"] = {
		['AOE_TYPE'] = 'AoE (Full)',
		['Hits'] = 4
	},
    ["shidou:one"] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 10,
	},
    ["shidou:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 15,
	},
    ["mechamaru:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 9,
	},
    ["mechamaru:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 12,
		['Hits'] = 3
	},
    ["mechamaru:three"] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 60,
		['Hits'] = 3
	},
	["toji:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['Hits'] = 3
	},
	["toji:two"] = {
		['Hits'] = 2
	},
	["toji:three"] = {
		['Hits'] = 3
	},
	["toji:four"] = {
		['Hits'] = 1
	},
    ["megumi_2:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['Special_Effect'] = {
			['Name'] = 'Cursed (30%)'
		}
	},
    ["megumi_2:two"] = {
		['Hits'] = 3,
		['Special_Effect'] = {
			['Name'] = 'Cursed (30%)'
		}
	},
    ["megumi_2:three"] = {
		['Hits'] = 1,
		['Special_Effect'] = {
			['Name'] = 'Cursed (30%)'
		}
	},
	["giselle:one"] = {
		['AOE_TYPE'] = 'AoE (Line)'
	},
	["giselle:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)'
	},
	["giselle:three"] = {
	},
    ["hakari:one"] = {
		['AOE_TYPE'] = 'AoE (Line)'
	},
    ["hakari:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)'
	},
    ["hakari:three"] = {
		['Hits'] = 3
	},
	["rukia_2:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 9,
		['Hits'] = 3
	},
	["rukia_2:two"] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 60,
		['Hits'] = 2
	},
	["rukia_2:three"] = {
		['AOE_TYPE'] = 'AoE (Full)',
		['Hits'] = 2
	},
	["sato:one"] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['Hits'] = 3
	},
	["sato:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['Hits'] = 1
	},
	["sato:three"] = {
		['Hits'] = 3
	},
	["sato:four"] = {
    	['Effect'] = {
			['Name'] = 'Burn',
			['Ticks'] = 4,
			['Multiplier'] = 0.1
		}
	},
	["sakamoto:one"] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 60,
	},
	["sakamoto:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 7,
		['Hits'] = 3
	},
	["sakamoto:three"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10,
		['Hits'] = 1
	},
	["sakamoto:four"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 12,
		['Hits'] = 4
	},
	["sakamoto:five"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 16,
		['Hits'] = 3
	},
	["nagumo:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8,
	},
	["nagumo:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['Hits'] = 3,
		['radius'] = 10,
	},
	["nagumo_evo:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8,
		['Special_Effect'] = {
			['Name'] = 'Dismembered',
		}
	},
	["nagumo_evo:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['Hits'] = 3,
		['radius'] = 10,
		['Special_Effect'] = {
			['Name'] = 'Dismembered',
		}
	},
    ["nagumo_evo:three"] = {
    	['AOE_TYPE'] = 'AoE (Circle)',
		['Hits'] = 3,
		['radius'] = 12,
		['Special_Effect'] = {
			['Name'] = 'Dismembered'
		}
	},
    ["gaku:one"] = {
     	['AOE_TYPE'] = 'AoE (Circle)',
     	['radius'] = 8
	},
    ["gaku:two"] = {
     	['AOE_TYPE'] = 'AoE (Circle)',
     	['radius'] = 13
	},
     ["gaku:three"] = {
      	['AOE_TYPE'] = 'AoE (Circle)',
      	['Hits'] = 2,
      	['radius'] = 15
	},
    ["osaragi:one"] = {
      	['AOE_TYPE'] = 'AoE (Circle)',
      	['radius'] = 7,
      	['Effect'] = {
			['Name'] = 'Bleed',
			['Ticks'] = 6,
			['Multiplier'] = 0.058333333333333333333
		}
	},
    ["osaragi:two"] = {
      	['AOE_TYPE'] = 'AoE (Cone)',
      	['Hits'] = 5,
      	['Effect'] = {
			['Name'] = 'Bleed',
			['Ticks'] = 6,
			['Multiplier'] = 0.058333333333333333333
		}
	},
    ["osaragi:three"] = {
      	['AOE_TYPE'] = 'AoE (Circle)',
      	['Hits'] = 5,
      	['radius'] = 15,
      	['Effect'] = {
			['Name'] = 'Bleed',
			['Ticks'] = 6,
			['Multiplier'] = 0.058333333333333333333
		}
	},
    ["feitan:one"] = {
      	['AOE_TYPE'] = 'AoE (Circle)',
      	['radius'] = 6,
	},
    ["feitan:two"] = {
      	['AOE_TYPE'] = 'AoE (Circle)',
      	['radius'] = 8,
      	['Hits'] = 4,
	},
    ["feitan:three"] = {
      	['AOE_TYPE'] = 'AoE (Full)',
      	['Hits'] = 6,
      	['Effect'] = {
			['Name'] = 'Burn',
			['Ticks'] = 6,
			['Multiplier'] = 0.4/6
		}
	},
    ["ragna:one"] = {
      	['AOE_TYPE'] = 'AoE (Circle)',
      	['radius'] = 8,
      	['Hits'] = 3
	},
    ["ragna:two"] = {
      	['AOE_TYPE'] = 'AoE (Line)',
      	['width'] = 2.5,
      	['Hits'] = 3
	},
    ["ragna:three"] = {
      	['AOE_TYPE'] = 'AoE (Circle)',
      	['Hits'] = 3
	},
    ["starlia:one"] = {
      	['AOE_TYPE'] = 'AoE (Circle)',
      	['radius'] = 8,
	},
    ["starlia:two"] = {
      	['AOE_TYPE'] = 'AoE (Circle)',
      	['radius'] = 10,
	},
    ["starlia:three"] = {
      	['AOE_TYPE'] = 'AoE (Circle)',
      	['Hits'] = 3
	},
    
    ["aizen_transcended:one"] = {
      	['AOE_TYPE'] = 'AoE (Circle)',
      	['radius'] = 8,
      	['Hits'] = 3
	},
    ["aizen_transcended:two"] = {
      	['AOE_TYPE'] = 'AoE (Cone)',
      	['angle'] = 60,
      	['Hits'] = 2
	},
    ["aizen_transcended:three"] = {
      	['AOE_TYPE'] = 'AoE (Cone)',
      	['angle'] = 60,
      	['Hits'] = 3
	},
    ["aizen_transcended:four"] = {
      	['AOE_TYPE'] = 'AoE (Full)',
      	['Hits'] = 2
	},
    ["buddha:one"] = {
      	['AOE_TYPE'] = 'AoE (Circle)',
      	['radius'] = 10,
	},
    ["buddha:bleed"] = {
      	['AOE_TYPE'] = 'AoE (Circle)',
      	['radius'] = 18,
      	['Effect'] = {
			['Name'] = 'Bleed',
			['Ticks'] = 3,
			['Multiplier'] = 0.1
		}
	},
    ["buddha:hybrid"] = {
      	['AOE_TYPE'] = 'AoE (Line)',
      	['width'] = 10,
	},
    ["judar:one"] = {
      	['AOE_TYPE'] = 'AoE (Circle)',
      	['radius'] = 8,
      	['Hits'] = 2
	},
    ["judar:two"] = {
      	['AOE_TYPE'] = 'AoE (Circle)',
      	['radius'] = 12,
      	['Hits'] = 1
	},
    ["judar:three"] = {
      	['AOE_TYPE'] = 'AoE (Cone)',
      	['angle'] = 50,
      	['Hits'] = 3
	},
    ["judar:four"] = {
      	['AOE_TYPE'] = 'AoE (Full)',
      	['Hits'] = 3
	},
    ["nokotan:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 7,
		['Hits'] = 2
	},
    ["nokotan:two"] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 16,
		['Hits'] = 4
	},
    ["nokotan:three"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 14,
		['Hits'] = 3
	},
    ["frieren:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8
	},
    ["frieren:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 9
	},
    ["frieren:three"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['Hits'] = 4,
		['radius'] = 11
	},
    ["vanilla_ice:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10
	},
    ["vanilla_ice:two"] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 60
	},
     ["vanilla_ice:three"] = {
		['AOE_TYPE'] = 'AoE (Full)',
		['Hits'] = 5
	},
    ["monet:one"] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 45,
		['Special_Effect'] = {
			['Name'] = 'Slow',
			['Duration'] = 4,
			['Influence'] = 0.5
		}
	},
    ["monet:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 9,
		['Special_Effect'] = {
			['Name'] = 'Slow',
			['Duration'] = 4,
			['Influence'] = 0.5
		}
	},
    ["monet:three"] = {
    	['AOE_TYPE'] = 'AoE (Circle)',
    	['Hits'] = 2,
        ['radius'] = 12,
		['Special_Effect'] = {
			['Name'] = 'Slow',
			['Duration'] = 4,
			['Influence'] = 0.5
		}
	},
    ["honey:one"] = {
		['AOE_TYPE'] = 'Single',
    },
    ["gremmy:one"] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 60,
		['Hits'] = 3,
    },
    ["gremmy:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 14,
		['Hits'] = 2,
    },
    ["gremmy:three"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 20,
		['Hits'] = 1,
    },
    ["rebirth_grimmjow:one"] ={
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 45,
		['Hits'] = 3,
    },
    ["rebirth_grimmjow:two"] ={
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10,
	    ['Hits'] = 2,
    },
    ["rebirth_grimmjow:three"] ={
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 50,
	    ['Hits'] = 3,
    },
    ["hanako_kun:one"] ={
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8,
		['Effect'] = {
			['Name'] = 'Burn',
			['Ticks'] = 4,
			['Multiplier'] = 0.125
		}
    },
    ["hanako_kun:two"] ={
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 11,
		['Hits'] = 3,
		['Effect'] = {
			['Name'] = 'Burn',
			['Ticks'] = 4,
			['Multiplier'] = 0.125
		}
    },
    ["hanako_kun:three"] ={
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 60,
		['Hits'] = 9,
		['Effect'] = {
			['Name'] = 'Burn',
			['Ticks'] = 4,
			['Multiplier'] = 0.125
		}
    },
	["buu:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 9
	},
	["buu:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 11
	},
	["buu:three"] = {
		['AOE_TYPE'] = 'AoE (Full)',
		['Hits'] = 3
	},
	["goku_ssj3:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8,
		['Hits'] = 3
	},
	["goku_ssj3:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 12,
		['Hits'] =	3
	},
	["goku_ssj3:three"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 15,
		['Hits'] = 3
	},
	["vegeta_majin:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8.5
	},
	["vegeta_majin:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10
	},
	["vegeta_majin:three"] = {
		['AOE_TYPE'] = 'AoE (Full)',
		['Hits'] = 3
	},
	["vegito:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8
	},
	["vegito:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 12
	},
	["vegito:four"] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 12
	},
	["vegito:three"] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 60,
		['Hits'] = 3
	},




	["yuma:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8
	},
	["yuma:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10,
		['Hits'] = 4
	},
	["yuma:three"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 12,
		['Hits'] = 12
	},
	["naruto_sage:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 9
	},
	["naruto_sage:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 11
	},
	["chika:one"] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 5
	},
	["chika:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 9,
		['Hits'] = 3
 	},
	["chika:three"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 13,
		['Hits'] = 1
	},
	["sasuke_3:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 9,
		['Hits'] = 3,
    	['Effect'] = {
			['Name'] = 'Burn',
			['Ticks'] = 5,
			['Multiplier'] = 0.2
		}
	},
	["sasuke_3:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 11,
		['Hits'] = 3,
    	['Effect'] = {
			['Name'] = 'Burn',
			['Ticks'] = 5,
			['Multiplier'] = 0.2
		}
	},
	["sasuke_3:three"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 13,
		['Hits'] = 1,
    	['Effect'] = {
			['Name'] = 'Burn',
			['Ticks'] = 5,
			['Multiplier'] = 0.2
		}
	},
	["sasuke_3:four"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 15,
		['Hits'] = 4,
    	['Effect'] = {
			['Name'] = 'Burn',
			['Ticks'] = 5,
			['Multiplier'] = 0.2
		}
	},
	["cooler:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8
	},
	["cooler:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10
	},
	["cooler:three"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 15,
		['Hits'] = 3
	},
	["pain_2:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8,
		['Hits'] = 2
	},
	["pain_2:two"] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 45,
		['Hits'] = 1
	},
	["pain_2:three"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 14,
		['Special_Effect'] = {
			['Name'] = 'Knockback'
		}
	},
	["pain_2:four"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 19,
		['Hits'] = 4
	},
	["jiraiya:one"] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 10,
		['Hits'] = 3,
		['Special_Effect'] = {
			['Name'] = 'Slow',
			['Duration'] = 4,
			['Influence'] = 0.5
		}
	},
	["jiraiya:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 12,
		['Hits'] = 1,
		['Special_Effect'] = {
			['Name'] = 'Slow',
			['Duration'] = 4,
			['Influence'] = 0.5
		}
	},
	["jiraiya:three"] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 60,
		['Hits'] = 3,
		['Special_Effect'] = {
			['Name'] = 'Slow',
			['Duration'] = 4,
			['Influence'] = 0.5
		}
	},
	["jiraiya:one_unevo"] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 10,
		['Hits'] = 3,
	},
	["jiraiya:two_unevo"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 12,
		['Hits'] = 1,
	},
	["naruto_6tails:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 9
	},
	["naruto_6tails:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 11,
		['Hits'] = 3
	},
	["naruto_6tails:three"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 13,
		['Hits'] = 1
	},
	["boxxo:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10,
		['Hits'] = 3
	},
	["konan_unit:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10
	},
	["konan_unit:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10
	},
	["konan_unit:three"] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 50,
		['Hits'] = 3
	},
	["konan_unit:four"] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 50,
		['Hits'] = 4
	},
	
	
	
	
	
	
	
	
	["hinami:one"] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 45
	},
	["hinami:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10
	},
	["hinami:three"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 12
	},
	["caesarclown:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6,
		['Effect'] = {
			['Name'] = 'Poison',
			['Ticks'] = 56,
			['Multiplier'] = 0.05
		}
	},
	["caesarclown:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 9,
		['Effect'] = {
			['Name'] = 'Poison',
			['Ticks'] = 56,
			['Multiplier'] = 0.05
		}
	},
	["caesarclown:three"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 13,
		['Hits'] = 3,
		['Effect'] = {
			['Name'] = 'Poison',
			['Ticks'] = 56,
			['Multiplier'] = 0.05
		}
	},
	["cid:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6,
		['Hits'] = 3
	},
	["cid:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 12,
		['Hits'] = 2
	},
	["cid:three"] = {
		['AOE_TYPE'] = 'AoE (Full)',
		['Hits'] = 3
	},
	["hidan_unit:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8,
		['Effect'] = {
			['Name'] = 'Bleed',
			['Ticks'] = 3,
			['Multiplier'] = 0.1
		}
	},
	["hidan_unit:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 12,
		['Hits'] = 2,
		['Effect'] = {
			['Name'] = 'Bleed',
			['Ticks'] = 3,
			['Multiplier'] = 0.1
		}
	},
	["hidan_unit:three"] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 60,
		['Hits'] = 3,
		['Effect'] = {
			['Name'] = 'Bleed',
			['Ticks'] = 3,
			['Multiplier'] = 0.1
		}
	},
	["alucard:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8,
		['Hits'] = 3
	},
	["alucard:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10,
		['Hits'] = 1
	},
	["alucard:three"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 12,
		['Hits'] = 3
	},
	
	
	
	
	["atsushi:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 7,
		['Hits'] = 3,
		['Effect'] = {
			['Name'] = 'Bleed',
			['Ticks'] = 3,
			['Multiplier'] = 0.083
		}
	},
	["atsushi:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 9,
		['Hits'] = 3,
		['Effect'] = {
			['Name'] = 'Bleed',
			['Ticks'] = 3,
			['Multiplier'] = 0.083
		}
	},
	["atsushi:three"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 15,
		['Hits'] = 2,
		['Effect'] = {
			['Name'] = 'Bleed',
			['Ticks'] = 3,
			['Multiplier'] = 0.083
		}
	},
	["chuya:one"] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 7
	},
	["chuya:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 9,
		['Hits'] = 3
	},
	["chuya:three"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 11,
		['Hits'] = 3
	},
	["chuya:four"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 13,
		['Hits'] = 4
	},
	["akutagawa:spikes"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10
	},
	["akutagawa:slash"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8
	},
	["akutagawa:ribbon"] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 60
	},
	["akutagawa:bite"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 12
	},
	["dazai:shoot"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8,
		['Hits'] = 3
	},
	["dazai:punch"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10,
		['Hits'] = 1
	},
	["dazai:full_aoe"] = {
		['AOE_TYPE'] = 'AoE (Full)',
		['Hits'] = 1
	},
	["izumi:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8
	},
	["izumi:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 9,
		['Hits'] = 3
	},
	["izumi:three"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10,
		['Hits'] = 4
	},
	
	
	
	
	["tsuna:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 9,
		['Hits'] = 3,
		['Effect'] = {
			['Name'] = 'Burn',
			['Ticks'] = 5,
			['Multiplier'] = 0.08
		}
	},
	["tsuna:two"] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 50,
		['Hits'] = 1,
		['Effect'] = {
			['Name'] = 'Burn',
			['Ticks'] = 5,
			['Multiplier'] = 0.08
		}
	},
	["tsuna:three"] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 60,
		['Hits'] = 2,
		['Effect'] = {
			['Name'] = 'Burn',
			['Ticks'] = 5,
			['Multiplier'] = 0.08
		}
	},
	["bambietta:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8
	},
	["bambietta:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 12,
		['Hits'] = 3
	},
	["bambietta:three"] = {
		['AOE_TYPE'] = 'AoE (Full)'
	},
	["kimimaro:one"] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 3
	},
	["kimimaro:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] =  8
	},
	["kimimaro:three"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 12
	},
	["illya:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6
	},
	["illya:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10
	},
	["illya:three"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 14,
		['Hits'] = 3
	},
	["gilgamesh:wheel_gates"] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 10,
		['Hits'] = 3
	},
	["gilgamesh:collapse"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 9,
		['Hits'] = 1
	},
	["gilgamesh:jump_and_gates"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 12,
		['Hits'] = 4
	},
	["gilgamesh:slashes"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 12,
		['Hits'] = 3
	},
	["gilgamesh:enuma_elish"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 16,
		['Hits'] = 5
	},
	["cranel:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 4.5
	},
	["cranel:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6
	},
	["cranel:three"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] =7
	},
	["caesar:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 5
	},
	["caesar:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8,
		['Hits'] = 3
	},
	["caesar:three"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 12,
		['Hits'] = 3
	},
	["lancer:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 7
	},
	["lancer:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 12
	},
	["lancer:three"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8,
		['Hits'] = 4
	},
	["lancer:four"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 9,
		['Hits'] = 3
	},
	["archer:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 5
	},
	["archer:two"] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 5,
		['Hits'] = 2
	},
	["archer:three"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 9.5,
		['Hits'] = 5
	},
	["archer:four"] = {
		['AOE_TYPE'] = 'Aoe (Circle)',
		['radius'] = 11,
		['Hits'] = 3
	},
	["medea:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 7
	},
	["medea:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8,
		['Hits'] = 3
	},
	["medea:three"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 9,
		['Hits' ] = 3
	},
	["saber:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 7.5
	},
	["saber:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 9
	},
	["saber:three"] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 50,
		['Hits' ] = 3
	},
	["saber:four"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 12
	},
	
	
	
	
	
	
	
	
	["josuke_2:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6,
		['Special_Effect'] = {
        	['Name'] = 'Stun'
        }
	},
	["josuke_2:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8,
		['Hits'] = 4,
		['Special_Effect'] = {
        	['Name'] = 'Stun'
        }
	},
	["josuke_2:three"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 12,
		['Hits'] = 2,
		['Special_Effect'] = {
        	['Name'] = 'Stun'
        }
	},
	["koichi:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 5,
		['Hits'] = 3
	},
	["koichi:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8
	},
	["koichi:three"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 12,
		['Hits'] = 3
	},
	["koichi_evolved:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 5,
		['Hits'] = 3,
		['Special_Effect'] = {
			['Name'] = 'Slow',
			['Duration'] = 2.5,
			['Influence'] = 0.5
		}
	},
	["koichi_evolved:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8,
		['Special_Effect'] = {
			['Name'] = 'Slow',
			['Duration'] = 2.5,
			['Influence'] = 0.65
		}
	},
	["koichi_evolved:three"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 12,
		['Hits'] = 3,
		['Special_Effect'] = {
			['Name'] = 'Slow',
			['Duration'] = 2.5,
			['Influence'] = 0.8
		}
	},
	["kira:coin_toss"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6
	},
	["kira:heart_attack"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8
	},
	["kira:bubble"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 9
	},
	["kira:triple_bomb"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 12,
		['Hits'] = 3
	},
	["rohan:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 5
	},
	["rohan:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 5.5,
		['Hits'] = 3
	},
	["rohan:three"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6,
		['Hits'] = 3,
		['Special_Effect'] = {
			['Name'] = 'Wild Card'
		}
	},
	
	
	
	
	
	
	
	["conrad:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 9,
		['Hits'] = 3
	},
	["conrad:two"] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 8,
		['Hits'] = 1
	},
	["conrad:three"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 15
	},
	
	
	
	["albedo:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 7
	},
	["albedo:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8,
		['Hits'] = 3
	},
	["albedo:three"] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 7
	},
	["albedo:four"] = {
		['AOE_TYPE'] = 'AoE (Full)'
	},
	["smoker:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8,
		['Hits'] = 3
	},
	["smoker:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10,
		['Hits'] = 3
	},
	["smoker:three"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 12,
		['Hits'] = 3
	},
	["shalltear:one"] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 50,
	},
	["shalltear:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 9
	},
	["shalltear:three"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 12,
		['Hits'] = 3
	},
    ["shalltear_evo:one"] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 50,
		['Special_Effect'] = {
        	['Name'] = 'Bleed Amplification'
        }
	},
	["shalltear_evo:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 9,
		['Special_Effect'] = {
        	['Name'] = 'Bleed Amplification'
        }
	},
	["shalltear_evo:three"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 12,
		['Hits'] = 3,
		['Special_Effect'] = {
        	['Name'] = 'Bleed Amplification'
        }
	},
	["narberal:one"] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 5
	},
	["narberal:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 7
	},
	["narberal:three"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 9
	},
	["minato:first"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 7
	},
	["minato:second"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 9
	},
	["minato:third"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 12,
		['Hits'] = 3
	},
	["kenshin:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 7
	},
	["kenshin:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8
	},
	["kenshin:three"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10,
		['Hits'] = 2
	},
	["isagi:one"] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 4
	},
	["isagi:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6
	},
	["isagi:three"] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 6
	},
	["evileye:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6
	},
	["evileye:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 7
	},
	["evileye:three"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 13,
		['Hits'] = 3
	},
	["demiurge:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8,
		['Effect'] = {
			['Name'] = 'Burn',
			['Ticks'] = 4,
			['Multiplier'] = 0.1
		}
	},
	["demiurge:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10,
		['Effect'] = {
			['Name'] = 'Burn',
			['Ticks'] = 4,
			['Multiplier'] = 0.1
		}
	},
	["demiurge:three"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 12,
		['Effect'] = {
			['Name'] = 'Burn',
			['Ticks'] = 4,
			['Multiplier'] = 0.1
		}
	},
	["ainz:ball"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 7
	},
	["ainz:lightning"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10
	},
	["ainz:fallen_down"] = {
		['AOE_TYPE'] = 'AoE (Full)',
		['Hits'] = 3
	},




	
	
	["avdol:one"] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 45,
		['Hits'] = 2,
		['Effect'] = {
			['Name'] = 'Burn',
			['Ticks'] = 5,
			['Multiplier'] = 0.06
		}
	},
	["avdol:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10,
		['Effect'] = {
			['Name'] = 'Burn',
			['Ticks'] = 5,
			['Multiplier'] = 0.06
		}
	},
	["avdol:three"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 14,
		['Hits'] = 4,
		['Effect'] = {
			['Name'] = 'Burn',
			['Ticks'] = 5,
			['Multiplier'] = 0.06
		}
	},
	["harribel:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6,
		['Hits'] = 3
	},
	["harribel:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8,
		['Hits'] = 1
	},
	["harribel:three"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 9,
		['Hits'] = 3
	},
	["kisame:one"] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 5
	},
	["kisame:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8
	},
	["kisame:three"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 11
	},
	["poseidon:one"] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 50,
		['Hits'] = 3
	},
	["poseidon:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8,
		['Hits'] = 3
	},
	["poseidon:three"] = {
		['AOE_TYPE'] = 'AoE (Full)',
		['Hits'] = 4
	},
	["roger:slashes"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8,
		['Hits'] = 3
	},
	["roger:projectile_slash"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 9
	},
	["roger:ult"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 11,
		['Hits'] = 3
	},
	["evolved_roger:slashes"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8,
		['Hits'] = 3,
		['Special_Effect'] = {
        	['Name'] = 'Stun'
        }
	},
	["evolved_roger:projectile_slash"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 9,
		['Special_Effect'] = {
        	['Name'] = 'Stun'
        }
	},
	["evolved_roger:ult"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 11,
		['Hits'] = 3,
		['Special_Effect'] = {
        	['Name'] = 'Stun'
        }
	},



	
	
	["temari:one"] = {
		['AOE_TYPE'] = 'AoE (Full)'
	},
	["temari:two"] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 8
	},
	["temari:three"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6
	},
	
	
	
	
	["gabimaru:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 7,
		['Effect'] = {
			['Name'] = 'Burn',
			['Ticks'] = 4,
			['Multiplier'] = 0.1
		}
	},
	["gabimaru:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 9,
		['Effect'] = {
			['Name'] = 'Burn',
			['Ticks'] = 4,
			['Multiplier'] = 0.1
		}
	},
	["gabimaru:three"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 12,
		['Hits'] = 3,
		['Effect'] = {
			['Name'] = 'Burn',
			['Ticks'] = 4,
			['Multiplier'] = 0.1
		}
	},
	["griffith:combo"] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 50,
		['Hits'] = 4
	},
	["griffith:stabs"] = {
			['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 50,
		['Hits'] = 4
	},
	["femto_egg:sacrifice"] = {
		['AOE_TYPE'] = 'AoE (Full)'
	},
	["femto:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 15,
		['Hits'] = 4
	},
	["femto:two"] = {
		['AOE_TYPE'] = 'AoE (Full)',
		['Hits'] = 4
	},
	["chad:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 7
	},
	["chad:two"] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 8,
		['Hits'] = 3
	},
	["chad:three"] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 10
	},
	["sengoku:slams"] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 60,
		['Hits'] = 2
	},
	["sengoku:kamehameha"] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 75
	},
	["sengoku:shockwave"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 20,
		['Hits'] = 3
	},
	["issei:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6
	},
	["issei:two"] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 6,
		['Hits'] = 2
	},
	["issei:three"] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 45,
		['Hits'] = 3	
	},
	["guts_berserker:two"] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 60,
		['Hits'] = 2,
		['Effect'] = {
			['Name'] = 'Bleed',
			['Ticks'] = 4,
			['Multiplier'] = 0.0625
		}
	},
	["guts_berserker:one"] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 60,
		['Hits'] = 3,
		['Effect'] = {
			['Name'] = 'Bleed',
			['Ticks'] = 4,
			['Multiplier'] = 0.0625
		}
	},
	["guts_berserker:three"] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 60,
		['Hits'] = 6,
		['Effect'] = {
			['Name'] = 'Bleed',
			['Ticks'] = 4,
			['Multiplier'] = 0.0625
		}
	},
	["guts_berserker:four"] = {
		['AOE_TYPE'] = 'AoE (Full)',
		['Hits'] = 5
	},
	["guts:slash"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 7,
		['Effect'] = {
			['Name'] = 'Bleed',
			['Ticks'] = 3,
			['Multiplier'] = 0.08
		}
	},
	["guts:cannon"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8,
		['Effect'] = {
			['Name'] = 'Bleed',
			['Ticks'] = 3,
			['Multiplier'] = 0.08
		}
	},
	["guts:combo"] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 60,
		['Hits'] = 4
	},
	["skull_knight:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 7
	},
	["skull_knight:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10
	},
	["skull_knight:three"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 12,
		['Hits'] = 3
	},
	
	
	
	
	
	
	
	
	["kirito:stab"] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 40
	},
	["kirito:double"] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 40,
		['Hits'] = 2
	},
	["kirito:square"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8,
		['Hits'] = 3
	},
	["kirito_evolved:slice"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6,
		['Hits'] = 1
	},
	["kirito_evolved:stream"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 12,
		['Hits'] = 6
	},
	["klein:slash"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 7
	},
	["klein:stab"] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 45
	},
	["klein:final"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10,
		['Hits'] = 3
	},
	["leafa:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6
	},
	["leafa:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8,
		['Hits'] = 3
	},
	["mash:punches"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6,
		['Hits'] = 2
	},
	["mash:throw"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8,
		['Hits'] = 1
	},
	["mash:counters"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 12,
		['Hits'] = 3
	},
	["roshi:one"] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 40
	},
	["roshi:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 7
	},
	["roshi:three"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 9,
		['Hits'] = 3
	},
	["stain:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8,
		['Effect'] = {
			['Name'] = 'Bleed',
			['Ticks'] = 3,
			['Multiplier'] = 0.1
		}
	},
	["stain:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 12,
		['Hits'] = 3,
		['Effect'] = {
			['Name'] = 'Bleed',
			['Ticks'] = 3,
			['Multiplier'] = 0.1
		}
	},
	["stain:three"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 15,
		['Hits'] = 3,
		['Effect'] = {
			['Name'] = 'Bleed',
			['Ticks'] = 3,
			['Multiplier'] = 0.1
		}
	},
	["asuna:jab"] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 40
	},
	["asuna:stabs"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6,
		['Hits'] = 3
	},
	["asuna:barrage"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8,
		['Hits'] = 3
	},
	["asuna:final"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10,
		['Hits'] = 3
	},
	["buggy:one"] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 5
	},
	["buggy:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 7
	},
	["buggy:three"] = {
		['AOE_TYPE'] = 'AoE (Full)'
	},
	["charmy:ball"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6,
		['Special_Effect'] = {
			['Name'] = 'Slow',
		}
	},
	["charmy:sheep"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 7.5,
		['Special_Effect'] = {
			['Name'] = 'Slow',
		}
	},
	["charmy:sheep2"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 11,
		['Hits'] = 3,
		['Special_Effect'] = {
			['Name'] = 'Slow',
		}
	},
	["heathcliff:shield_bash"] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 40
	},
	["heathcliff:bash_and_slash"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10,
		['Hits'] = 2
	},
	["heathcliff:stabs"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8,
		['Hits'] = 3
	},
	["heathcliff:full_sweep"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 15,
		['Hits'] = 3
	},

	
	
	--Update 13.5.0
	["homura:shoot"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 5,
		['Hits'] = 3
	},
	["homura:grenade"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 7,
		['Hits'] = 1
	},
	["homura:ult"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 14,
		['Hits'] = 3
	},
	["sayaka:slash"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6
	},
	["sayaka:dash"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 7
	},
	["sayaka:final"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 9,
		['Hits'] = 2
	},
	["mami:one"] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 40
	},
	["mami:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8
	},
	["mami:three"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 15,
		['Hits'] = 3
	},
	["madoka:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 7
	},
	["madoka:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 9,
		['Hits'] = 3
	},
	["madoka:three"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 11,
		['Hits'] = 1
	},
	["kyoko:stab"] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 7.5
	},
	["kyoko:combo"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8,
		['Hits'] = 4
	},
	["kyoko:final"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 12,
		['Hits'] = 2
	},
	
	--Update 13.0.0
	["usopp_ts:trap"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 4
	},
	["usopp_ts:trap2"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6
	},
	["usopp_ts:trap3"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8
	},
	["luffy_g4:punch"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 7.5
	},
	["luffy_g4:organ"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 9,
		['Hits'] = 4
	},
	["luffy_g4:gatling"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 12,
		['Hits'] = 4
	},
	["luffy_g4:final"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 15,
		['Hits'] = 1
	},
	["law_2:shot"] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 30
	},
	["law_2:radio"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 7
	},
	["law_2:shock"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 9
	},
	["law_2:gamma"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 11,
		['Hits'] = 3
	},
	["fujitora:touch"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8,
		['Hits'] = 2
	},
	["fujitora:meteor"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10,
		['Hits'] = 1
	},
	["fujitora:meteors"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 16,
		['Hits'] = 3
	},
	["sabo:fireball"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 9,
		['Effect'] = {
			['Name'] = 'Burn',
			['Ticks'] = 4,
			['Multiplier'] = 0.1
		}
	},
	["sabo:leap"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 9,
		['Effect'] = {
			['Name'] = 'Burn',
			['Ticks'] = 4,
			['Multiplier'] = 0.1
		}
	},
	["sabo:three"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 11,
		['Effect'] = {
			['Name'] = 'Burn',
			['Ticks'] = 4,
			['Multiplier'] = 0.1
		}
	},
	["rayleigh:attack_1"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6,
		['Hits'] = 3,
		['Special_Effect'] = {
        	['Name'] = 'Unconscious'
        }
	},
	["rayleigh:attack_2"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8,
		['Hits'] = 3,
		['Special_Effect'] = {
        	['Name'] = 'Unconscious'
        }
	},
	["rayleigh:final"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10,
		['Hits'] = 3,
		['Special_Effect'] = {
        	['Name'] = 'Unconscious'
        }
	},
	["ippo:basic"] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 40,
		['Hits'] = 4
	},
	["ippo:ult"] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 50,
		['Hits'] = 7
	},
	["doflamingo:rainbow"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6.5
	},
	["doflamingo:overheat"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8
	},
	["doflamingo:spikes"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 9
	},
	["doflamingo:birdcage"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10
	},
	["doflamingo:bullets"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 12,
		['Hits'] = 3
	},
	["nejire:one"] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 30
	},
	["nejire:two"] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 30
	},
	["nejire:three"] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 30
	},	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	-- Update 12.5.0
	["haze:bulb_throw"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6,
		['Hits'] = 3,
		['Effect'] = {
			['Name'] = 'Poison',
			['Ticks'] = 20,
			['Multiplier'] = 0.15
		}
	},
	["haze:bulb_shoot"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8,
		['Hits'] = 3,
		['Effect'] = {
			['Name'] = 'Poison',
			['Ticks'] = 20,
			['Multiplier'] = 0.15
		}
	},
	["haze:slam"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10,
		['Hits'] = 3,
		['Effect'] = {
			['Name'] = 'Poison',
			['Ticks'] = 20,
			['Multiplier'] = 0.15
		}
	},
	
	
	
	["carrot_evolved:one"] = {
		['AOE_TYPE'] = 'AoE (Full)',
		['Special_Effect'] = {
        	['Name'] = 'Stun'
        }
	},
	["carrot_evolved:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 7,
		['Special_Effect'] = {
        	['Name'] = 'Stun'
        }
	},
	["carrot_evolved:three"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 9,
		['Special_Effect'] = {
        	['Name'] = 'Stun'
        }
	},
	["carrot:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 5
	},
	["carrot:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 7
	},
	["carrot:three"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8
	},
	["mirko:kick"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['Hits'] = 1,
		['radius'] = 8,
	},
	["mirko:spin"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['Hits'] = 2,
		['radius'] = 9
	},
	["mirko:final"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['Hits'] = 1,
		['radius'] = 10
	},
	["yoshino:icicles"] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 60,
		['Special_Effect'] = {
    		['Name'] = 'Slow'
    	}
	},
	["yoshino:tornado"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 9,
		['Special_Effect'] = {
    		['Name'] = 'Slow'
    	}
	},
	["yoshino:summon"] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 5,
		['Special_Effect'] = {
    		['Name'] = 'Slow'
    	}
	},
	["daki:slash"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 5,
		['Effect'] = {
			['Name'] = 'Bleed',
			['Ticks'] = 4,
			['Multiplier'] = 0.1
		}
	},
	["daki:slam"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6,
		['Effect'] = {
			['Name'] = 'Bleed',
			['Ticks'] = 4,
			['Multiplier'] = 0.1
		}
	},
	["daki:spike"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['Hits'] = 2,
		['radius'] = 7,
		['Effect'] = {
			['Name'] = 'Bleed',
			['Ticks'] = 4,
			['Multiplier'] = 0.1
		}
	},
	["daki:ult"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['Hits'] = 3,
		['radius'] = 14,
		['Effect'] = {
			['Name'] = 'Bleed',
			['Ticks'] = 4,
			['Multiplier'] = 0.1
		}
	},
	["gyutaro:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['Hits'] = 3,
		['radius'] = 5,
		['Special_Effect'] = {
			['Name'] = 'OverCrit',
		}
	},
	["gyutaro:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['Hits'] = 3,
		['radius'] = 8,
		['Special_Effect'] = {
			['Name'] = 'OverCrit',
		}
	},
	["gyutaro:three"] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['Hits'] = 3,
		['angle'] = 50,
		['Special_Effect'] = {
			['Name'] = 'OverCrit',
		}
	},
	["tengen_2:slam"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 7
	},
	["tengen_2:combo_1"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['Hits'] = 3,
		['radius'] = 8
	},
	["tengen_2:combo_2"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['Hits'] = 4,
		['radius'] = 9
	},
	["tengen_2:ult"] = {
		['AOE_TYPE'] = 'AoE (Full)',
		['Hits'] = 5,
	},
	
	
	
	-- Update 12.0.0
	["vash_revolver:shoot"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['Hits'] = 3,
		['radius'] = 6
	},
	["vash_revolver:barrage"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['Hits'] = 3,
		['radius'] = 8
	},
	["vash_cross:attack"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['Hits'] = 3,
		['radius'] = 8
	},
	["vash_cross:final"] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['Hits'] = 3,
		['width'] = 10
	},
	["deku_vigilante:axe_kick"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6
	},
	["deku_vigilante:blackwhip"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 9
	},
	["deku_vigilante:whip_punch"] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 8.5
	},
	["deku_vigilante:slingshot"] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 10
	},
	["endeavor:spear"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 7,
		['Effect'] = {
			['Name'] = 'Burn',
			['Ticks'] = 6,
			['Multiplier'] = 0.08333333333333333
		}
	},
    ["endeavor:fire_spray"] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 60,
		['Effect'] = {
			['Name'] = 'Burn',
			['Ticks'] = 6,
			['Multiplier'] = 0.08333333333333333
		}
	},
	["vash_cross:final"] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 10
	},
	["endeavor:prominence_burn"] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 60,
		['Effect'] = {
			['Name'] = 'Burn',
			['Ticks'] = 6,
			['Multiplier'] = 0.08333333333333333
		}
	},
	["bakugou_2:jump"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 5
	},
	["bakugou_2:dash"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6
	},
	["bakugou_2:barrage"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 9
	},
	["bakugou_2:howitzer"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 13
	},
	["hawks:slashes"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6.5
	},
	["hawks:projectiles"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8
	},
	["hawks:tornado"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10
	},

	["shigaraki:target"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8,
	},
	["shigaraki:aoe"] = {
		['AOE_TYPE'] = 'AoE (Full)'
	},

	["shigaraki_evolved:target"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8,
		['Effect'] = {
			['Name'] = 'Wither',
			['Ticks'] = 3,
			['Multiplier'] = 0.06666666666666667
		},
		['Special_Effect'] = {
			['Name'] = 'Wither'
		}
	},
	["shigaraki_evolved:aoe"] = {
		['AOE_TYPE'] = 'AoE (Full)',
		['Effect'] = {
		    ['Name'] = 'Wither',
		    ['Ticks'] = 4,
		    ['Multiplier'] = 0.06666666666666667
		}
	},
	["shigaraki_evolved:full_aoe"] = {
		['AOE_TYPE'] = 'AoE (Full)',
		['Hits'] = 3,
		['Effect'] = {
		    ['Name'] = 'Wither',
		    ['Ticks'] = 18,
		    ['Multiplier'] = 0.06666666666666667
		}
	},

	["unohana:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6
	},
	["unohana:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6
	},
	["unohana:bankai"] = {
		['AOE_TYPE'] = 'AoE (Full)',
		['Effect'] = {
			['Name'] = 'Bleed',
			['Ticks'] = 4,
			['Multiplier'] = 0.125
		}
	},
	["jin_mori:kick"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6
	},
	["jin_mori:dragon"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8
	},
	["jin_mori:staff"] = {
		['AOE_TYPE'] = 'AoE (Full)',
	},
	["jozu:one"] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 5
	},
	["jozu:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6
	},
	["jozu:three"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10
	},
	["gogeta_failed:run"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 5
	},
	["rias:one"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 5
	},
	["rias:two"] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 5
	},
	["rias:three"] = {
		['AOE_TYPE'] = 'AoE (Full)',
	},
	["koneko:one"] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['Hits'] = 2,
		['angle'] = 30
	},
	["koneko:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['Hits'] = 1,
		['radius'] = 6
	},
	["koneko:three"] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['Hits'] = 2,
		['angle'] = 45
	},
	["akeno:one"] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['Hits'] = 2,
		['angle'] = 30
	},
	["akeno:two"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['Hits'] = 1,
		['radius'] = 8
	},
	["akeno:three"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['Hits'] = 3,
		['radius'] = 12
	},
	
	
	
	
	
	
	-- Update 11.7.5
	["hange:slash"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 4,
		['Effect'] = {
			['Name'] = 'Bleed',
			['Ticks'] = 3,
			['Multiplier'] = 0.1
		}
	},
    ["hange:dive"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 5,
		['Effect'] = {
			['Name'] = 'Bleed',
			['Ticks'] = 3,
			['Multiplier'] = 0.1
		}
	},
    ["hange:spear"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6,
		['Effect'] = {
			['Name'] = 'Bleed',
			['Ticks'] = 3,
			['Multiplier'] = 0.1
		}
	},
    ["inuyasha:dimension"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10
	},
    ["frieza_golden:beams"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6
	},
    ["frieza_golden:discs"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8
	},
    ["frieza_golden:ball"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 18
	},
    ["piccolo_fused:bomb"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8
	},
    ["piccolo_fused:grenade"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10
	},
    ["piccolo_fused:beam"] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 3
	},
    ["vegeta_super:normal_blast"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8
	},
    ["vegeta_super:galick_gun"] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 60
	},
    ["vegeta_super:final_flash"] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 60
	},
    
	
	
	
	
	
	-- Update 11.5.0
	["inuyasha:slash"] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 6
	},
	["inuyasha:cone"] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 56
	},
	["inuyasha:dimension"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10
	},
	["merlin:blast"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8
	},
	["merlin:beam_unevo"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8
	},
	["merlin:beam"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8,
		['Special_Effect'] = {
			['Name'] = 'Hexed (20%)',
		}
	},
	["merlin:ray"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 12,
		['Special_Effect'] = {
			['Name'] = 'Hexed (25%)',
		}
	},
	["escanor:jump_slam"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 7
	},
	["escanor:divine_spear"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8.5
	},
	["escanor:cruel_sun"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10.5
	},
	["escanor_evolved:jump_slam"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8,
		['Special_Effect'] = {
			['Name'] = 'Sunshine',
		}
	},
	["escanor_evolved:divine_spear"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10,
		['Special_Effect'] = {
			['Name'] = 'Sunshine',
		}
	},
	["escanor_evolved:cruel_sun"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 12,
		['Special_Effect'] = {
			['Name'] = 'Sunshine',
		}
	},
	["escanor_evolved:final"] = {
		['AOE_TYPE'] = 'AoE (Full)',
		['Special_Effect'] = {
			['Name'] = 'Sunshine',
		}
	},
	["escanor_weak:throw"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8
	},
	

	
	-- Update 11.0.0
	["zabuza:slash"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 5
	},
	["zabuza:clone"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 7
	},
	["zabuza:dragons"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10
	},
	["boa:first"] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 50,
        ['Special_Effect'] = {
        	['Name'] = 'Freeze'
        }
	},
	["boa:projectile_and_kick"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 7,
        ['Special_Effect'] = {
        	['Name'] = 'Freeze'
        }
	},
	["boa:final"] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 60,
        ['Special_Effect'] = {
        	['Name'] = 'Freeze'
        }
	},



	["meliodas:flame"] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 50
	},
	["meliodas:slashes"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 7
	},
    ["meliodas:explode_slash"] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['Hits'] = 2,
		['angle'] = 50
	},
	["meliodas:dark_sword"] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['Hits'] = 1,
		['angle'] = 50
	},
	["meliodas:final"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['Hits'] = 3,
		['radius'] = 9
	},
	["ban:slash"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6,
		['Effect'] = {
			['Name'] = 'Bleed',
			['Ticks'] = 4,
			['Multiplier'] = 0.075
		}
	},
	["ban:barrage"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8,
		['Effect'] = {
			['Name'] = 'Bleed',
			['Ticks'] = 4,
			['Multiplier'] = 0.075
		}
	},
	["ban:suck"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8,
		['Special_Effect'] = {
        	['Name'] = 'Snatched'
        }
	},
	["gowther:shots"] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 60
	},
	["gowther:barrage"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10
	},
	["gowther_evolved:barrage"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10,
		['Special_Effect'] = {
        	['Name'] = 'Mind Control'
        }
	},
	["gowther:sky"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 11,
		['Special_Effect'] = {
        	['Name'] = 'Mind Control'
        }
	},
	["king_7ds:butterfly"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6
	},
	["king_7ds:combo"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8
	},
	["king_7ds:big_spear"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10
	},
	["diane:stream"] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 10
	},
	["diane:spikes"] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 80
	},
	["diane:hands"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['Hits'] = 3,
		['radius'] = 20
	},
	
	
	
    -- Update 10.7.5
	["shisui:slash"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 5
	},
    ["shisui:kunai"] = {
    	['AOE_TYPE'] = 'AoE (Circle)',
    	['radius'] = 7
    },
    ["shisui:flicker"] = {
    	['AOE_TYPE'] = 'AoE (Cone)',
    	['angle'] = 40
    },
    ["shisui_evolved:spikes"] = {
    	['AOE_TYPE'] = 'AoE (Cone)',
    	['angle'] = 50
    },
    ["shisui_evolved:lunge"] = {
    	['AOE_TYPE'] = 'AoE (Cone)',
    	['angle'] = 60
    },
    ["sasuke_2:cutter"] = {
    	['AOE_TYPE'] = 'AoE (Circle)',
    	['radius'] = 5
    },
    ["sasuke_2:leap"] = {
    	['AOE_TYPE'] = 'AoE (Circle)',
    	['radius'] = 7
    },
    ["sasuke_2:leap_black"] = {
    	['AOE_TYPE'] = 'AoE (Circle)',
    	['radius'] = 7
    },
    ["sasuke_2:kirin"] = {
    	['AOE_TYPE'] = 'AoE (Circle)',
    	['radius'] = 12,
        ['Special_Effect'] = {
        	['Name'] = 'Stun'
        }
    },
    ["itachi_2:fireball"] = {
    	['AOE_TYPE'] = 'AoE (Circle)',
    	['radius'] = 7,
    	['Effect'] = {
			['Name'] = 'Burn',
			['Ticks'] = 5,
			['Multiplier'] = 0.1
		}
    },
    ["itachi_2:amaterasu"] = {
    	['AOE_TYPE'] = 'AoE (Circle)',
        ['Hits'] = 2,
    	['radius'] = 9.5,
    	['Effect'] = {
			['Name'] = 'Burn',
			['Ticks'] = 10,
			['Multiplier'] = 0.1
		}
    },
    ["itachi_2:susanoo_combo"] = {
    	['AOE_TYPE'] = 'AoE (Cone)',
        ['Hits'] = 3,
    	['angle'] = 50,
    	['Effect'] = {
			['Name'] = 'Burn',
			['Ticks'] = 10,
			['Multiplier'] = 0.1
		}
    },
    ["itachi_2:downward_slash"] = {
    	['AOE_TYPE'] = 'AoE (Cone)',
        ['Hits'] = 3,
    	['angle'] = 50,
    	['Effect'] = {
			['Name'] = 'Burn',
			['Ticks'] = 10,
			['Multiplier'] = 0.1
		}
    },
    

	
	
	-- Update 10.5 ? (Maybe)
	["thor:slam"] = {
	    ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 8
    },
    ["thor:slam_2"] = {
    	['AOE_TYPE'] = 'AoE (Cone)',
    	['angle'] = 60
    },
    ["thor:final"] = {
    	['AOE_TYPE'] = 'AoE (Circle)',
    	['radius'] = 12
    },
    	
    	
	    
	    
	-- Update ????
	["geten:ice"] = {
		['AOE_TYPE'] = 'AoE (Line)',
	    ['width'] = 6
	},
	["geten:spikes"] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 7
	},
    ["geten:slam"] = {
    	['AOE_TYPE'] = 'AoE (Circle)',
    	['radius'] = 9
    },
	
	
	
	-- Update 10
	["nami:bubble"] = {
	    ['AOE_TYPE'] = 'AoE (Circle)',
	    ['radius'] = 6
	},
    ["nami:wind"] = {
    	['AOE_TYPE'] = 'AoE (Line)',
    	['width'] = 6
    },
    ["nami:thunder"] = {
    	['AOE_TYPE'] = 'AoE (Cone)',
    	['angle'] = 60
    },
	["tatsumi:lunge"] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 6
	},
    ["tatsumi:dive"] = {
       	['AOE_TYPE'] = 'AoE (Circle)',
       	['radius'] = 9
    },
    
    
	['android21:blast'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 5
    },
    ['android21:lazer'] = {
        ['AOE_TYPE'] = 'AoE (Line)',
        ['width'] = 4
    },
    ['android21:ball'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 12
    },
    ['obito:fire'] = {
        ['AOE_TYPE'] = 'AoE (Line)',
        ['width'] = 4
    },
    ['obito:slam'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 7
    },
    ['obito:bomb'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 9
    },
    ['boros:slam'] = {
        ['AOE_TYPE'] = 'AoE (Full)'
    },
    ['boros:projectile'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 7.5
    },
    ['boros:final'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['Hits'] = 3,
        ['radius'] = 12
    },
    ['bang:double_punch'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['Hits'] = 2,
        ['radius'] = 5
    },
    ['bang:punch_barrage'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['Hits'] = 3,
        ['radius'] = 7
    },
    ['bang:final'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['Hits'] = 3,
        ['radius'] = 10
    },
	['genos_2:smaller_blast'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 6.5,
		['Effect'] = {
			['Name'] = 'Burn',
			['Ticks'] = 5,
			['Multiplier'] = 0.06
		}
    },
	['genos_2:boost_attack'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 8,
		['Effect'] = {
			['Name'] = 'Burn',
			['Ticks'] = 5,
			['Multiplier'] = 0.06
		}
	},
	['genos_2:incinerate'] = {
		['AOE_TYPE'] = 'AoE (Cone)',
        ['angle'] = 60,
		['Effect'] = {
			['Name'] = 'Burn',
			['Ticks'] = 5,
			['Multiplier'] = 0.06
		}
    },
    ['metal_knight:landing'] = {
        ['AOE_TYPE'] = 'Single'
    },
    ['metal_knight:wristfire'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 6
    },
    ['metal_knight:laser'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['Hits'] = 3,
        ['radius'] = 10
    },
    ['metal_knight:rockets'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['Hits'] = 4,
        ['radius'] = 15
    },
    ['sonic:slash'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 4
    },
    ['sonic:bomb'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 6
    },
    ['sonic:clones'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 10
    },
    ['tatsumaki:basic'] = {
        ['AOE_TYPE'] = 'AoE (Cone)',
        ['angle'] = 60
    },
    ['tatsumaki:rocks'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 6
    },
    ['tatsumaki:kick'] = {
        ['AOE_TYPE'] = 'AoE (Cone)',
        ['angle'] = 60
    },
    ['tatsumaki:kick_evolved'] = {
        ['AOE_TYPE'] = 'AoE (Cone)',
        ['angle'] = 60,
		['Special_Effect'] = {
			['Name'] = 'Knockback',
		}
    },
    ['tatsumaki:meteor'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 15,
		['Special_Effect'] = {
			['Name'] = 'Knockback',
		}
    },
    
    
	
	-- Update 9
	['kobeni:slash'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 6
    },
        ['kobeni:dash_slash'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 6.5
    },
	['kobeni:final'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 8
    },
    ['aki:3_hit'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 3
    },
    ['himeno:slam'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 6
    },
    ['himeno:squeeze'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 7
    },
    ['power:sword'] = {
        ['AOE_TYPE'] = 'AoE (Cone)',
		['Hits'] = 2,
        ['angle'] = 60
    },
    ['power:hammer'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
		['Hits'] = 1,
        ['radius'] = 10
    },
    ['power:scythe'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
		['Hits'] = 3,
        ['radius'] = 10
    },
    ['power_evolved:sword'] = {
        ['AOE_TYPE'] = 'AoE (Cone)',
		['Hits'] = 2,
        ['angle'] = 60,
        ['Special_Effect'] = {
        	['Name'] = 'Bleed Amplification'
        }
    },
    ['power_evolved:hammer'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
		['Hits'] = 1,
        ['radius'] = 10,
        ['Special_Effect'] = {
        	['Name'] = 'Bleed Amplification'
        }
    },
    ['power_evolved:scythe'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
		['Hits'] = 3,
        ['radius'] = 10,
        ['Special_Effect'] = {
        	['Name'] = 'Bleed Amplification'
        }
    },
    ['denji_chainsaw:flip'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 6,
        ['Effect'] = {
			['Name'] = 'Bleed',
			['Ticks'] = 4,
			['Multiplier'] = 0.0833333
		}
	},
    ['denji_chainsaw:spin'] = {
        ['AOE_TYPE'] = 'AoE (Cone)',
        ['angle'] = 60,
        ['Hits'] = 3,
        ['Effect'] = {
			['Name'] = 'Bleed',
			['Ticks'] = 4,
			['Multiplier'] = 0.0833333
		}
	},
    ['denji_chainsaw:barrage'] = {
        ['AOE_TYPE'] = 'AoE (Cone)',
        ['angle'] = 60,
        ['Hits'] = 6,
        ['Effect'] = {
			['Name'] = 'Bleed',
			['Ticks'] = 6,
			['Multiplier'] = 0.0833333
		}
	},
    ['angel_devil:sword'] = {
        ['AOE_TYPE'] = 'AoE (Line)',
        ['width'] = 7
    },
    ['angel_devil:spear'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 8
    },
    ['angel_devil:final'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 10
    },
    
    
    
	
	-- Update 8
    ['dio_heaven:barrage'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 8
    },
    ['dio_heaven:smite'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 12
    },
    ['dio_heaven:lightning'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 15
    },
    ['aokiji:partisan'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 8
    },
    ['aokiji:pheasant_beak'] = {
        ['AOE_TYPE'] = 'AoE (Line)',
        ['width'] = 8
    },
    ['aokiji:final'] = {
        ['AOE_TYPE'] = 'AoE (Full)'
    },
    ['haku:attack_1'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 7
    },
    ['haku:attack_2'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 9.5
    },
    ['haku:attack_3'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 12
    },
    ['todoroki_2:ice'] = {
        ['AOE_TYPE'] = 'AoE (Cone)',
        ['angle'] = 50,
    	['Special_Effect'] = {
    		['Name'] = 'Slow'
    	}
    },
    ['todoroki_2:ice_fire'] = {
        ['AOE_TYPE'] = 'AoE (Cone)',
        ['angle'] = 50,
    	['Special_Effect'] = {
    		['Name'] = 'Slow'
    	}
    },
    ['todoroki_2:heat'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 12.5,
    	['Special_Effect'] = {
    		['Name'] = 'Slow'
    	}
    },
    ['toshiro:ice_projectiles'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 6
    },
    ['toshiro:lunge'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 7
    },
    ['toshiro:dragon'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 8
    },
    ['ghiaccio:skate'] = {
        ['AOE_TYPE'] = 'AoE (Line)',
        ['width'] = 7
    },
    ['ghiaccio:breath'] = {
        ['AOE_TYPE'] = 'AoE (Cone)',
        ['angle'] = 45
    },
    ['ghiaccio:stomp'] = {
        ['AOE_TYPE'] = 'AoE (Cone)',
        ['angle'] = 45
    },
    ['ghiaccio:final'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 11
    },
    ['hiei:unsheath'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 7
    },
    ['hiei:dragon'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 9
    },
    ['hiei:fist'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 6
    },
    ['emilia:shot'] = {
        ['AOE_TYPE'] = 'AoE (Line)',
        ['width'] = 5,
    	['Special_Effect'] = {
    		['Name'] = 'Slow'
    	}
    },
    ['emilia:shards'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 8,
    	['Special_Effect'] = {
    		['Name'] = 'Slow'
    	}
    },
    ['emilia:flower'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 12,
    	['Special_Effect'] = {
    		['Name'] = 'Slow'
    	}
    },
    ['weather_report:ice'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 6
    },
    ['weather_report:frogs'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 15
    },
    ['weather_report:lightning'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 18
    },
    ['stone_free:punch'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 5
    },
    ['stone_free:barrage'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 6
    },
    ['stone_free:baseball'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 8
    },
    ['stone_free:strings'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 9
    },
    ['whitesnake:punch'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 6
    },
    ['whitesnake:gun'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 7.5
    },
    ['whitesnake:disc'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 9
    },
    ['cmoon:barrage'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['Hits'] = 3,
        ['radius'] = 6
    },
    ['cmoon:beam'] = {
        ['AOE_TYPE'] = 'AoE (Cone)',
        ['Hits'] = 2,
        ['angle'] = 30
    },
    ['cmoon:slam'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['Hits'] = 2,
        ['radius'] = 10
    },
    ['pucci_heaven:knives'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 4
    },
    ['pucci_heaven:slash'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 7
    },
    ['pucci_heaven:teleport'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['Hits'] = 4,
        ['radius'] = 15
    },
    ['pucci_heaven:final'] = {
        ['AOE_TYPE'] = 'Single'
    },
    ['starplatinum_p6:punch'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 6
    },
    ['starplatinum_p6:barrage'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 7
    },
    ['starplatinum_p6:timestop'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 13,
        ['Special_Effect'] = {
        	['Name'] = 'Timestop'
        }
    },
    ['kiss:broom'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 6
    },
    ['kiss:barrage'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 6
    },
    ['kiss:slam'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 12
    },


    ['yamamoto:slash'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 7,
		['Effect'] = {
			['Name'] = 'Burn',
			['Ticks'] = 5,
			['Multiplier'] = 0.06
		}
    },
    ['yamamoto:tornado'] = {
        ['AOE_TYPE'] = 'AoE (Full)',
		['Effect'] = {
			['Name'] = 'Burn',
			['Ticks'] = 5,
			['Multiplier'] = 0.06
		}
    },
    ['yamamoto:pillars'] = {
        ['AOE_TYPE'] = 'AoE (Full)',
		['Effect'] = {
			['Name'] = 'Burn',
			['Ticks'] = 5,
			['Multiplier'] = 0.06
		}
    },
    ['yamamoto:skeletons'] = {
        ['AOE_TYPE'] = 'AoE (Full)',
		['Effect'] = {
			['Name'] = 'Burn',
			['Ticks'] = 5,
			['Multiplier'] = 0.06
		}
    },


    ['shinji:multicut'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 8
    },
    ['shinji:dash'] = {
        ['AOE_TYPE'] = 'AoE (Line)',
        ['width'] = 10
    },
    ['shinji:cero'] = {
        ['AOE_TYPE'] = 'AoE (Cone)',
        ['angle'] = 45
    },
    ['julius:time_orb'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 5
    },
    ['julius:multiple_throws'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 12
    },
    ['julius:time_orb_teleport'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 8
    },






	-- Update ESDEATH
	['esdeath:ice_spike'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 5
	},
	['esdeath:upwards_slash'] = {
		['AOE_TYPE'] = 'AoE (Line)',
        ['radius'] = 7
	},
	['esdeath:ice_meteor'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 12
	},
	['esdeath:timestop'] = {
		['AOE_TYPE'] = 'AoE (Full)',
        ['Special_Effect'] = {
        	['Name'] = 'Freeze'
        }
	},
	
	-- Update AIZEN
	['aizen_hog:box'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 12
    },
    ['aizen_hog:roar'] = {
        ['AOE_TYPE'] = 'AoE (Full)'
    },
    ['aizen_hog:slashes'] = {
        ['AOE_TYPE'] = 'AoE (Cone)',
        ['angle'] = 60
    },
    ['aizen_hog:fragor'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 10
    },
    ['aizen_hog:pillar'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 10
    },
    ['aizen_hog:ultrafragor'] = {
        ['AOE_TYPE'] = 'AoE (Full)'
    },
    

	-- Update Bleach
	['gin:pierce1'] = {
        ['AOE_TYPE'] = 'AoE (Line)',
        ['width'] = 7
    },
    ['gin:pierce2'] = {
        ['AOE_TYPE'] = 'AoE (Line)',
        ['width'] = 9
    },
    ['gin:spear'] = {
        ['AOE_TYPE'] = 'AoE (Line)',
        ['width'] = 12
    },
    ['ichigo_black:lunge'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 7
    },
    ['ichigo_black:ult'] = {
        ['AOE_TYPE'] = 'AoE (Line)',
        ['width'] = 12
    },
    ['ichigo_black:mugetsu'] = {
        ['AOE_TYPE'] = 'Single'
    },
    ['ichigo_black:dash_spin'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 8.5
    },
    ['ichigo_black:spikes'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 11
    },
    ['soifon:ground_slam'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 9
    },
    ['soifon:stab'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 7
    },
    ['soifon:missile'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 11
    },
    ['kenpachi:scream'] = {
        ['AOE_TYPE'] = 'AoE (Full)',
        ['Special_Effect'] = {
        	['Name'] = 'Stun'
        }
    },
    ['kenpachi:kendo'] = {
        ['AOE_TYPE'] = 'AoE (Cone)',
        ['angle'] = 30
    },
    ['kenpachi:spin'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 9
    },

	-- Update 7
    ['kuma_unit:punch'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 5
    },
    ['kuma_unit:barrage'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 7
    },
    ['kuma_unit:shock'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 14
    },
    ['tengen:overhead_slash'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 7
    },
    ['tengen:multiple_slashes'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 8
    },
    ['tengen:spinning_run'] = {
        ['AOE_TYPE'] = 'AoE (Cone)',
        ['angle'] = 50
    },
    ['asta:dash_slash'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 5
    },
    ['asta:cross'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 6
    },
    ['asta:multi_slash'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 8
    },
    ['asta:hurricane'] = {
        ['AOE_TYPE'] = 'AoE (Cone)',
        ['angle'] = 60
    },
    ['yuno:daggers'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
		['Hits'] = 3,
        ['radius'] = 6
    },
    ['yuno:tornado'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
		['Hits'] = 3,
        ['radius'] = 10
    },
    ['yuno:beam'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
		['Hits'] = 3,
        ['radius'] = 12
    },
    
    --// LUCK AND LUCK EVO (battlelust effect)
    ['luck:dropkick'] = {
        ['AOE_TYPE'] = 'AoE (Line)',
        ['width'] = 5
    },
    ['luck:swipe'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 5
    },
    ['luck_thunder_fiend:dropkick'] = {
        ['AOE_TYPE'] = 'AoE (Line)',
        ['width'] = 5,
        ['Special_Effect'] = {
        	['Name'] = 'Battlelust'
        }
    },
    ['luck_thunder_fiend:swipe'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 5
    },
    ['luck_thunder_fiend:jump'] = {
        ['AOE_TYPE'] = 'AoE (Line)',
        ['width'] = 7
    },
    
    
    ['noelle:ball'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 5
    },
    ['noelle:multi_balls'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 8
    },
    ['noelle:geyser'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 10
    },
    ['noelle:dragon'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 12
    },
    ['yami:lunge'] = {
        ['AOE_TYPE'] = 'AoE (Line)',
        ['width'] = 2
    },
    ['yami:multi_slashes'] = {
        ['AOE_TYPE'] = 'AoE (Line)',
        ['width'] = 3.5
    },
    ['yami:slash'] = {
        ['AOE_TYPE'] = 'AoE (Line)',
        ['width'] = 4
    },
    ['yami_evolved:slash'] = {
        ['AOE_TYPE'] = 'AoE (Line)',
        ['width'] = 4
    },
    ['magna:fireballs'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 4
    },
    ['magna:swing'] = {
        ['AOE_TYPE'] = 'AoE (Cone)',
        ['angle'] = 40
    },
    ['magna:bomb'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 9
    },
    ['wendy:throw'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 5
    },
    ['wendy:beam'] = {
        ['AOE_TYPE'] = 'AoE (Line)',
        ['width'] = 6
    },


	-- Update 6.5
    ['luffy_nightmare:slash'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 6
    },
    ['luffy_nightmare:smash'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 8
    },
    ['luffy_nightmare:barrage'] = {
        ['AOE_TYPE'] = 'AoE (Line)',
        ['width'] = 5
    },
    
    --// PERONA NORMAL AND PERONA EVO (HAS SLOWS) - Evanie
    ['perona:ghost_spiral'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 7
    },
    ['perona:ghost'] = {
        ['AOE_TYPE'] = 'Single'
    },
    ['perona:big_ghost'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 9
    },
    ['perona_ghost_princess:ghost_spiral'] = {
    	['AOE_TYPE'] = 'AoE (Circle)',
    	['radius'] = 7,
    	['Special_Effect'] = {
    		['Name'] = 'Slow'
    	}
    },
    ['perona_ghost_princess:ghost'] = {
    	['AOE_TYPE'] = 'Single',
    	['Special_Effect'] = {
    		['Name'] = 'Slow'
    	}
    },
    ['perona_ghost_princess:big_ghost'] = {
    	['AOE_TYPE'] = 'AoE (Circle)',
    	['radius'] = 9,
    	['Special_Effect'] = {
    		['Name'] = 'Slow'
    	}
    },
    
    ['brook:slashes'] = {
        ['AOE_TYPE'] = 'AoE (Cone)',
        ['angle'] = 45
    },
    ['brook:guitar_projectile'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 9
    },
    ['brook:soul_king'] = {
        ['AOE_TYPE'] = 'AoE (Full)',
        ['Special_Effect'] = {
        	['Name'] = 'Motivate'
        }
    },
    ['moria:combo'] = {
        ['AOE_TYPE'] = 'AoE (Cone)',
        ['angle'] = 50
    },
    ['moria:bat_tornado'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 7
    },
    ['moria:shadow_clone'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 8
    },
    ['moria:shadow_dive'] = {
        ['AOE_TYPE'] = 'AoE (Circle)',
        ['radius'] = 9.5
    },





	['yuta:beam'] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['Hits'] = 7,
		['width'] = 15
	},
	['yuta:micro'] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['Hits'] = 3,
		['angle'] = 45
	},
	['yuta:flash'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8
	},
	['yuta:slash'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6
	},
	['geto:spiral'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 12
	},
	['geto:baby'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6
	},
	['geto:centipede'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8
	},
	['sukuna:dismantle'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 14
	},
	['sukuna:cleave'] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 45,
		['Special_Effect'] = {
			['Name'] = 'Dismembered',
		},
		['Effect'] = {
			['Name'] = 'Bleed',
			['Ticks'] = 3,
			['Multiplier'] = 0.0833
		}
	},
	['sukuna:fire_arrow'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8
	},
	['megumi:wolf'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 7
	},
	['megumi:shadow_garden'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 11
	},
	['megumi_evolved:owl'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 9
	},
	['megumi:owl'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 9
	},
	['megumi_evolved:wolf'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 7,
		['Special_Effect'] = {
			['Name'] = 'Cursed (30%)',
		},
	},
	['kento:precision_slash'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8
	},
	['kento:collapse'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 9
	},
	['kento:multiple_slashes'] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 60
	},
	['kento:punch'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 7
	},
	['nobara:nail'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6,
		['Effect'] = {
			['Name'] = 'Bleed',
			['Ticks'] = 3,
			['Multiplier'] = 0.083333
		}
		
	},
	['nobara:strong_nail'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8
	},
	['nobara:multi_slashes'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 11,
		['Hits'] = 4,
	},
	['toge:shout_explode'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6
	},
	['toge:shout_3'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 13.5
	},
	['toge:shout_2'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 9,
		['Special_Effect'] = {
			['Name'] = 'Stun',
		},
	},
	
	
	['itadori:slam'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 11
	},
	['itadori:black_flash'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 11
	},
	['itadori:punches'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 7
	},
	['gojo:blue'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6
	},
	['gojo:domain'] = {
		['AOE_TYPE'] = 'Single'
	},
	['gojo:purple'] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 10
	},
	['gojo:red'] = {
		['AOE_TYPE'] = 'AoE (Full)'
	},
	
	['trunks:god_breaker'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6
	},
	['trunks:burning_slash'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 9
	},
	['trunks:dome'] = {
		['AOE_TYPE'] = 'AoE (Full)'
	},
	['trunks:burning_attack'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 7
	},
	['cell:storm'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 11
	},
	['cell:beam'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 14
	},
	['cell:flare'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8
	},
	['cell:purple_blasts'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6
	},
	['erza:sword_strike'] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 7
	},
	['stand_barrage'] = {
		['AOE_TYPE'] = 'Single'
	},
	['overhaul:spikes'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6
	},
	['uryu:beam'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10
	},
	['gaara:coffin'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8
	},
	['akaza_unit:air_type'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 3
	},
	['byakuya:projectiles'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6
	},
	['gaara:spikes'] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 45
	},
	['katakuri:mochi_barrage'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 12
	},
	['tatara:flamethrower'] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 45,
		['Effect'] = {
			['Name'] = 'Burn',
			['Ticks'] = 5,
			['Multiplier'] = 0.06666
		}
	},
	['rin:skill_two'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 9.5
	},
	['inosuke:cross'] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 50
	},
	['krillin:destructo_disc'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 4
	},
	['netero:99th_hand'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 13.5
	},
	['lucy:taurus_attack'] = {
		['AOE_TYPE'] = 'Single'
	},
	['juvia:slashes'] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 30
	},
	['kite:scythe'] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 70
	},
	['colossal_titan:steam'] = {
		['AOE_TYPE'] = 'AoE (Full)'
	},
	['frieza:ball'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10
	},
	['all_might:spin_punch'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 13
	},
	['tatara:kagune'] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 45
	},
	['apshot'] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 2.5
	},
	['zetsu:spawn'] = {
		['AOE_TYPE'] = 'Single'
	},
	['piccolo:special_beam_cannon'] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 4
	},
	['goku_ssb:kamehameha_kaio'] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 8
	},
	['naruto_pts:slash'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6
	},
	['recoome:beam'] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 6
	},
	['stand_barrage_heavy_end'] = {
		['AOE_TYPE'] = 'Single'
	},
	['juvia:geyser'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8
	},
	['natsu:breath'] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 50
	},
	['katakuri:fire_mochi_evolved'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6,
		['Effect'] = {
			['Name'] = 'Burn',
			['Ticks'] = 5,
			['Multiplier'] = 0.02
		}
	},
	['frieza_boss:spawn_units'] = {
		['AOE_TYPE'] = 'Single'
	},
	['gildarts_evolved:aura'] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 50,
    	['Special_Effect'] = {
    		['Name'] = 'Shatter'
    	}
	},
	['arima:both_attacks'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10
	},
	['luffy_marineford:barrage'] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 70
	},
	['gray:spears'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 7,
		['Special_Effect'] = {
			['Name'] = 'Freeze',
		}
	},
	['colossal_titan:spawn'] = {
		['AOE_TYPE'] = 'Single'
	},
	['king_crimson:back_attack'] = {
		['AOE_TYPE'] = 'Single'
	},
	['inosuke:slashes'] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 50
	},
	['gray:hammer'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 9
	},
	['natsu_evolved:slam'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 7,
		['Effect'] = {
			['Name'] = 'Burn',
			['Ticks'] = 5,
			['Multiplier'] = 0.08
		}
	},
	['star_platinum_ts'] = {
		['AOE_TYPE'] = 'AoE (Full)'
	},
	['eto:jump'] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 60
	},
	['king_crimson:slice'] = {
		['AOE_TYPE'] = 'Single'
	},
	['mihawk:slash'] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 5
	},
	['amon:smash_1'] = {
		['AOE_TYPE'] = 'Single'
	},
	['kizaru:teleport'] = {
		['AOE_TYPE'] = 'Single'
	},
	['rin:skill_one'] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 50,
		['Effect'] = {
			['Name'] = 'Burn',
			['Ticks'] = '3',
			['Multiplier'] = 0.075
		}
	},
	['akaza_unit:annihilation'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6
	},
	['all_might:punch'] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 10
	},
	['erza_valkyrie:dash'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 7
	},
	['naruto_pts_evolved:slam'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8
	},
	['jellal:pleiades'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8.5
	},
	['saiki:rock'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 5
	},
	['frieza:death_beam'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 4
	},
	['kaneki:jump'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 4
	},
	['ulquiorra_evolved:dash'] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 10
	},
	['rukia:juhaku'] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 60
	},
	['aizen:lightning'] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 60
	},
	['ulquiorra_evolved:cero'] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 10
	},
	['gray:cannon'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 11
	},
	['rengoku:dragon'] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 10
	},
	['ace:fireflies'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6,
		['Effect'] = {
			['Name'] = 'Burn',
			['Ticks'] = 5,
			['Multiplier'] = 0.05
		}
	},
	['lucy_leo:projectiles'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8
	},
	['killua_godspeed_evolved:dash'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6,
		['Special_Effect'] = {
			['Name'] = 'Stun',
		}
	},
	['future_gohan:beam_1'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8
	},
	['deidara:c0'] = {
		['AOE_TYPE'] = 'AoE (Full)'
	},
	['lucy_taurus:smash'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 5
	},
	['daki:beam_aoe'] = {
		['AOE_TYPE'] = 'AoE (Full)'
	},
	['saiki:volleyball'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 3
	},
	['juuzou:line'] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 60
	},
	['goku_ssb:kamehameha'] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 6
	},
	['ulquiorra_evolved:spear'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 13.5
	},
	['natsu_evolved:breath'] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 50
	},
	['all_might:land'] = {
		['AOE_TYPE'] = 'Single'
	},
	['krillin:double_beams'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 3
	},
	['gildarts_evolved:punch'] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 50,
    	['Special_Effect'] = {
    		['Name'] = 'Shatter'
    	}
	},
	['gon_adult:final_rock'] = {
		['AOE_TYPE'] = 'AoE (Full)'
	},
	['beast_titan_boss:rock'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8
	},
	['aizen:illusion'] = {
		['AOE_TYPE'] = 'Single'
	},
	['zarbon_evolved:fly_attack'] = {
		['AOE_TYPE'] = 'AoE (Full)'
	},
	['zarbon:blast'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 7
	},
	['hisoka:5_kind'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10
	},
	['eto:laser'] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 60
	},
	['gildarts:slam'] = {
		['AOE_TYPE'] = 'AoE (Full)'
	},
	['kokushibo:slash'] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 60
	},
	['gajeel:sword'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 5
	},
	['renji:strike'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 12
	},
	['akaza_raid:compass'] = {
		['AOE_TYPE'] = 'Single'
	},
	['akaza:compass'] = {
		['AOE_TYPE'] = 'Single'
	},
	['all_might:cross'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10
	},
	['shanks:lightning'] = {
		['AOE_TYPE'] = 'AoE (Full)'
	},
	['saiki:bomb'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 9
	},
	['ulquiorra:spin'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 7.25
	},
	['broly:smash'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 5
	},
	['rengoku_evolved:undulation'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6,
		['Effect'] = {
			['Name'] = 'Burn',
			['Ticks'] = 5,
			['Multiplier'] = 0.1
		}
	},
	['renji:orb'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 7
	},
	['aokiji:freeze'] = {
		['AOE_TYPE'] = 'AoE (Full)'
	},
	['kaneki_centipede:swipe'] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 60,
		['Effect'] = {
			['Name'] = 'Bleed',
			['Ticks'] = 3,
			['Multiplier'] = 0.083333
		}
	},
	['zenitsu:lightning'] = {
		['AOE_TYPE'] = 'Single'
	},
	['crocodile:spikes'] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 5
	},
	['sasuke:dragon_fire'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8
	},
	['akaza_unit:disorder'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 12
	},
	['zoro:slashes'] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 4
	},
	['arima:ixa_attack'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10
	},
	['kisuke:shield_blasts'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10
	},
	['levi:spins'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 2
	},
	['goku:beam'] = {
		['AOE_TYPE'] = 'Single'
	},
	['future_gohan:ki_blasts'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6
	},
	['rengoku_evolved:universe'] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 50
	},
	['naruto:rasengan_base'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 4
	},
	['dabi:fire_punch'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 5,
		['Effect'] = {
			['Name'] = 'Burn',
			['Ticks'] = 5,
			['Multiplier'] = 0.02
		}
	},
	['future_gohan:beam_2'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10
	},
	['arima:narukami_attack'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 11
	},
	['jellal:meteor'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 12
	},
	['crocodile:tornado'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10
	},
	['ichigo:slash'] = {
		['AOE_TYPE'] = 'Single'
	},
	['rengoku:tiger'] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 8,
		['Effect'] = {
			['Name'] = 'Burn',
			['Ticks'] = 5,
			['Multiplier'] = 0.02
		}
	},
	['starrk_wolf_unit:explode'] = {
		['AOE_TYPE'] = 'AoE (Full)'
	},
	['tatara:flamethrower_2'] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 45
	},
	['ace:enkai'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10
	},
	['hisoka:slash'] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 7
	},
	['madara:susanoo_evolved'] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 110
	},
	['tanjiro:whirlpool'] = {
		['AOE_TYPE'] = 'AoE (Full)'
	},
	['lucy:aquarius_attack'] = {
		['AOE_TYPE'] = 'Single'
	},
	['dio:road_roller'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 9
	},
	['flag_bearer:buff_moving'] = {
		['AOE_TYPE'] = 'AoE (Full)'
	},
	['amaterasu_2'] = {
		['AOE_TYPE'] = 'Single',
		['Effect'] = {
			['Name'] = 'Burn',
			['Ticks'] = 10,
			['Multiplier'] = 0.025
		}
	},
	['madara:susanoo'] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 110
	},
	['naruto_pts:rasengan'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 4
	},
	['yahaba:arrow_2'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 7
	},
	['ace:pillar'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8
	},
	['law:gamma'] = {
		['AOE_TYPE'] = 'Single'
	},
	['all_might:smash_evolved'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 15,
		['Special_Effect'] = {
			['Name'] = 'Knockback',
		}
	},
	['naruto_pts:chuck'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8
	},
	['luffy_marineford:stomp'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6
	},
	['lucy:leo_attack'] = {
		['AOE_TYPE'] = 'Single'
	},
	['starrk:shoot'] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 5
	},
	['hierophant_green:splash'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['Hits'] = 3,
		['radius'] = 3.5
	},
	['titan:stomp'] = {
		['AOE_TYPE'] = 'AoE (Full)'
	},
	['rukia:tsuki'] = {
		['AOE_TYPE'] = 'Single',
		['Special_Effect'] = {
			['Name'] = 'Freeze',
		}
	},
	['gildarts_evolved:slam'] = {
		['AOE_TYPE'] = 'AoE (Full)',
    	['Special_Effect'] = {
    		['Name'] = 'Shatter'
    	}
	},
	['jonathan:punches'] = {
		['AOE_TYPE'] = 'Single'
	},
	['whitebeard:waves'] = {
		['AOE_TYPE'] = 'AoE (Full)'
	},
	['attack_titan:spawn_self'] = {
		['AOE_TYPE'] = 'Single'
	},
	['erwin:spawn_unit'] = {
		['AOE_TYPE'] = 'Single'
	},
	['jose:spawn_shades'] = {
		['AOE_TYPE'] = 'Single'
	},
	['broly:beam'] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 6
	},
	['amaterasu'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 5
	},
	['uraraka:rock_throw_single'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 7
	},
	['noro:attack_1'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 4
	},
	['naruto_pts_evolved:beam'] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 40
	},
	['whitebeard:earthquake'] = {
		['AOE_TYPE'] = 'AoE (Full)'
	},
	['naruto_pts_evolved:bomb_throw'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6
	},
	['sanji:table_kick'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 4
	},
	['sasori:puppet_spawn'] = {
		['AOE_TYPE'] = 'Single'
	},
	['akainu:erupt'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6
	},
	['erza_lightning:strikes'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8
	},
	['muzan:heal'] = {
		['AOE_TYPE'] = 'AoE (Full)'
	},
	['female_titan:invincibility_activate'] = {
		['AOE_TYPE'] = 'Single'
	},
	['katakuri:donut'] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 6
	},
	['katakuri:mochi_barrage_evolved'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 12
	},
	['erza_valkyrie:wheel'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 11
	},
	['guldo:paralysis'] = {
		['AOE_TYPE'] = 'AoE (Full)'
	},
	['flag_bearer:hold_down'] = {
		['AOE_TYPE'] = 'AoE (Full)'
	},
	['pitou:jump_slash'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 7
	},
	['sasuke:fireball'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 5
	},
	['luffy:punches'] = {
		['AOE_TYPE'] = 'Single'
	},
	['jason:shield'] = {
		['AOE_TYPE'] = 'Single'
	},
	['rin:skill_three'] = {
		['AOE_TYPE'] = 'AoE (Full)'
	},
	['jiren:counter'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 5
	},
	['jellal:swords'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 7
	},
	['kizaru:kick'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 12
	},
	['usopp:bamboo'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 4
	},
	['britannia_soldier:rifle'] = {
		['AOE_TYPE'] = 'Single'
	},
	['erza_samurai:skill_1'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 5,
		['Effect'] = {
			['Name'] = 'Bleed',
			['Ticks'] = 3,
			['Multiplier'] = 0.0833333
		}
	},
	['pitou:dash_slash'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6,
		['Effect'] = {
			['Name'] = 'Bleed',
			['Ticks'] = 3,
			['Multiplier'] = 0.0833333
		}
	},
	['ichigo_mask:cross'] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 7
	},
	['erza_valkyrie:final'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 15
	},
	['arima:owl_slash'] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 60
	},
	['eto:shards'] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 8
	},
	['ichigo_hollow:cero'] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 8
	},
	['kaneki_centipede:jump'] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 60
	},
	['jellal:chariot'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10
	},
	['warhammer_titan:slam'] = {
		['AOE_TYPE'] = 'AoE (Full)'
	},
	['gildarts:punch'] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 50
	},
	['ginyu:spawn_unit'] = {
		['AOE_TYPE'] = 'Single'
	},
	['nezuko:slashes'] = {
		['AOE_TYPE'] = 'Single',
		['Effect'] = {
			['Name'] = 'Bleed',
			['Ticks'] = 3,
			['Multiplier'] = 0.033333
		}
	},
	['usopp:slingshot_basic'] = {
		['AOE_TYPE'] = 'Single'
	},
	['bakugou:explosions_new'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10
	},
	['guldo:spike'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 7
	},
	['noro:attack_2'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10
	},
	['vegeta:gun'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 4
	},
	['kc:time_erase'] = {
		['AOE_TYPE'] = 'Single'
	},
	['vegeta:galick_gun'] = {
		['AOE_TYPE'] = 'AoE (Full)'
	},
	['pain:almighty_push'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 15,
		['Special_Effect'] = {
			['Name'] = 'Knockback',
		}
	},
	['pitou_boss:heal'] = {
		['AOE_TYPE'] = 'Single'
	},
	['byakuya:bankai'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8
	},
	['crazy_diamond_barrage'] = {
		['AOE_TYPE'] = 'Single'
	},
	['lelouch:summon'] = {
		['AOE_TYPE'] = 'Single'
	},
	['erza:horizontal_slash'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6.5
	},
	['delaware_smash'] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 6.5
	},
	['starrk:metra'] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 20
	},
	['gray_evolved:bow'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 12
	},
	['lelouch:geass'] = {
		['AOE_TYPE'] = 'AoE (Full)'
	},
	['erwin:buff_units'] = {
		['AOE_TYPE'] = 'AoE (Full)'
	},
	['ichigo:slash_2'] = {
		['AOE_TYPE'] = 'Single'
	},
	['rui:webs'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10
	},
	['shuriken_throw'] = {
		['AOE_TYPE'] = 'Single'
	},
	['zenitsu:lightning_2'] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 8
	},
	['eren_final:rumbling'] = {
		['AOE_TYPE'] = 'Single'
	},
	['shinkiro:lazer'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 4
	},
	['killua_godspeed_evolved:rush'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 12
	},
	['netero:zero_hand'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 16
	},
	['piccolo:mouth_beam'] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 4
	},
	['hierophant_green:splash_2'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['Hits'] = 3,
		['radius'] = 6
	},
	['shinkiro:spawn'] = {
		['AOE_TYPE'] = 'Single'
	},
	['sanji:kick_combo'] = {
		['AOE_TYPE'] = 'Single'
	},
	['gold_experience:frog_throw_2'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6
	},
	['meruem:tail_swipes'] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 50
	},
	['broly:aoe_attacks_evolved'] = {
		['AOE_TYPE'] = 'AoE (Full)'
	},
	['lucy_aquarius:splash'] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 30
	},
	['big_puppet:shield'] = {
		['AOE_TYPE'] = 'Single'
	},
	['shanks:slashes'] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 90
	},
	['goku_black:slicer'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 5
	},
	['juuzou:spin'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10,
		['Effect'] = {
			['Name'] = 'Bleed',
			['Ticks'] = 3,
			['Multiplier'] = 0.0833333
		}
	},
	['tatara_evolved:slam'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 15
	},
	['jonathan:ripple'] = {
		['AOE_TYPE'] = 'AoE (Full)'
	},
	['todoroki:ice_fire'] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 60,
		['Effect'] = {
			['Name'] = 'Burn',
			['Ticks'] = 3,
			['Multiplier'] = 0.033333
		}
	},
	['erza_lightning:cloud'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 12
	},
	['kisuke:buff'] = {
		['AOE_TYPE'] = 'AoE (Full)'
	},
	['ichigo_hollow:slash'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 3
	},
	['tatara_evolved:flamethrower_2'] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 45
	},
	['tatara:slam'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 15
	},
	['killua:thunderbolt'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10
	},
	['gildarts:final'] = {
		['AOE_TYPE'] = 'AoE (Full)'
	},
	['dabi:cremation'] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 60,
		['Effect'] = {
			['Name'] = 'Burn',
			['Ticks'] = 10,
			['Multiplier'] = 0.004
		}
	},
	['deidara_explosion'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 5
	},
	['gon:rock'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8
	},
	['gold_experience:tree'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 5
	},
	['katakuri:donut_evolved'] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 6,
		['Special_Effect'] = {
			['Name'] = 'Slow',
		}
	},
	['crocodile:throw_explosion'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8
	},
	['attack_titan:spawn_titan'] = {
		['AOE_TYPE'] = 'Single'
	},
	['gon_adult:single_smash'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10
	},
	['kaneki:stab'] = {
		['AOE_TYPE'] = 'Single'
	},
	['itachi_boss:start_teleport'] = {
		['AOE_TYPE'] = 'Single'
	},
	['titan_shifter_spawn'] = {
		['AOE_TYPE'] = 'Single'
	},
	['dio:road_roller_new'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10,
		['Special_Effect'] = {
			['Name'] = 'Freeze',
		}
	},
	['gon:scissors'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6
	},
	['gajeel:roar'] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 60
	},
	['akainu:shower'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 20
	},
	['erza:downward_slash'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 5
	},
	['killua_godspeed_evolved:narukami'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 9
	},
	['armin:titan_shift'] = {
		['AOE_TYPE'] = 'AoE (Full)'
	},
	['rengoku_evolved:dragon'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 18
	},
	['broly:aoe_attacks'] = {
		['AOE_TYPE'] = 'AoE (Full)'
	},
	['kisuke:net'] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 10
	},
	['akainu:magma'] = {
		['AOE_TYPE'] = 'Single'
	},
	['shanks:haki'] = {
		['AOE_TYPE'] = 'AoE (Full)'
	},
	['luffy2:gun'] = {
		['AOE_TYPE'] = 'Single'
	},
	['amon:smash_2'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6
	},
	['akaza_unit:compass'] = {
		['AOE_TYPE'] = 'Single'
	},
	['gajeel:lance'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8
	},
	['kisuke:portal'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6
	},
	['ulquiorra:balls_throw'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6
	},
	['killua_godspeed:narukami'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 9
	},
	['touka:jump_attack'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10
	},
	['ichigo_mask:slash'] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 10
	},
	['starrk:summon'] = {
		['AOE_TYPE'] = 'Single'
	},
	['tanjiro:wheel'] = {
		['AOE_TYPE'] = 'Single'
	},
	['sanji:diabe_jamble'] = {
		['AOE_TYPE'] = 'Single'
	},
	['akaza_unit:leaves'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8
	},
	['blackbeard:liberation'] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 8,
		['Special_Effect'] = {
			['Name'] = 'Cursed (15%)',
		}
	},
	['jiren:power_impact'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 20
	},
	['all_might:jump'] = {
		['AOE_TYPE'] = 'Single'
	},
	['sasuke:chidori'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 5
	},
	['spawn_wolf'] = {
		['AOE_TYPE'] = 'Single'
	},
	['natsu:slam'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 7,
		['Effect'] = {
			['Name'] = 'Burn',
			['Ticks'] = 5,
			['Multiplier'] = 0.08
		}
	},
	['aizen:dragon'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8
	},
	['akainu:punch'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 4,
		['Effect'] = {
			['Name'] = 'Burn',
			['Ticks'] = 3,
			['Multiplier'] = 0.1
		}
	},
	['nezuko:demon_slashes'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 7
	},
	['meruem_evolved:rush'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8
	},
	['aizen:coffin'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10
	},
	['katakuri:fire_mochi'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6,
		['Effect'] = {
			['Name'] = 'Burn',
			['Ticks'] = 5,
			['Multiplier'] = 0.02
		}
	},
	['kakashi:lightning'] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 6
	},
	['grimmjow:grand_cero'] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 10
	},
	['todoroki:ice'] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 60,
		['Special_Effect'] = {
			['Name'] = 'Slow',
		}
	},
	['heal_mage:heal'] = {
		['AOE_TYPE'] = 'AoE (Full)'
	},
	['grimmjow:cero_left'] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 8
	},
	['lelouch:summon_2'] = {
		['AOE_TYPE'] = 'Single'
	},
	['madara:fan'] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 70
	},
	['overhaul:deconstruct'] = {
		['AOE_TYPE'] = 'Single'
	},
	['deidara_clone:self_destruct'] = {
		['AOE_TYPE'] = 'AoE (Full)'
	},
	['all_might:smash'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 15
	},
	['zeke:rock_throw_2'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10
	},
	['muzan:spawn_units'] = {
		['AOE_TYPE'] = 'Single'
	},
	['gon_adult:barrage'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 14
	},
	['deidara:create_unit'] = {
		['AOE_TYPE'] = 'Single'
	},
	['mihawk:rush'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 3
	},
	['kizaru_unit:barrage'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10
	},
	['blackbeard:black_hole'] = {
		['AOE_TYPE'] = 'AoE (Full)'
	},
	['levi:slashes_1'] = {
		['AOE_TYPE'] = 'Single',
		['Effect'] = {
			['Name'] = 'Bleed',
			['Ticks'] = 3,
			['Multiplier'] = 0.0833333
		}
	},
	['kite:gun'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 5
	},
	['goku_black:scythe'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10
	},
	['madara:susanoo_small'] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 90
	},
	['madara:susanoo_small_evolved'] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 90,
		['Effect'] = {
			['Name'] = 'Burn',
			['Ticks'] = 5,
			['Multiplier'] = 0.04
		}
	},
	['ginyu_force:spawn'] = {
		['AOE_TYPE'] = 'Single'
	},
	['erza_samurai:skill_3'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10
	},
	['kite:mace'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 15
	},
	['hisoka:spin_projectiles'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8,		
		['Special_Effect'] = {
			['Name'] = 'Slow',
		}
	},
	['killua_godspeed:dash'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6
	},
	['zeke:rock_throw'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6
	},
	['killua_godspeed:rush'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 12
	},
	['enmu:hand'] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 60
	},
	['erza_lightning:vault_jump'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 5
	},
	['natsu_evolved:spin_slam'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 12
	},
	['gon:paper'] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 5
	},
	['ulquiorra:cero'] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 7
	},
	['pitou:terpischora_rush'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 8
	},
	['gildarts:aura'] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 50
	},
	['juvia:ball'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 6
	},
	['whitebeard:slash'] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 90
	},
	['rengoku_evolved:unknowing'] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 60
	},
	['netero:third_hand'] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 80
	},
	['uraraka:rock_throw'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10
	},
	['meruem_evolved:beam'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 12
	},
	['gildarts_evolved:final'] = {
		['AOE_TYPE'] = 'AoE (Full)',
    	['Special_Effect'] = {
    		['Name'] = 'Shatter'
    	}
	},
	['rukia:hakuren'] = {
		['AOE_TYPE'] = 'AoE (Full)'
	},
	['touka:attack_1'] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 4
	},
	['juvia_boss:shield'] = {
		['AOE_TYPE'] = 'Single'
	},
	['natsu:spin_slam'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 12
	},
	['levi:slashes_2'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 4
	},
	['meruem:summersault'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 7
	},
	['genos:lazer'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 4
	},
	['crazy_diamond:stun_punch'] = {
		['AOE_TYPE'] = 'Single',
		['Special_Effect'] = {
			['Name'] = 'Stun',
		}
	},
	['stand_kick_barrage'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 2
	},
	['zoro:spin'] = {
		['AOE_TYPE'] = 'AoE (Full)'
	},
	['spin_single_kick'] = {
		['AOE_TYPE'] = 'Single'
	},
	['ant_queen:egg'] = {
		['AOE_TYPE'] = 'Single'
	},
	['deku:punch_1'] = {
		['AOE_TYPE'] = 'AoE (Line)',
		['width'] = 4
	},
	['pain:meteor'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10
	},
	['genos:missile'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 2.5
	},
	['uryu:shot'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 4
	},
	['tatara_evolved:flamethrower'] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 45,
		['Effect'] = {
			['Name'] = 'Burn',
			['Ticks'] = 5,
			['Multiplier'] = 0.1333
		}
	},
	['killua:godspeed'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 10
	},
	['jellal_raid:buff'] = {
		['AOE_TYPE'] = 'Single'
	},
	['lucy:multi_summon'] = {
		['AOE_TYPE'] = 'Single'
	},
	['law:shot'] = {
		['AOE_TYPE'] = 'Single'
	},
	['erza_samurai:skill_2'] = {
		['AOE_TYPE'] = 'AoE (Cone)',
		['angle'] = 40
	},
	['uryu:volley'] = {
		['AOE_TYPE'] = 'AoE (Circle)',
		['radius'] = 7
	}
}