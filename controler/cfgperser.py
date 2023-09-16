import configparser
import json


def dialogue():
    config = configparser.ConfigParser()
    config.read("data/pnj/tavernier.ini")
    texte = json.loads(config.get("DIALOGUES","pnj"))

    print(texte[0])
    choix_hero = []
    reponses_pnj = []
    for i in range(1, len(texte)):
        choix_hero.append(texte[i])

    display_possible_answer_hero(choix_hero, reponses_pnj, config)


def display_possible_answer_hero(choix_hero, reponses_pnj, config):

    index_choix = 1
    for i in choix_hero:
        texte = json.loads(config.get("DIALOGUES", i))
        print("\t", index_choix, ' - ', texte[0])
        reponses_pnj.append(texte[1])
        index_choix += 1
    choice_answer_hero(choix_hero, reponses_pnj)


def choice_answer_hero(choix_hero, reponses_pnj):

    choice_answer = int(input())
    if choice_answer <= len(choix_hero):
        reponse_pnj = reponses_pnj[choice_answer-1]
    else:
        print("Cette option nest pas disponible..")
        choice_answer_hero(choix_hero, reponses_pnj)

    display_answer_pnj(reponse_pnj)


def display_answer_pnj(reponse_pnj):

    config = configparser.ConfigParser()
    config.read("data/pnj/tavernier.ini")
    texte = json.loads(config.get("DIALOGUES", reponse_pnj))

    print(texte[0])
    choix_hero = []
    reponse_pnj = []
    for i in range(1, len(texte)):
        choix_hero.append(texte[i])

    display_possible_answer_hero(choix_hero, reponse_pnj, config)