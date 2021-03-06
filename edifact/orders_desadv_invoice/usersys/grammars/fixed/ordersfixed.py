from bots.botsconfig import *

from syntaxfixed import syntax

structure=    [
    {ID:'HEA',MIN:1,MAX:10000,LEVEL:[
        {ID:'LIN',MIN:0,MAX:10000},
        ]},
    ]
    

recorddefs = {
    'HEA':[
            ['BOTSID','C',3,'A'],
            ['SOORT', 'C', 20, 'AN'],          
            ['EANZENDER', 'C', 13, 'AN'],         
            ['EANONTVANGER', 'C', 13, 'AN'],         
            ['TEST', 'C', 1, 'AN'],         
            ['ORDERNUMMER', 'C', 17, 'AN'],         
            ['ORDERDATUM', 'C', 12, 'AN'],          
            ['INDICATIEONTVANGSTBEVESTIGING', 'C', 3, 'AN'],   
            ['SOORTORDER', 'C', 3, 'AN'],          
            ['EANAFNEMER', 'C', 13, 'AN'],         
            ['EANLEVERANCIER', 'C', 13, 'AN'],         
            ['EANAFLEVER', 'C', 13, 'AN'],         
            ['EANHAALADRES', 'C', 13, 'AN'],         
            ['EANEINDBESTEMMING', 'C', 13, 'AN'],         
            ['EANFACTUUR', 'C', 13, 'AN'],         
            ['LEVERDATUM', 'C', 12, 'AN'],          
            ['VLEVERDATUM', 'C', 12, 'AN'],          
            ['LLEVERDATUM', 'C', 12, 'AN'],          
            ['GEIMPROVISEERD', 'C', 3, 'AN'],          
            ['ACCIJNSVRIJ', 'C', 3, 'AN'],          
            ['NULORDER', 'C', 3, 'AN'],          
            ['BACKHAULING', 'C', 3, 'AN'],          
            ['SPOEDORDER', 'C', 3, 'AN'],          
            ['WINKELINSTALLATIE', 'C', 3, 'AN'],          
            ['RAAMORDERNUMMER', 'C', 17, 'AN'],         
            ['ACTIENUMMER', 'C', 17, 'AN'],         
          ],
    'LIN':[
            ['BOTSID','C',3,'A'],
            ['REGEL', 'C', 6, 'N'],         
            ['ARTIKEL', 'C', 14, 'AN'],         
            ['PROMOTIECODE', 'C', 17, 'AN'],        
            ['ARTIKELOMSCHRIJVING', 'C', 35, 'AN'],         
            ['BESTELDAANTAL', 'C', 16.3, 'N'],      
          ],
    }
     
