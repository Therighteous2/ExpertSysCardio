#importer la librairie et tous ses modules
import streamlit as st
from experta import*

class Symptome(Fact):
    pass
class MaladieExpert(KnowledgeEngine):
    def _init_(self):
        super()._init_()
        self.resultat=" "
    @Rule(Symptome(essouflement=True,fatigue=True,Arythmie=True,douleurThorax=True,evanouissement=True,fievre=True,gonflementArt=True,nausee=True,crampe=True,vomissement=True,vertige=False,sueur=False,angoisse = False,douleurArt=False, raideurMat=False,gonflementJambe=False,perteMob=False,craquement=False,souffle=False, oedeme=False,rythmeCard=False,peauPale=False))
    def Rhumatismale(self):
        self.resultat="**Veuillez administrez de la pénicilline pour éraiquer l'infection streptococcique, utilisez de l'aspirine ou autres AINS pour réduire l'inflammation et gérer des complication cardiaques en utilisant des diurétiques, bêta-bloquants ou inhibiteurs de l'ECA pour traiter l'insuffisance cardiaque**"
        st.error("**Le patient souffre de la Cardiopathie Rhumatismale**")
        
    @Rule(Symptome(essouflement=True,fatigue=False,Arythmie=False,douleurThorax=True,evanouissement=False,fievre=False,gonflementArt=False,nausee=True,crampe=False,vomissement=False,vertige=True,sueur=True,angoisse=True,faiblesse=True,douleurArt=False, raideurMat=False,gonflementJambe=False,perteMob=False,craquement=False, souffle=False, oedeme=False,rythmeCard=False,peauPale=False))
    def Ischemique(self):
        self.resultat= "1°.Utilisez des bêta-bloquants, inhibiteurs calciques, dérivés nitrés pour réduire la demande en Oxygène du coeur; 2°. Administrez de l'aspirine, clopidogrel pour prévenir la formation des caillots; 3°. Statines: pour abaisser le cholestérol LDL et stabiliser les plaques d'athérome; 4°. Utiliser les inhibiteurs de l'enzyme de conversion (IEC) pour réduire la pression artérielle et la charge cardiaque."
        st.error("**Le patient souffre de la Cardio-Ischémique**")
    @Rule(Symptome(essouflement=False,fatigue=False,Arythmie=False,douleurThorax=False,evanouissement=False,fievre=False,gonflementArt=False,nausee=False,crampe=False,vomissement=False,vertige=False,sueur=False,angoisse=False,faiblesse=False,douleurArt=True, raideurMat=True,gonflementJambe=True,perteMob=True,craquement=True, souffle=False, oedeme=False,rythmeCard=False,peauPale=False))
    def peripherique(self):
        self.resultat ="**1°. Utilisez des anti-inflammatoires non stéroïdiens(AINS) pour réduire la douleur et l'inflammation; 2°. Administrez des Corticostéroïdes par voie orale ou en injections intra-articulaires pour les pousés inflammatoire sévères. 3°. Faire de la thérapie physique et une rééducation**"
        st.error("**Le patient souffre de l'Arthropathie périphérique**")
    @Rule(Symptome(essouflement=True,fatigue=True,Arythmie=False,douleurThorax=False,evanouissement=False,fievre=False,gonflementArt=False,nausee=False,crampe=False,vomissement=False,vertige=False,sueur=False,angoisse=False,faiblesse=False,douleurArt=False, raideurMat=False,gonflementJambe=False,perteMob=False,craquement=False, souffle=True, oedeme=True,rythmeCard=True,peauPale=True))
    def Congenital(self):
        self.resultat ="**1°. Thérapie génique; 2°. Soins de soutien et réadaptation**"
        st.error("**Le patient souffre de la malformation congénitale**")

    @Rule(AS.f<<Symptome())
    def inconnu(self,f):         
        self.resultat= "**Symptômes non reconnues**"