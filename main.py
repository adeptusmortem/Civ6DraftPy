import flet as ft
import json
import os
from assets.scripts.generatejson import GenerateNations
from math import isclose
from random import random, shuffle

class LeaderClass:
    # Атрибуты лидеров, имя, специализация, нация, можно будет добавить еще роль и тд
    def __init__(self, name, spec, nation):
        self.name = name      # имя лидера
        self.spec = spec      # специализация лидера
        self.nation = nation  # нация

class LeaderButton(ft.UserControl):

    def __init__(self, leader: LeaderClass) -> None:
        super().__init__()
        self.leader = leader
        self.text = f"""{str(leader.name)} {str(leader.spec)}, {str(leader.nation)}"""
        self.style = ft.ButtonStyle( color={ft.MaterialState.DEFAULT: ft.colors.BLACK}, 
                                    bgcolor={ft.MaterialState.DEFAULT: ft.colors.RED,"": ft.colors.GREEN_200})
        self.state = True

    def switch_leader(self, e: ft.ControlEvent) -> None:
        if self.state:
            self.style.bgcolor[""]=ft.colors.RED_200
        else:
            self.style.bgcolor[""]=ft.colors.GREEN_200
        self.state = not(self.state)
        self.update()

    def build(self):
        result_button = ft.OutlinedButton(self.text, style = self.style, on_click=self.switch_leader)
        return result_button


