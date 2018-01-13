#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Alan Veloso, Elton Quaresma
"""

# Grafo que representa a disposição dos prédios da Universidade Federal do Pará (UFPa) campus Profissional
class graph: 
	vertex = {"P3", "BA1", "RU", "ITEC", "ICED", "NAEA", "ICSA", "BA2", "Ver-o-Pezinho", "LEEC", "LEM", 
		  "AA", "LABTIC", "PPGEM", "UNIVERSITEC", "INCUBADORA", "A.ARQ", "AUD", "NUMA", "ICJ"}
	
	edge = {"P3" : { "LEEC" : 130 , "BA1" : 130 , "ICJ" : 270},
	    		"BA1": { "P3" : 130, "RU": 70 }, 
			"RU": {"BA1" : 70, "Ver-o-Pezinho": 40 , "BA2": 50, "ITEC": 100},
			"ITEC": {"RU" : 100, "ICED": 72 },
			"ICED": {"ICED" : 72, "NAEA": 92 },
			"NAEA": {"ICED" : 92, "ICSA": 80 },
			"ICSA": {"NAEA" : 80 , "BA2": 130}, 
			"BA2": {"RU": 50, "ICSA": 130, "ver-o-zinho" : 20 },
			"Ver-o-Pezinho": {"RU": 40, "BA2": 20 }, 
			"LEEC": {"P3": 130, "LEM":100, "PPGEM" : 215 }, 
			"LEM": {"LEEC" : 100, "AA": 90 }, 
			"AA": {"LEM": 90, "LABTIC" : 70, "PPGEM": 70 }, 
			"LABTIC": {"AA": 70 }, 
			"PPGEM": {"LEEC" : 215, "AA": 70, "AUD": 200, "UNIVERSITEC": 25  }, 
			"UNIVERSITEC": {"INCUBADORA": 70, "PPGEM": 25 }, 
			"INCUBADORA": {"UNIVERSITEC": 70, "A.ARQ": 100 }, 
			"A.ARQ": {"INCUBADORA": 100 }, 
			"AUD": {"PPGEM": 200, "NUMA": 83}, 
			"NUMA": {"AUD": 83 }, 
			"ICJ": {"P3" : 270}}