def main(page: ft.Page) -> None:

    #### DEBUG

    # ALL_BORDERES_VISIBLE=False
    if not(os.path.isfile("nations.json")):
        GenerateNations()
    ####

    #### Настройки окна
    page.theme_mode = ft.ThemeMode.LIGHT
    page.title = "Civ6DraftPy"
    page.window_width=1800
    page.window_height=900
    page.window_maximized=True
    page.window_full_screen=False
    page.update()

    
    ##### Импорт из json список наций
    f = open('nations.json')
    leader_data = json.load(f)
    f.close()

    ##### Создания списка лидеров
    nations = [LeaderClass(leader['name'], leader['spec'], leader['nation']) for leader in leader_data]
    NationList = nations.copy()
    NationList.sort(key=lambda k: k.name)
    AllowedNations = NationList.copy()
    RandomNations = []
    seen_leader = set()
    seen_nation = set()

    WIDTH_LEADER_ROW=page.window_width*0.9
    WIDTH_LEADER_COLUMN=WIDTH_LEADER_ROW*0.33

    HEIGHT_LEADER_ROW=page.window_height*0.9
    HEIGHT_LEADER_COLUMN=HEIGHT_LEADER_ROW*0.9

    #### Объявление функций 

    def res_but_clicked(e):
        for button in leader_buttons:
            if button.leader in AllowedNations:
                if not(button.state):
                    AllowedNations.remove(button.leader)
            else:
                if button.state:
                    AllowedNations.append(button.leader)
                    
        AllowedNations.sort(key=lambda k: k.name)

        for i in range(len(NationList)):
            try: 
                AllowedNationsText[i].value=f"""{
                    str(AllowedNations[i].name)} {str(AllowedNations[i].spec)}, {str(AllowedNations[i].nation)
                    }"""
            except Exception:
                AllowedNationsText[i].value=''
        
        page.update()

    #### Закрытие окна на Esc
    def close_window(e: ft.KeyboardEvent): 
        if e.key == 'Escape':
            page.window_close()

    page.on_keyboard_event = close_window

    #### Создание случайных наций для игроков
    def generate_nations(e):        
        RandomNations = AllowedNations.copy()
        shuffle(AllowedNations)
        for leader in AllowedNations:
            if (leader.name not in seen_leader) and (leader.nation not in seen_nation):
                # RandomNations.append(leader)
                seen_leader.add(leader.name)
                seen_nation.add(leader.nation)
            else:
                RandomNations.remove(leader)

        ResultPlayersCol.clean()

        ResultPlayersCol.controls.append(ft.Divider(thickness=3))

        try:
            RandomNations[int(slider_n_of_players.value*slider_n_for_players.value)]
            for i in range(int(slider_n_of_players.value*slider_n_for_players.value)):
                if isclose(i % slider_n_for_players.value, 0):
                    ResultPlayersCol.controls.append(ft.Text(value=f"Игрок №{int(i // slider_n_for_players.value + 1)}"))
                    ResultPlayersCol.controls.append(ft.Divider(thickness=1))

                ResultPlayersCol.controls.append(
                    ft.Text(
                        value=f"{str(RandomNations[i].name)} {str(RandomNations[i].spec)}, {str(RandomNations[i].nation)}"
                    )
                )

                if isclose((i+1) % slider_n_for_players.value, 0):
                    ResultPlayersCol.controls.append(ft.Divider(thickness=3, height=20))
        except IndexError:
            ResultPlayersCol.controls.append(ft.Text(value='Ну у вас и запросы...'))

        RandomNations = []
        seen_leader.clear()
        seen_nation.clear()
        ResultPlayersCol.update()

    ####
        

    #### Объявление элементов интерфейса

    NationsCol=ft.Column(
                spacing=5,
                width=WIDTH_LEADER_COLUMN,
                height=HEIGHT_LEADER_COLUMN,
                scroll=ft.ScrollMode.AUTO,
                )
    
    PlayerCol=ft.Column(
                spacing=5,
                width=WIDTH_LEADER_COLUMN,
                height=HEIGHT_LEADER_COLUMN,
                scroll=ft.ScrollMode.HIDDEN,
                )

    ResultPlayersCol=ft.Column(
                spacing=1,
                width=WIDTH_LEADER_COLUMN,
                height=HEIGHT_LEADER_COLUMN, 
                scroll=ft.ScrollMode.AUTO,                  
                )

    ResultNationsCol=ft.Column(
                spacing=5,
                width=WIDTH_LEADER_COLUMN,
                height=HEIGHT_LEADER_COLUMN*0.9,        
                )
    
    ResultColText=ft.Column(
                spacing=0,
                width=WIDTH_LEADER_COLUMN,
                height=ResultNationsCol.height*0.9,
                scroll=ft.ScrollMode.AUTO,             
                )
    
    ####


    #### Колонка выбора нациий

    leader_buttons = [LeaderButton(leader) for leader in NationList]
    [NationsCol.controls.append(button) for button in leader_buttons]

    ####


    #### Колонка даных об игроках

    slider_n_of_players_text = ft.Text(value='Выбор количества игроков')
    slider_n_of_players = ft.Slider(
        min=1,
        max=10,
        divisions=9,
        value=4,
        label="{value} игрок(-а/ов)",
        # on_change_end=generate_nations,
    )

    slider_n_for_players_text = ft.Text(value='Выбор количества наций на игрока')
    slider_n_for_players = ft.Slider(
        min=1,
        max=10,
        divisions=9,
        value=4,
        label="{value} нации на игрока",
        # on_change_end=generate_nations,
    )

    img_cntr = ft.Container(
        width=PlayerCol.width*0.9,
        height=250,
        image_src="/images/mish.gif",
        image_fit = ft.ImageFit.FIT_WIDTH,
        border_radius=15,
        on_click=generate_nations,
        on_hover=res_but_clicked,
    )


    PlayerCol.controls.append(slider_n_of_players_text)
    PlayerCol.controls.append(slider_n_of_players)
    PlayerCol.controls.append(slider_n_for_players_text)
    PlayerCol.controls.append(slider_n_for_players)
    PlayerCol.controls.append(img_cntr)

    ####


    #### Колонка результата

    [ResultPlayersCol.controls.append(ft.Text(value=str(leader.name))) for leader in RandomNations]

    result_button = ft.OutlinedButton('Получить список доступных лидеров', on_click=res_but_clicked)    
    ResultNationsCol.controls.append(
        ft.Container(
            content=result_button,
        )
    )


    AllowedNationsText = [ft.Text(value=f"""{
        str(leader.name)} {str(leader.spec)}, {str(leader.nation)
        }""") for leader in NationList]
    for i in range(len(NationList)):
        ResultColText.controls.append(AllowedNationsText[i])
    ResultNationsCol.controls.append(ResultColText)

    ResultTab = ft.Tabs(
        selected_index=0,
        animation_duration=100,
        height=HEIGHT_LEADER_COLUMN,
        tabs=[
            ft.Tab(
                text='Нации для игроков',
                icon=ft.icons.CHECKLIST,
                content=ResultPlayersCol,

            ),
            ft.Tab(
                text='Доступные нации',
                icon=ft.icons.LIST,
                content=ResultNationsCol,
            ),
        ],
        expand=1,
    )

    ####


    MainRow=ft.Row(
                [NationsCol, PlayerCol, ResultTab],
                height=HEIGHT_LEADER_ROW,
                width=WIDTH_LEADER_ROW
            )

    page.add(MainRow)


if __name__ == '__main__':
    ft.app(
        target=main,
        assets_dir="assets"
    )
