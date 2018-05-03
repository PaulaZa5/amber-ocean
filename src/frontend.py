import amber
import personal_docks
import seas
import ships

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.switch import Switch
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen, SwapTransition
from kivy.properties import StringProperty,NumericProperty
from kivy.uix.scrollview import ScrollView
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, Rectangle
#from kivy.uix.spinner import Spinner
import datetime
from kivy.clock import *
from kivy.uix.widget import Widget
from kivy.uix.popup import *
from amber import database, generate_personal_docks

Builder.load_file("frontend.kv")

user_id_for_login = ""

returned_id = ""



###################  Login
class LoginScreen(BoxLayout):
    # define the constructor and access the class method and attributes
    def __init__(self, users_manager, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        # **kwargs allow you to pass a variable number of arguments to a function.
        self.users_manager = users_manager
        # BaxLayout Orientation is vertical
        self.orientation = 'vertical'


class Login(Widget):
    def submit_login(self):
        global user_id_for_login
        # save textinput to a variables
        logname = self.login_name.text
        logpass = self.login_password.text
        # test only
        # if logname == 'admin' and logpass == 'admin':
        # users_manager.current = 'home'
        flag=0
        for value in amber.generate_personal_docks():
            key = value
            value = database[value]
            if value.master_email == logname:
                if value.check_password(logpass):
                    user_id_for_login = key
                    home = Screen(name='home')
                    home.add_widget(Page(users_manager=users_manager, user_id=user_id_for_login))
                    users_manager.add_widget(home)
                    users_manager.current = 'home'
                    self.login_name.text=""
                    self.login_password.text=""
                    flag=1

        if flag==0:
            l = Label(text='Wrong Username or password', color=(1, 0, 0, 1), markup=True)
            self.ids.end.add_widget(l)
            Clock.schedule_once(lambda dt: self.ids.end.remove_widget(l), 1)
            print("error")



###################  Registeration
class Registeration(Widget):
    date = StringProperty(None)
 #   def __init__(self, **kwargs):
 #       super(Registeration, self).__init__(**kwargs)
 #       self.flag_male=False
 #       self.flag_female = False
 #   def ismale(self):
 #       gender = "male"
 #       self.flag_male = not self.flag_male
 #       print (gender + " flag2: " + str(self.flag_male))
#
#
 #   def isfemale(self):
 #       gender = "female"
 #       self.flag_female = not self.flag_female
 #       print (gender+" flag2: "+str(self.flag_female))

    def registerAccount(self):
        global returned_id
        flag=0
        # check input data
        for c in self.name.text:
            if not (c.isalpha() or c.isspace()):
                l = Label(text='Please enter a valid name', color=(1, 0, 0, 1), markup=True)
                self.ids.error.add_widget(l)
                Clock.schedule_once(lambda dt: self.ids.error.remove_widget(l), 1)
                flag=1
        if self.name.text == "" :
            l = Label(text='Please enter a valid name', color=(1, 0, 0, 1), markup=True)
            self.ids.error.add_widget(l)
            Clock.schedule_once(lambda dt: self.ids.error.remove_widget(l), 1)
            flag=1
        elif self.gender.text =="Gender" :
           l = Label(text='Please enter your gender', color=(1, 0, 0, 1), markup=True)
           self.ids.error.add_widget(l)
           Clock.schedule_once(lambda dt: self.ids.error.remove_widget(l), 1)
           flag=1
        elif not self.year.text.isdigit() or not self.month.text.isdigit() or not self.day.text.isdigit():
            l = Label(text='Please enter a valid Birthday', color=(1, 0, 0, 1), markup=True)
            self.ids.error.add_widget(l)
            Clock.schedule_once(lambda dt: self.ids.error.remove_widget(l), 1)
            flag=1
        elif self.year.text.isdigit() and self.month.text.isdigit() and self.day.text.isdigit():
            if int(self.day.text) > 31 or int(self.day.text) < 0:
                l = Label(text='Please enter a valid Birth Day', color=(1, 0, 0, 1), markup=True)
                self.ids.error.add_widget(l)
                Clock.schedule_once(lambda dt: self.ids.error.remove_widget(l), 1)
                flag=1
            elif int(self.month.text) > 12 or int(self.day.text) < 0:
                l = Label(text='Please enter a valid Birth Month', color=(1, 0, 0, 1), markup=True)
                self.ids.error.add_widget(l)
                Clock.schedule_once(lambda dt: self.ids.error.remove_widget(l), 1)
                flag=1
            elif int(self.year.text) > 2018 or int(self.year.text) < 1900:
                l = Label(text='Please enter a valid Birth Year', color=(1, 0, 0, 1), markup=True)
                self.ids.error.add_widget(l)
                Clock.schedule_once(lambda dt: self.ids.error.remove_widget(l), 1)
                flag=1
            elif not '@' in self.email.text or self.email.text == "":
                l = Label(text='Please enter a valid email', color=(1, 0, 0, 1), markup=True)
                self.ids.error.add_widget(l)
                Clock.schedule_once(lambda dt: self.ids.error.remove_widget(l), 1)
                flag=1
            elif self.password.text == "":
                l = Label(text='Please enter your Password', color=(1, 0, 0, 1), markup=True)
                self.ids.error.add_widget(l)
                Clock.schedule_once(lambda dt: self.ids.error.remove_widget(l), 1)
                flag=1
            elif self.phone.text == "":
                l = Label(text='Please enter your Phone', color=(1, 0, 0, 1), markup=True)
                self.ids.error.add_widget(l)
                Clock.schedule_once(lambda dt: self.ids.error.remove_widget(l), 1)
                flag=1
            else:
                docks=generate_personal_docks()
                for id in docks:
                    if self.email.text == database[id].master_email:
                        l = Label(text='Please, Choose another email', color=(1, 0, 0, 1), markup=True)
                        self.ids.error.add_widget(l)
                        Clock.schedule_once(lambda dt: self.ids.error.remove_widget(l), 1)
                        flag=1
        if flag==0 :
                date = datetime.datetime(int(self.year.text), int(self.month.text), int(self.day.text))

                returned_id = personal_docks.PersonalDock.RegisterAccount(self.name.text, self.gender.text, date,
                                                                          self.password.text,self.email.text,self.phone.text)
                home = Screen(name='home2')
                home.add_widget(Page(users_manager=users_manager, user_id=returned_id))
                users_manager.add_widget(home)
                users_manager.current = 'home2'
                self.name.text=""
                self.gender.text ="Gender"
                self.day.text = ""
                self.month.text = ""
                self.year.text=""
                self.password.text=""
                self.email.text=""
                self.phone.text=""
    # check valid date

    # else:
    # popup = Popup(title='Test popup',
    # content=Label(text='Please enter a valid Birthday'),
    # size_hint=(None, None), size=self.size)
    # popup.open()
    # print(self.password.text+" "+self.email.text+" "+self.phone.text)
    #  if self.name.text == "" or self.gender==""or date==""or self.password.text=="" or self.email.text == "" or self.phone.text== "" :
    #         # label = Label(text='Please Write Your Name',color=(0,0,0,1))
    # self.ids.error.add_widget(label)
    # else:
    #  returned_id = personal_docks.PersonalDock.RegisterAccount(self.name.text,self.gender,date,self.password.text,
    #                         self.email.text,self.phone.text)
    #   print(returned_id)


class RegisterationScreen(Screen):
    pass


###################################
class Page(BoxLayout):

    class ContentManager(ScreenManager):
        class BackButton(Button):

            def __init__(self, screen_manager, **kwargs):
                super(Page.ContentManager.BackButton, self).__init__(**kwargs)
                self.screen_manager = screen_manager

            def on_release(self):
                try:
                    prev_screen = self.screen_manager.previous()
                    current_screen = self.screen_manager.current_screen
                    self.screen_manager.transition.direction = 'right'
                    self.screen_manager.current = prev_screen
                    self.screen_manager.remove_widget(current_screen)
                except:
                    pass

        class GroupButton(Button):

            def __init__(self, user_id, group_id, screen_manager, **kwargs):
                super(Page.ContentManager.GroupButton, self).__init__(**kwargs)
                self.user_id = user_id
                self.group_id = group_id
                self.text = amber.database[group_id].name
                self.screen_manager = screen_manager

            def on_release(self):
                new_group_screen = Screen(name=str(self.screen_manager.screens_added_counter))
                new_group_screen.add_widget(Page.GroupPage(user_id=self.user_id, group_id=self.group_id,
                                                           screen_manager=self.screen_manager))
                self.screen_manager.add_widget(new_group_screen)
                self.screen_manager.transition.direction = 'left'
                self.screen_manager.current = new_group_screen.name

        class GroupCreationButton(Button):

            def __init__(self, user_id, screen_manager, **kwargs):
                super(Page.ContentManager.GroupCreationButton, self).__init__(**kwargs)
                self.user_id = user_id
                self.text = 'Create\na new sea'
                self.screen_manager = screen_manager

            def on_release(self):
                new_create_group_screen = Screen(name=str(self.screen_manager.screens_added_counter))
                new_create_group_screen.add_widget(Page.GroupCreationPage(user_id=self.user_id,
                                                                          screen_manager=self.screen_manager))
                self.screen_manager.add_widget(new_create_group_screen)
                self.screen_manager.transition.direction = 'left'
                self.screen_manager.current = new_create_group_screen.name

        class HomeButton(Button):

            def __init__(self, user_id, screen_manager, **kwargs):
                super(Page.ContentManager.HomeButton, self).__init__(**kwargs)
                self.user_id = user_id
                self.screen_manager = screen_manager

            def on_release(self):
                new_home_screen = Screen(name=str(self.screen_manager.screens_added_counter))
                new_home_screen.add_widget(Page.HomePage(user_id=self.user_id, screen_manager=self.screen_manager))
                self.screen_manager.add_widget(new_home_screen)
                self.screen_manager.transition.direction = 'left'
                self.screen_manager.current = new_home_screen.name

        class ProfileButton(Button):

            def __init__(self, user_id, destination_id, screen_manager, **kwargs):
                super(Page.ContentManager.ProfileButton, self).__init__(**kwargs)
                self.user_id = user_id
                self.text = amber.database[destination_id].name
                self.destination_id = destination_id
                self.screen_manager = screen_manager

            def on_release(self):
                new_profile_screen = Screen(name=str(self.screen_manager.screens_added_counter))
                new_profile_screen.add_widget(Page.ProfilePage(user_id=self.user_id, destination_id=self.destination_id,
                                                               screen_manager=self.screen_manager))
                self.screen_manager.add_widget(new_profile_screen)
                self.screen_manager.transition.direction = 'left'
                self.screen_manager.current = new_profile_screen.name

        def __init__(self, user_id, **kwargs):
            super(Page.ContentManager, self).__init__(**kwargs)
            self.screens_added_counter = 0
            self.user_id = user_id

        def add_widget(self, screen):
            screen.name = str(self.screens_added_counter)
            super(Page.ContentManager, self).add_widget(screen)
            self.screens_added_counter = self.screens_added_counter + 1

        def back_button(self, **kwargs):
            return Page.ContentManager.BackButton(screen_manager=self, **kwargs)

        def group_button(self, **kwargs):
            return Page.ContentManager.GroupButton(user_id=self.user_id, screen_manager=self, **kwargs)

        def group_creation_button(self, **kwargs):
            return Page.ContentManager.GroupCreationButton(user_id=self.user_id, screen_manager=self, **kwargs)

        def home_button(self, **kwargs):
            return Page.ContentManager.HomeButton(user_id=self.user_id, screen_manager=self, **kwargs)

        def post_input(self, **kwargs):
            return Page.PostInput(user_id=self.user_id, screen_manager=self, **kwargs)

        def post(self, **kwargs):
            return Page.Post(user_id=self.user_id, screen_manager=self, **kwargs)

        def profile_button(self, **kwargs):
            return Page.ContentManager.ProfileButton(user_id=self.user_id, screen_manager=self, **kwargs)

    class GroupCreationPage(BoxLayout):

        class CreateGroupButton(Button):

            def __init__(self, user_id, screen_manager, name_tb, description_tb, **kwargs):
                super(Page.GroupCreationPage.CreateGroupButton, self).__init__(**kwargs)
                self.text = 'Create'
                self.user_id = user_id
                self.screen_manager = screen_manager
                self.name_tb = name_tb
                self.description_tb = description_tb

            def on_release(self):
                new_sea_id = seas.Sea.RegisterSea(creator=self.user_id, name=self.name_tb.text,
                                                  description=self.description_tb.text)
                amber.database[self.user_id].join_sea(new_sea_id)
                self.screen_manager.back_button().on_release()
                self.screen_manager.group_button(group_id=new_sea_id).on_release()

        def __init__(self, user_id, screen_manager, **kwargs):
            super(Page.GroupCreationPage, self).__init__(**kwargs)
            self.orientation = 'vertical'
            self.padding = 10
            self.spacing = 5

            name_box = BoxLayout(orientation='horizontal', padding=10, spacing=5)
            name_box.add_widget(Label(text='Sea Name: '))
            name_tb = TextInput(text='', size_hint_x=2, multiline=False)
            name_box.add_widget(name_tb)
            self.add_widget(name_box)

            description_box = BoxLayout(orientation='horizontal', padding=10, spacing=5, size_hint_y=4)
            description_box.add_widget(Label(text='Sea Description: '))
            description_tb = TextInput(text='', size_hint_x=2)
            description_box.add_widget(description_tb)
            self.add_widget(description_box)

            self.add_widget(Page.GroupCreationPage.CreateGroupButton(user_id=user_id, screen_manager=screen_manager,
                                                                     name_tb=name_tb, description_tb=description_tb))

    class GroupPage(BoxLayout):

        class GroupSettings(BoxLayout):

            def save_settings(self, instance):
                if self.group.is_administrator(self.user_id):
                    self.group.name = self.name_tb.text
                    self.group.active = self.active.active
                    if len(self.group.name) == 0:
                        self.group.name = 'No Name'
                    self.group.description = self.description_tb.text
                    for member_id, member_data in self.members_status.items():
                        admin, editor, member = member_data
                        if (not admin.active) and (not editor.active) and (not member.active):
                            if self.group.is_administrator(member_id):
                                self.group.remove_administrator(member_id)
                            elif self.group.is_editor(member_id):
                                self.group.remove_editor(member_id)
                            self.group.remove_member(member_id)
                            amber.database[member_id].leave_sea(self.group.id)
                        elif (admin.active and editor.active) or admin.active:
                            if self.group.is_editor(member_id):
                                self.group.remove_editor(member_id)
                            if not self.group.is_administrator(member_id):
                                self.group.add_administrator(member_id)
                        elif editor.active:
                            if not self.group.is_editor(member_id):
                                self.group.add_editor(member_id)
                            if self.group.is_administrator(member_id):
                                self.group.remove_administrator(member_id)
                        else:
                            if self.group.is_editor(member_id):
                                self.group.remove_editor(member_id)
                            if self.group.is_administrator(member_id):
                                self.group.remove_administrator(member_id)
                    self.group.visibility_privacy = ''.join(self.visibility_btn.text.split()).lower()
                    self.group.sailing_privacy = ''.join(self.sailing_btn.text.split()).lower()
                    Page.ContentManager.BackButton(screen_manager=self.screen_manager).on_release()

            def __init__(self, user_id, group, screen_manager, **kwargs):
                super(Page.GroupPage.GroupSettings, self).__init__(**kwargs)
                self.orientation = 'vertical'
                self.padding = 10
                self.spacing = 5
                self.user_id = user_id
                self.group = group
                self.screen_manager = screen_manager

                name_and_active = BoxLayout(orientation='horizontal', padding=10, spacing=5, size_hint_y=1)
                name_and_active.add_widget(Label(text='Group Name: ', size_hint_x=1))
                self.name_tb = TextInput(text=self.group.name, size_hint_x=2, multiline=False)
                name_and_active.add_widget(self.name_tb)
                name_and_active.add_widget(Label(text='Active Group: ', size_hint_x=1))
                self.active = CheckBox(active=True)
                name_and_active.add_widget(self.active)
                self.add_widget(name_and_active)

                description = BoxLayout(orientation='horizontal', padding=10, spacing=5, size_hint_y=2)
                description.add_widget(Label(text='Description: ', size_hint_x=1))
                self.description_tb = TextInput(text=self.group.description, size_hint_x=4)
                description.add_widget(self.description_tb)
                self.add_widget(description)

                members = BoxLayout(orientation='horizontal', padding=10, spacing=5, size_hint_y=0.5)
                members.add_widget(Label(text='Members'))
                members.add_widget(Label(text='Is Administrator'))
                members.add_widget(Label(text='Is Editor'))
                members.add_widget(Label(text='Is Member'))
                self.add_widget(members)
                scrollable_members = ScrollView(do_scroll_x=False, size_hint_y=5)
                all_members = BoxLayout(size_hint_y=None, height=len(self.group.members) * 35,
                                        orientation='vertical', padding=10, spacing=5)
                self.members_status = {}
                for member in self.group.members:
                    member_data = BoxLayout(size_hint_y=None, height=30, orientation='horizontal', padding=10, spacing=5)
                    self.members_status[member] = (CheckBox(), CheckBox(), CheckBox(active=True))
                    if member in self.group.administrators:
                        self.members_status[member][0].active = True
                    if member in self.group.editors:
                        self.members_status[member][1].active = True
                    member_data.add_widget(screen_manager.profile_button(destination_id=member))
                    member_data.add_widget(self.members_status[member][0])
                    member_data.add_widget(self.members_status[member][1])
                    member_data.add_widget(self.members_status[member][2])
                    all_members.add_widget(member_data)
                scrollable_members.add_widget(all_members)
                self.add_widget(scrollable_members)

                visibility = BoxLayout(orientation='horizontal', padding=10, spacing=5)
                visibility.add_widget(Label(text='Sea Visibility: ', size_hint_x=1))
                visibility_dp = DropDown()
                self.visibility_btn = Button(text='', size_hint_x=4)
                self.visibility_btn.bind(on_release=visibility_dp.open)
                visibility_dp.bind(on_select=lambda instance, x: setattr(self.visibility_btn, 'text', x))
                if self.group.visibility_privacy == "onlymembers":
                    self.visibility_btn.text = "Only members"
                else:
                    self.visibility_btn.text = "Everyone"
                btn = Button(text='Only members', size_hint_y=None, height=44)
                btn.bind(on_release=lambda btn: visibility_dp.select(btn.text))
                visibility_dp.add_widget(btn)
                btn = Button(text='Everyone', size_hint_y=None, height=44)
                btn.bind(on_release=lambda btn: visibility_dp.select(btn.text))
                visibility_dp.add_widget(btn)
                visibility.add_widget(self.visibility_btn)
                self.add_widget(visibility)

                sailing = BoxLayout(orientation='horizontal', padding=10, spacing=5)
                sailing.add_widget(Label(text='Sea Sailing Privacy: ', size_hint_x=1))
                sailing_dp = DropDown()
                self.sailing_btn = Button(text='', size_hint_x=4)
                self.sailing_btn.bind(on_release=sailing_dp.open)
                sailing_dp.bind(on_select=lambda instance, x: setattr(self.sailing_btn, 'text', x))
                if self.group.sailing_privacy == "onlyadministrators":
                    self.sailing_btn.text = "Only administrators"
                elif self.group.sailing_privacy == "onlyeditors":
                    self.sailing_btn.text = "Only editors"
                else:
                    self.sailing_btn.text = "Everyone"
                btn = Button(text='Only administrators', size_hint_y=None, height=44)
                btn.bind(on_release=lambda btn: sailing_dp.select(btn.text))
                sailing_dp.add_widget(btn)
                btn = Button(text='Only editors', size_hint_y=None, height=44)
                btn.bind(on_release=lambda btn: sailing_dp.select(btn.text))
                sailing_dp.add_widget(btn)
                btn = Button(text='Everyone', size_hint_y=None, height=44)
                btn.bind(on_release=lambda btn: sailing_dp.select(btn.text))
                sailing_dp.add_widget(btn)
                sailing.add_widget(self.sailing_btn)
                self.add_widget(sailing)

                btn = Button(text='Save Settings')
                btn.bind(on_release=self.save_settings)
                self.add_widget(btn)

        class SettingsButton(Button):

            def __init__(self, user_id, group, screen_manager, **kwargs):
                super(Page.GroupPage.SettingsButton, self).__init__(**kwargs)
                self.text = 'Settings'
                self.user_id = user_id
                self.group = group
                self.screen_manager = screen_manager

            def on_release(self):
                if self.group.is_administrator(self.user_id):
                    settings_page = Screen(name='group_settings')
                    settings_page.add_widget(Page.GroupPage.GroupSettings(user_id=self.user_id, group=self.group,
                                                                          screen_manager=self.screen_manager))
                    self.screen_manager.add_widget(settings_page)
                    self.screen_manager.current = settings_page.name

        class JoinOrLeaveButton(Button):

            def __init__(self, user_id, group, **kwargs):
                super(Page.GroupPage.JoinOrLeaveButton, self).__init__(**kwargs)
                self.user = amber.database[user_id]
                self.group = group
                if group.is_member(user_id):
                    self.text = 'Leave'
                else:
                    self.text = 'Join'

            def on_release(self):
                if self.group.is_member(self.user.id):
                    if self.group.is_administrator(self.user.id):
                        self.group.remove_administrator(self.user.id)
                    elif self.group.is_editor(self.user.id):
                        self.group.remove_editor(self.user.id)
                    self.group.remove_member(self.user.id)
                    self.user.leave_sea(self.group.id)
                else:
                    self.group.add_member(self.user.id)
                    self.user.join_sea(self.group.id)

        class TopBar(BoxLayout):

            def __init__(self, user_id, group, screen_manager, **kwargs):
                super(Page.GroupPage.TopBar, self).__init__(**kwargs)
                self.orientation = 'horizontal'
                self.padding = 10
                self.spacing = 5
                self.add_widget(Label(text=group.name, size_hint_x=1))
                if group.is_administrator(user_id):
                    self.add_widget(Page.GroupPage.SettingsButton(user_id=user_id, group=group, screen_manager=screen_manager,
                                                                  size_hint_x=3))
                else:
                    self.add_widget(Label(size_hint_x=3))
                self.add_widget(Page.GroupPage.JoinOrLeaveButton(user_id=user_id, group=group))

        class GroupUsers(ScrollView):

            def __init__(self, group, screen_manager, **kwargs):
                super(Page.GroupPage.GroupUsers, self).__init__(**kwargs)
                self.do_scroll_x = False
                self.size_hint_x = 0
                self.users = BoxLayout(size_hint_y=None, orientation='vertical', padding=10, spacing=5)
                self.users.bind(minimum_height=self.users.setter('height'))
                for member in group.members:
                    self.size_hint_x = 1
                    if group.is_administrator(member):
                        self.users.add_widget(screen_manager.profile_button(destination_id=member,
                                                                            background_color=(1, 0, 0, 1), size_hint_y=None))
                    elif group.is_editor(member):
                        self.users.add_widget(screen_manager.profile_button(destination_id=member,
                                                                            background_color=(1, 1, 0, 1), size_hint_y=None))
                    else:
                        self.users.add_widget(screen_manager.profile_button(destination_id=member, size_hint_y=None))
                self.add_widget(self.users)

        class SuggestedUsers(ScrollView):

            def __init__(self, user, screen_manager, **kwargs):
                super(Page.GroupPage.SuggestedUsers, self).__init__(**kwargs)
                self.do_scroll_x = False
                self.size_hint_x = 0
                self.users = BoxLayout(size_hint_y=None, orientation='vertical', padding=10, spacing=5)
                self.users.bind(minimum_height=self.users.setter('height'))
                for user in user.docks_you_may_know():
                    self.size_hint_x = 1
                    self.users.add_widget(screen_manager.profile_button(destination_id=user, size_hint_y=None))
                self.add_widget(self.users)

        class SuggestedGroups(ScrollView):

            def __init__(self, user, screen_manager, **kwargs):
                super(Page.GroupPage.SuggestedGroups, self).__init__(**kwargs)
                self.do_scroll_x = False
                self.size_hint_x = 0
                self.groups = BoxLayout(size_hint_y=None, orientation='vertical', padding=10, spacing=5)
                self.groups.bind(minimum_height=self.groups.setter('height'))
                for group in user.seas_you_might_join():
                    self.size_hint_x = 1
                    self.groups.add_widget(screen_manager.group_button(group_id=group, size_hint_y=None))
                self.add_widget(self.groups)

        class GroupPosts(ScrollView):

            def __init__(self, user_id, group, screen_manager, **kwargs):
                super(Page.GroupPage.GroupPosts, self).__init__(**kwargs)
                self.do_scroll_x = False
                self.screen_manager = screen_manager
                self.group = group
                self.posts = BoxLayout(size_hint_y=None, orientation='vertical', padding=10, spacing=5)
                self.posts.bind(minimum_height=self.posts.setter('height'))
                if self.group.sailing_privacy == seas.SeaSailingPrivacy.Everyone or self.group.is_administrator(user_id) or (self.group.sailing_privacy == seas.SeaSailingPrivacy.Only_editors and self.group.is_editor(user_id)):
                    self.posts.add_widget(screen_manager.post_input(where_is_it_created=group.id))
                for post, date in group.sailed_ships:
                    self.posts.add_widget(self.screen_manager.post(post_id=post, destination_id=self.group.id))
                self.add_widget(self.posts)

        def __init__(self, user_id, group_id, screen_manager, **kwargs):
            super(Page.GroupPage, self).__init__(**kwargs)
            self.user = amber.database[user_id]
            self.group = amber.database[group_id]
            if (self.group.visibility_privacy == seas.SeaVisibilityPrivacy.Only_Members and user_id in self.group.members) or self.group.visibility_privacy == seas.SeaVisibilityPrivacy.Everyone:
                self.screen_manager = screen_manager
                self.orientation = 'vertical'
                self.padding = 10
                self.spacing = 5
                self.add_widget(Page.GroupPage.TopBar(user_id=user_id, group=self.group, screen_manager=screen_manager))
                grp_page = BoxLayout(orientation='horizontal', padding=10, spacing=5, size_hint_y=7)
                grp_page.add_widget(Page.GroupPage.GroupPosts(user_id=user_id, group=self.group, screen_manager=screen_manager,
                                                              size_hint_x=7))
                grp_page.add_widget(Page.GroupPage.GroupUsers(group=self.group, screen_manager=screen_manager))
                grp_page.add_widget(Page.GroupPage.SuggestedUsers(user=self.user, screen_manager=screen_manager))
                grp_page.add_widget(Page.GroupPage.SuggestedGroups(user=self.user, screen_manager=screen_manager))
                self.add_widget(grp_page)
            else:
                self.size_hint = (0, 0)

    class HomePage(BoxLayout):
        def __init__(self, user_id, screen_manager, **kwargs):
            super(Page.HomePage, self).__init__(**kwargs)
            self.user_id = user_id
            self.screen_manager = screen_manager
            user = amber.database[self.user_id]
            self.orientation = "horizontal"
            ships = Page.HomePage.Ships(user=amber.database[self.user_id], screen_manager=screen_manager)
            self.add_widget(ships)
            groups = Page.HomePage.Groups(user=amber.database[self.user_id], screen_manager=screen_manager)
            self.add_widget(groups)
            friends = Page.HomePage.Friends(user=amber.database[self.user_id], screen_manager=screen_manager)
            self.add_widget(friends)
            followees = Page.HomePage.Followees(user=amber.database[self.user_id], screen_manager=screen_manager)
            self.add_widget(followees)
            suggested_friends = Page.HomePage.Suggested_Friends(user=amber.database[self.user_id], screen_manager=screen_manager)
            self.add_widget(suggested_friends)
            suggested_groups = Page.HomePage.Suggested_Groups(user=amber.database[self.user_id], screen_manager=screen_manager)
            self.add_widget(suggested_groups)

        class Groups(ScrollView):
            def __init__(self, user, screen_manager, **kwargs):
                super(Page.HomePage.Groups, self).__init__(**kwargs)
                self.do_scroll_x = False
                self.size_hint_x = 0
                self.groups = BoxLayout(size_hint_y=None, orientation='vertical', padding=10, spacing=5)
                self.groups.bind(minimum_height=self.groups.setter('height'))
                for num, group in enumerate(user.seas):
                    if num == 0:
                        self.groups.add_widget(Label(text='Groups', size_hint_y=None))
                        self.size_hint_x = 1
                    self.groups.add_widget(screen_manager.group_button(group_id=group, size_hint_y=None))
                self.add_widget(self.groups)

        class Friends(ScrollView):
            def __init__(self, user, screen_manager, **kwargs):
                super(Page.HomePage.Friends, self).__init__(**kwargs)
                self.do_scroll_x = False
                self.size_hint_x = 0
                self.friends = BoxLayout(size_hint_y=None, orientation='vertical', padding=10, spacing=5)
                self.friends.bind(minimum_height=self.friends.setter('height'))
                for num, frnd in enumerate(user.friends):
                    if num == 0:
                        self.friends.add_widget(Label(text='Friends', size_hint_y=None))
                        self.size_hint_x = 1
                    self.friends.add_widget(screen_manager.profile_button(destination_id=frnd, size_hint_y=None))
                self.add_widget(self.friends)

        class Followees(ScrollView):
            def __init__(self, user, screen_manager, **kwargs):
                super(Page.HomePage.Followees, self).__init__(**kwargs)
                self.do_scroll_x = False
                self.size_hint_x = 0
                self.followees = BoxLayout(size_hint_y=None, orientation='vertical', padding=10, spacing=5)
                self.followees.bind(minimum_height=self.followees.setter('height'))
                for num, follow in enumerate(user.followees):
                    if num == 0:
                        self.followees.add_widget(Label(text='Followees', size_hint_y=None))
                        self.size_hint_x = 1
                    self.followees.add_widget(screen_manager.profile_button(destination_id=follow, size_hint_y=None))
                self.add_widget(self.followees)

        class Ships(ScrollView):
            def __init__(self, user, screen_manager, **kwargs):
                super(Page.HomePage.Ships, self).__init__(**kwargs)
                self.do_scroll_x = False
                self.size_hint_x = 4
                self.ships = BoxLayout(size_hint_y=None, orientation='vertical', padding=10, spacing=5)
                self.ships.bind(minimum_height=self.ships.setter('height'))
                self.ships.add_widget(screen_manager.post_input(where_is_it_created=user.id))
                for num, ship in enumerate(user.newsfeed_ships()):
                    self.ships.add_widget(screen_manager.post(post_id=ship, destination_id=user.id, size_hint_y=None))
                self.add_widget(self.ships)

        class Suggested_Friends(ScrollView):

            def __init__(self, user, screen_manager, **kwargs):
                super(Page.HomePage.Suggested_Friends, self).__init__(**kwargs)
                self.do_scroll_x = False
                self.size_hint_x = 0
                self.suggested_friends = BoxLayout(size_hint_y=None, orientation='vertical', padding=10, spacing=5)
                self.suggested_friends.bind(minimum_height=self.suggested_friends.setter('height'))
                new = user.docks_you_may_know()
                for num, sugg_friend in enumerate(new):
                    if num == 0:
                        self.suggested_friends.add_widget(Label(text='Suggested Friends', size_hint_y=None))
                        self.size_hint_x = 1
                    self.suggested_friends.add_widget(screen_manager.profile_button(destination_id=sugg_friend[0], size_hint_y=None))
                self.add_widget(self.suggested_friends)

        class Suggested_Groups(ScrollView):

            def __init__(self, user, screen_manager, **kwargs):
                super(Page.HomePage.Suggested_Groups, self).__init__(**kwargs)
                self.do_scroll_x = False
                self.size_hint_x = 0
                self.suggested_groups = BoxLayout(size_hint_y=None, orientation='vertical', padding=10, spacing=5)
                self.suggested_groups.bind(minimum_height=self.suggested_groups.setter('height'))
                new = user.seas_you_might_join()
                for num, group in enumerate(new):
                    if num == 0:
                        self.suggested_groups.add_widget(Label(text='Suggested Groups', size_hint_y=None))
                        self.size_hint_x = 1
                    self.suggested_groups.add_widget(screen_manager.group_button(group_id=group[0], size_hint_y=None))
                self.add_widget(self.suggested_groups)
            """suggested_groups = Page.GroupPage.SuggestedGroups(user=amber.database[self.user_id], screen_manager=screen_manager)
            self.add_widget(suggested_groups)"""
            """
            ##### Groups
            group_number = len(list(user.seas))
            group_label = Label(text='Groups' ,size_hint_y=40 ,size_hint_x=1 )
            l = Label(text='', size_hint_y=100, size_hint_x=1)
            e = Label(text='', size_hint_y=100, size_hint_x=1)
            self.ids.groups_l.add_widget(group_label)
            #self.ids.groups_l.add_widget(l)

            for i in range(group_number):
                name = amber.database[user.seas[i]].name

                button = Button(text=name
                                , background_color=(0, 0, 1, 0.6)
                                , size_hint_y=None
                                , height=30)
                self.ids.groups_l.add_widget(button)


            ##### Friends
            friend_number = len(list(user.friends))
            Friends_label = Label(text='Freinds', size_hint_y=10 ,size_hint_x=1)
            self.ids.friends_l.add_widget(Friends_label)
            for i in range(friend_number):
                name = amber.database[user.friends[i]].name
                button = Button(text="Friend " + name
                                , background_color=(0, 1, 0, 0.6)
                                , height=30)
                self.ids.friends.add_widget(button)

            ##### Followees
            Followee_number = len(list(user.followees))
            Followess_label = Label(text='Followees')
            self.ids.followees_l.add_widget(Followess_label)
            for i in range(friend_number):
                name = amber.database[user.followees[i]].name
                button = Button(text="Followee " + name, background_color=(1, 0, 0, 0.6))
                self.ids.followees.add_widget(button)

            ##### Ships
            Ships_number = len(list(user.newsfeed_ships()))
            Ships_label = Label(text='Ships')
            self.ids.ships_l.add_widget(Ships_label)
            for i in range(Ships_number):
                name = amber.database[user.sailed_ships[i][0]]
                button = Button(text="Ship " + name
                                , background_color=(0, 1, 1, 0.6)
                                , height=30)
                self.ids.ships.add_widget(button)
            ##### Suugested Friends
            sugg_friend_number = len(list(user.docks_you_may_know()))
            sugg_friend_label = Label(text='Suggested Friends')
            self.ids.sugg_friend_l.add_widget(sugg_friend_label)
            for i in range(sugg_friend_number):
                name = amber.database[user.docks_you_may_know[i][0]]
                button = Button(text= name
                                , background_color=(1, 1, 0, 0.6)
                                , height=30)
                self.ids.sugg_friend.add_widget(button)
            ##### Suugested Groups
            sugg_groups_number = len(list(user.seas_you_might_join()))
            sugg_group_label = Label(text='Suggested Groups')
            self.ids.sugg_group_l.add_widget(sugg_group_label)
            for i in range(sugg_groups_number):
                name = amber.database[user.seas_you_might_join[i][0]]
                button = Button(text="Group " + name
                                , background_color=(1, 0, 1, 0.6)
                                , height=30)
                self.ids.sugg_group.add_widget(button)
                """

    class PostInput(BoxLayout):

        def __init__(self, user_id, where_is_it_created, screen_manager, **kwargs):
            super(Page.PostInput, self).__init__(**kwargs)
            self.user_id = user_id
            self.where_is_it_created = where_is_it_created
            self.orientation = 'vertical'
            self.size_hint_y = None
            self.height = 500

            Privacy = BoxLayout(orientation='vertical', padding=10)
            Box = BoxLayout(orientation='vertical', size_hint=(1, 5), padding=10)
            Share = BoxLayout(orientation='vertical', padding=10)
            self.add_widget(Privacy)
            self.add_widget(Box)
            self.add_widget(Share)

            def post(instance):
                if box.text != "" and box.text != "What's on your mind?":
                    post_privacy = ships.ShipPrivacy.Everyone
                    if spin_privacy.text == "Everyone":
                        post_privacy = ships.ShipPrivacy.Everyone
                    elif spin_privacy.text == "Friends and Followers":
                        post_privacy = ships.ShipPrivacy.Only_friends_and_followers
                    elif spin_privacy.text == "Only Followers":
                        post_privacy = ships.ShipPrivacy.Only_followers
                    elif spin_privacy.text == "Only Friends":
                        post_privacy = ships.ShipPrivacy.Only_friends
                    elif spin_privacy.text == "Only Me":
                        post_privacy = ships.ShipPrivacy.Only_creator
                    new_ship = ships.Ship.RegisterShip(creator_id=user_id, where_is_it_created_id=where_is_it_created,
                                                       content_type=ships.ContentType.Text, txt_content=box.text,
                                                       privacy=post_privacy)
                    amber.database[where_is_it_created].sailed_ships.append((new_ship, amber.database[new_ship].creation_date))
                    new_post = screen_manager.post(post_id=new_ship, destination_id=where_is_it_created)
                    self.height = self.height + new_post.height
                    self.add_widget(new_post)
                    box.text = ""

            spin_privacy = Spinner(
                text="Everyone",
                size_hint=(0.3, 1),
                values=("Everyone",
                        "Friends and Followers",
                        "Only Followers",
                        "Only Friends",
                        "Only Me")
            )
            Privacy.add_widget(spin_privacy)

            def show_selected_value(spin_privacy, values):
                return values

            spin_privacy.bind(text=show_selected_value)

            share = Button(
                text="Share",
                size_hint=(0.1, 1),
                disabled=True,
                on_release=post
            )
            Share.add_widget(share)

            def remove(instance, touch):
                if instance.text == "What's on your mind?":
                    instance.text = ""

            def write(instance, touch):
                if instance.text == "":
                    share.disabled = True
                    instance.text = "What's on your mind?"
                else:
                    share.disabled = False

            box = TextInput(
                text="What's on your mind?",
                multiline=True,
                size_hint=(1, 5),
                on_touch_down=remove,
                on_touch_up=write
            )
            Box.add_widget(box)

    class Post(BoxLayout):

        class Comment(BoxLayout):

            def __init__(self, user_id, reply_id, screen_manager, **kwargs):
                super(Page.Post.Comment, self).__init__(**kwargs)
                self.user_id = user_id
                self.reply = amber.database[reply_id]
                self.screen_manager = screen_manager
                self.orientation = 'horizontal'
                self.padding = 5
                self.spacing = 5
                self.size_hint_y = None
                self.height = 40
                self.add_widget(screen_manager.profile_button(destination_id=self.reply.creator_id))
                self.add_widget(Label(text=self.reply.txt_content, size_hint_x=4))

                self.prev_reaction = 'React'
                def update_reactions(instance, touch):

                    if 'Like' in instance.text and not self.prev_reaction == 'Like':
                        self.reply.change_reaction(user_id, ships.Reactions.Like)
                        instance.values[0] = 'Like - ' + str(self.reply.count_of_reaction(ships.Reactions.Like))
                        instance.text = instance.values[0]
                        self.prev_reaction = 'Like'
                    elif 'Haha' in instance.text and not self.prev_reaction == 'Haha':
                        self.reply.change_reaction(user_id, ships.Reactions.Haha)
                        instance.values[1] = 'Haha - ' + str(self.reply.count_of_reaction(ships.Reactions.Haha))
                        instance.text = instance.values[1]
                        self.prev_reaction = 'Haha'
                    elif 'Love' in instance.text and not self.prev_reaction == 'Love':
                        self.reply.change_reaction(user_id, ships.Reactions.Love)
                        instance.values[2] = 'Love - ' + str(self.reply.count_of_reaction(ships.Reactions.Love))
                        instance.text = instance.values[2]
                        self.prev_reaction = 'Love'
                    elif 'Dislike' in instance.text and not self.prev_reaction == 'Dislike':
                        self.reply.change_reaction(user_id, ships.Reactions.Dislike)
                        instance.values[3] = 'Dislike - ' + str(self.reply.count_of_reaction(ships.Reactions.Dislike))
                        instance.text = instance.values[3]
                        self.prev_reaction = 'Dislike'
                    elif 'Angry' in instance.text and not self.prev_reaction == 'Angry':
                        self.reply.change_reaction(user_id, ships.Reactions.Angry)
                        instance.values[4] = 'Angry - ' + str(self.reply.count_of_reaction(ships.Reactions.Angry))
                        instance.text = instance.values[4]
                        self.prev_reaction = 'Angry'
                    elif self.prev_reaction is not 'React':
                        self.reply.remove_reaction(user_id)
                        instance.text = 'React'
                        self.prev_reaction = 'React'

                    instance.values[0] = 'Like - ' + str(self.reply.count_of_reaction(ships.Reactions.Like))
                    instance.values[1] = 'Haha - ' + str(self.reply.count_of_reaction(ships.Reactions.Haha))
                    instance.values[2] = 'Love - ' + str(self.reply.count_of_reaction(ships.Reactions.Love))
                    instance.values[3] = 'Dislike - ' + str(self.reply.count_of_reaction(ships.Reactions.Dislike))
                    instance.values[4] = 'Angry - ' + str(self.reply.count_of_reaction(ships.Reactions.Angry))

                reactions = Spinner(text="React", values=(
                    'Like - ' + str(amber.database[reply_id].count_of_reaction(ships.Reactions.Like)),
                    'Haha - ' +  str(amber.database[reply_id].count_of_reaction(ships.Reactions.Haha)),
                    'Love - ' + str(amber.database[reply_id].count_of_reaction(ships.Reactions.Love)),
                    'Dislike - ' + str(amber.database[reply_id].count_of_reaction(ships.Reactions.Dislike)),
                    'Angry - ' + str(amber.database[reply_id].count_of_reaction(ships.Reactions.Angry))
                ))
                reactions.bind(is_open=update_reactions)
                if user_id in self.reply.reactions:
                    reactions.text = self.reply.reactions[user_id][:1].upper() + self.reply.reactions[user_id][1:]
                self.add_widget(reactions)

        def __init__(self, user_id, post_id, destination_id, screen_manager, **kwargs):
            super(Page.Post, self).__init__(**kwargs)
            self.user_id = user_id
            self.ship_id = post_id
            ship_id = post_id
            self.destination_id = destination_id
            self.screen_manager = screen_manager
            is_able_to_see = False
            # print(self.ship_id, self.user_id, amber.database[ship_id].creator_id)
            if amber.is_personal_dock(amber.database[amber.database[ship_id].where_is_it_created_id]):
                # Everyone
                if amber.database[ship_id].privacy == ships.ShipPrivacy.Everyone:
                    is_able_to_see = True
                # Friends and Followers
                elif (user_id in amber.database[amber.database[ship_id].creator_id].friends \
                      or user_id in amber.database[amber.database[ship_id].creator_id].followers) \
                        and amber.database[ship_id].privacy == ships.ShipPrivacy.Only_friends_and_followers:
                    is_able_to_see = True
                # Friends
                elif user_id in amber.database[amber.database[ship_id].creator_id].friends \
                        and amber.database[ship_id].privacy == ships.ShipPrivacy.Only_friends:
                    is_able_to_see = True
                # Followers
                elif user_id in amber.database[amber.database[ship_id].creator_id].followers \
                        and amber.database[ship_id].privacy == ships.ShipPrivacy.Only_followers:
                    is_able_to_see = True
                # Only me
                elif user_id == amber.database[ship_id].creator_id:
                    is_able_to_see = True
            else:
                if amber.database[amber.database[
                    ship_id].where_is_it_created_id].visibility_privacy == seas.SeaVisibilityPrivacy.Everyone:
                    is_able_to_see = True
                elif user_id in amber.database[amber.database[ship_id].where_is_it_created_id].members:
                    is_able_to_see = True

            # Label for editing number of likes
            number_likes = Label(
                text="0 likes",
                size_hint=(1, 1)
            )
            number_haha = Label(
                text="",
                size_hint=(1, 1)
            )
            number_love = Label(
                text="",
                size_hint=(1, 1)
            )
            number_dislike = Label(
                text="",
                size_hint=(1, 1)
            )

            number_angry = Label(
                text="",
                size_hint=(1, 1)
            )

            number_comments = Label(
                text=str(len(amber.database[ship_id].child_ships)) + " Comment",
                # color=(0, 0, 0, 1),
                size_hint=(1, 1),
                pos_hint={'center_x': 0.9, 'center_y': 1}
            )


            def comment_clicked(cmt_btn):
                txt_splitted = number_comments.text.split()
                number_comments.text = str(int(txt_splitted[0]) + 1) + ' ' + txt_splitted[1]


            if is_able_to_see:
                self.orientation = 'vertical'
                self.spacing = 10
                self.padding = 20
                self.size_hint = (1, None)
                self.height = 600



                Header = BoxLayout(orientation='vertical', spacing=0, padding=20, size_hint=(1, 1))
                Delete = BoxLayout(orientation='horizontal', size_hint=(1, 1), spacing=0, padding=20)
                Center = BoxLayout(orientation='vertical', spacing=10, padding=20, size_hint=(1, 2))
                Footer = BoxLayout(orientation='horizontal', spacing=10, padding=20, size_hint=(1, 1))
                Likes = BoxLayout(orientation='horizontal', spacing=60, padding=0, size_hint=(1, 1))
                Comments = BoxLayout(orientation='vertical', spacing=10, padding=10, size_hint=(1, 2))

                comments_box = BoxLayout(orientation='vertical', size_hint_y=None)
                for comment_id in amber.database[ship_id].generate_comments():
                    comments_box.add_widget(Page.Post.Comment(reply_id=comment_id, user_id=user_id, screen_manager=screen_manager))

                self.add_widget(Delete)
                self.add_widget(Header)
                self.add_widget(Center)
                Footer.add_widget(Likes)
                Footer.add_widget(Comments)
                self.add_widget(Footer)

                # Button for user name
                name = screen_manager.profile_button(destination_id=amber.database[self.ship_id].creator_id,
                              size_hint=(1, 1),
                              bold=True
                              )
                Delete.add_widget(name)
                Delete.add_widget(Label(size_hint_x=3))

                def delete_ship(instance):
                    try:
                        if amber.is_sea(amber.database[amber.database[ship_id].where_is_it_created_id]):
                            amber.database[amber.database[ship_id].where_is_it_created_id].sink_ship_from_this_sea(ship_id)
                        elif amber.is_personal_dock(amber.database[amber.database[ship_id].where_is_it_created_id]):
                            amber.database[amber.database[ship_id].where_is_it_created_id].sink_ship_from_this_dock(ship_id)
                        # elif amber.is_ship(amber.database[amber.database[ship_id].where_is_it_created_id]):
                        #     amber.database[amber.database[ship_id].where_is_it_created_id].child_ships.remove(ship_id)
                        del amber.database[ship_id]
                        self.clear_widgets()
                        self.parent.height -= self.height
                        self.size = (0, 0)
                    except:
                        pass

                delete = Button(text="Remove ship", size_hint=(1, 1),
                                on_release=delete_ship)
                Delete.add_widget(delete)


                def like_clicked(like_btn, touch):
                    cont = True
                    if user_id in amber.database[ship_id].reactions:
                        if like_btn.text.lower() == amber.database[ship_id].reactions[user_id]:
                            amber.database[ship_id].remove_reaction(user_id)
                            cont = False

                    if cont:
                        if (like_btn.text is "Like"):
                            amber.database[ship_id].change_reaction(user_id, ships.Reactions.Like)
                        elif (like_btn.text is "Haha"):
                            amber.database[ship_id].change_reaction(user_id, ships.Reactions.Haha)
                        elif (like_btn.text is "Love"):
                            amber.database[ship_id].change_reaction(user_id, ships.Reactions.Love)
                        elif (like_btn.text is "Dislike"):
                            amber.database[ship_id].change_reaction(user_id, ships.Reactions.Dislike)
                        elif (like_btn.text is "Angry"):
                            amber.database[ship_id].change_reaction(user_id, ships.Reactions.Angry)

                    number_likes.text = str(amber.database[ship_id].count_of_reaction(ships.Reactions.Like)) + ' like'
                    number_haha.text = str(amber.database[ship_id].count_of_reaction(ships.Reactions.Haha)) + ' Haha'
                    number_love.text = str(amber.database[ship_id].count_of_reaction(ships.Reactions.Love)) + ' Love'
                    number_dislike.text = str(amber.database[ship_id].count_of_reaction(ships.Reactions.Dislike)) + ' Dislike'
                    number_angry.text = str(amber.database[ship_id].count_of_reaction(ships.Reactions.Angry)) + ' angry'

                # label for date
                current_date = Label(
                    text=str(amber.database[ship_id].creation_date.date()),
                    size_hint=(0, 1)
                )
                Header.add_widget(current_date)

                # label for time
                current_time = Label(
                    text=str(amber.database[ship_id].creation_date.time()),
                    size_hint=(0, 1)
                )
                Header.add_widget(current_time)

                # Button for Like
                def trigger_fn(instance):
                    like.is_open = True

                like = Spinner(
                    text="Reactions",
                    values=("Like", "Haha", "Love", "Dislike", "Angry"),
                    size_hint=(0, 1)
                )
                like.bind(text=like_clicked)
                Likes.add_widget(like)


                number_likes.text = str(amber.database[ship_id].count_of_reaction(ships.Reactions.Like)) + ' Like'
                number_haha.text = str(amber.database[ship_id].count_of_reaction(ships.Reactions.Haha)) + ' Haha'
                number_love.text = str(amber.database[ship_id].count_of_reaction(ships.Reactions.Love)) + ' Love'
                number_dislike.text = str(amber.database[ship_id].count_of_reaction(ships.Reactions.Dislike)) + ' Dislike'
                number_angry.text = str(amber.database[ship_id].count_of_reaction(ships.Reactions.Angry)) + ' angry'
                Likes.add_widget(number_likes)
                Likes.add_widget(number_haha)
                Likes.add_widget(number_love)
                Likes.add_widget(number_dislike)
                Likes.add_widget(number_angry)

                vert_scr = ScrollView(size_hint=(1, None), height=120)
                comments_box.bind(minimum_height=comments_box.setter('height'))
                vert_scr.add_widget(comments_box)
                self.add_widget(vert_scr)

                def add_comment(comment_btn):

                    def on_text(instance, touch):
                        if (not new_post.text == ""):
                            post.disabled = False

                    box_l = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
                    new_post = TextInput(size_hint_y=None, height=40, on_touch_up=on_text)
                    # def increase_likes(instance, touch):
                    #     if "Like" in instance.text:
                    #         instance.values[0] = "Like: " + str(int(instance.values[0].split()[1]) + 1)
                    #     elif "Love" in instance.text:
                    #         instance.values[2] = "Love: " + str(int(instance.values[0].split()[1]) + 1)
                    #     elif "Haha" in instance.text:
                    #         instance.values[1] = "Haha: " + str(int(instance.values[0].split()[1]) + 1)
                    #     elif "Dislike" in instance.text:
                    #         instance.values[3] = "Dislike: " + str(int(instance.values[0].split()[1]) + 1)
                    #     elif "None" in instance.text:
                    #         try:
                    #             amber.database[reply_id].remove_reaction(user_id)
                    #         except:
                    #             pass
                    #     elif "Angry" in instance.text:
                    #         instance.values[4] = "Angry: " + str(int(instance.values[0].split()[1]) + 1)
                    #
                    # def like_cmt_clicked(like_btn, touch):
                    #     if "Like" in like_btn.text:
                    #         amber.database[post_id].change_reaction(user_id, ships.Reactions.Like)
                    #     elif ( "Haha" in like_btn.text):
                    #         amber.database[post_id].change_reaction(user_id, ships.Reactions.Haha)
                    #     elif ("Love" in like_btn.text):
                    #         amber.database[post_id].change_reaction(user_id, ships.Reactions.Love)
                    #     elif ("Dislike" in like_btn.text):
                    #         amber.database[post_id].change_reaction(user_id, ships.Reactions.Dislike)
                    #     elif ("Angry" in like_btn.text):
                    #         amber.database[post_id].change_reaction(user_id, ships.Reactions.Angry)
                    #     elif ("None" in like_btn.text):
                    #         try:
                    #             amber.database[post_id].remove_reaction(user_id)
                    #         except:
                    #             pass
                    #     number_likes.text = str(
                    #         amber.database[post_id].count_of_reaction(ships.Reactions.Like)) + ' Like'
                    #     number_haha.text = str(
                    #         amber.database[post_id].count_of_reaction(ships.Reactions.Haha)) + ' Haha'
                    #     number_love.text = str(
                    #         amber.database[post_id].count_of_reaction(ships.Reactions.Love)) + ' Love'
                    #     number_dislike.text = str(
                    #         amber.database[post_id].count_of_reaction(ships.Reactions.Dislike)) + ' Dislike'
                    #     number_angry.text = str(
                    #         amber.database[post_id].count_of_reaction(ships.Reactions.Angry)) + ' Angry'

                    def create_comment(post_btn):

                        comment_btn.disabled = False
                        written_text = new_post.text
                        reply_id = amber.database[ship_id].add_reply(replyer_id=user_id, reply_type=ships.ContentType.Text, reply_text=new_post.text)
                        # new_label = Label(text=written_text, size_hint_y=None, height=40)
                        # name_btn = screen_manager.profile_button(destination_id=user_id,
                        #                   size_hint_x=0.2, size_hint_y=None, height=30, bold=True)
                        # like_cmt_btn = Spinner(text="Reactions",
                        #                        values=(
                        #                        'Like: ' + str(amber.database[reply_id].count_of_reaction(ships.Reactions.Like)),
                        #                        "Haha: " +  str(amber.database[reply_id].count_of_reaction(ships.Reactions.Haha)),
                        #                        "Love: " +str(amber.database[reply_id].count_of_reaction(ships.Reactions.Love)),
                        #                        "Dislike: "+str(amber.database[reply_id].count_of_reaction(ships.Reactions.Dislike)),
                        #                        "Angry: "+str(amber.database[reply_id].count_of_reaction(ships.Reactions.Angry)),
                        #                        "None"),
                        #                        size_hint_y=None, height=30, size_hint_x=0.2)
                        #
                        # """
                        # reply_btn = Button(text="Reply",size_hint_y=None, height=30,
                        #                      size_hint_x=0.2 )
                        # """
                        # like_cmt_btn.bind(text=increase_likes)

                        box_l.remove_widget(new_post)
                        box_l.remove_widget(post_btn)
                        comments_box.add_widget(Page.Post.Comment(reply_id=reply_id, user_id=user_id, screen_manager=screen_manager))

                        # new_commen_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
                        # new_commen_box.add_widget(name_btn)
                        # new_commen_box.add_widget(new_label)
                        # new_commen_box.add_widget(like_cmt_btn)
                        # new_commen_box.add_widget(reply_btn)
                        # comments_box.add_widget(new_commen_box)
                        self.remove_widget(box_l)

                    comment_btn.disabled = True

                    post = Button(text="Post", size_hint_x=0.2, size_hint_y=None, height=40,
                                  on_release=create_comment, disabled=True, on_press=comment_clicked)

                    box_l.add_widget(new_post)
                    box_l.add_widget(post)
                    self.add_widget(box_l)

                # Button for Comment
                comment = Button(
                    text="Comment",
                    size_hint=(0, 1),
                    disabled=False,
                    pos_hint={'center_x': 0.9, 'center_y': 1},
                    on_release=add_comment
                )
                Comments.add_widget(comment)

                # Label for editing number of comments

                Comments.add_widget(number_comments)

                # After writing post
                text_input = Button(
                    text=amber.database[ship_id].txt_content,
                    size_hint=(1, 2),
                    background_color = (5,1,3,1),
                    disabled=True
                )
                Center.add_widget(text_input)
            else:
                self.add_widget(Label(size_hint=(0, 0), size=(0, 0)))

    class ProfilePage(BoxLayout):

        '''
        Not Done yet

        '''

        class EditprofileButton(Button):
            def __init__(self, user_id, destination_id, screen_manager, **kwargs):
                super(Page.ProfilePage.EditprofileButton, self).__init__(**kwargs)
                self.user_id = user_id
                self.destination_id = destination_id
                self.screen_manager = screen_manager
                self.text='Edit Profile'
            def on_release(self):
                Edit_profile_screen = Screen(name='edit')
                Edit_profile_screen.add_widget(Page.EditProfilePage( user_id=self.user_id, destination_id=self.destination_id, screen_manager=self.screen_manager))
                self.screen_manager.add_widget(Edit_profile_screen)
                self.screen_manager.current = Edit_profile_screen.name

        class AddFriendButton(Button):
            def __init__(self, user_id, destination_id, screen_manager,FriendAndFollowBox, **kwargs):
                super(Page.ProfilePage.AddFriendButton, self).__init__(**kwargs)
                self.user_id = user_id
                self.destination_id = destination_id
                self.screen_manager = screen_manager
                self.FriendAndFollowBox=FriendAndFollowBox
                self.text='Add friend'

            def on_release(self):
                personal_docks.PersonalDock.add_friend(amber.database[self.user_id],self.destination_id)
                self.FriendAndFollowBox.clear_widgets()
                self.FriendAndFollowBox.add_widget(Page.ProfilePage.RemoveFriend_button(self,self.FriendAndFollowBox))
                if self.destination_id in amber.database[self.user_id].followees:
                    self.FriendAndFollowBox.add_widget(Page.ProfilePageFollowFriend_button(self,self.FriendAndFollowBox))
                else:
                    self.FriendAndFollowBox.add_widget(Page.ProfilePage.UnFollowFriend_button(self,self.FriendAndFollowBox))
                # .add_widget(self.FriendAndFollowBox)


        class RemoveFriendButton(Button):
            def __init__(self, user_id, destination_id, screen_manager,FriendAndFollowBox, **kwargs):
                super(Page.ProfilePage.RemoveFriendButton, self).__init__(**kwargs)
                self.user_id = user_id
                self.destination_id = destination_id
                self.screen_manager = screen_manager
                self.FriendAndFollowBox = FriendAndFollowBox
                self.text='Unfriend'
            def on_release(self):
                personal_docks.PersonalDock.remove_friend(amber.database[self.user_id],self.destination_id)
                self.FriendAndFollowBox.clear_widgets()
                self.FriendAndFollowBox.add_widget(Page.ProfilePage.AddFriend_button(self, self.FriendAndFollowBox))
                if self.destination_id in amber.database[self.user_id].followees:
                    self.FriendAndFollowBox.add_widget(
                        Page.ProfilePageFollowFriend_button(self, self.FriendAndFollowBox))
                else:
                    self.FriendAndFollowBox.add_widget(
                        Page.ProfilePage.UnFollowFriend_button(self, self.FriendAndFollowBox))

        class FollowFriendButton(Button):
            def __init__(self, user_id, destination_id, screen_manager,FriendAndFollowBox, **kwargs):
                super(Page.ProfilePage.FollowFriendButton, self).__init__(**kwargs)
                self.user_id = user_id
                self.destination_id = destination_id
                self.screen_manager = screen_manager
                self.FriendAndFollowBox = FriendAndFollowBox
                self.text='Follow'
            def on_release(self):
                personal_docks.PersonalDock.add_followee(amber.database[self.user_id],self.destination_id)
                personal_docks.PersonalDock.add_follower(self.destination_id,amber.database[self.user_id])
                self.FriendAndFollowBox.clear_widgets()
                if self.destination_id in amber.database[self.user_id].friends:
                    self.FriendAndFollowBox.add_widget(self.RemoveFriend_button(self.FriendAndFollowBox))
                else:
                    self.FriendAndFollowBox.add_widget(self.AddFriend_button(self.FriendAndFollowBox))
                self.FriendAndFollowBox.add_widget(self.UnFollowFriend_button(self.FriendAndFollowBox))
        class UnFollowFriendButton(Button):
            def __init__(self, user_id, destination_id, screen_manager,FriendAndFollowBox, **kwargs):
                super(Page.ProfilePage.UnFollowFriendButton, self).__init__(**kwargs)
                self.user_id = user_id
                self.destination_id = destination_id
                self.screen_manager = screen_manager
                self.FriendAndFollowBox = FriendAndFollowBox
                self.text='UnFollow'
            def on_release(self):
                personal_docks.PersonalDock.remove_followee(amber.database[self.user_id],self.destination_id)
                personal_docks.PersonalDock.remove_follower(self.destination_id,amber.database[self.user_id])
                self.FriendAndFollowBox.clear_widgets()
                if self.destination_id in amber.database[self.user_id].friends:
                    self.FriendAndFollowBox.add_widget(self.RemoveFriend_button(self.FriendAndFollowBox))
                else:
                    self.FriendAndFollowBox.add_widget(self.AddFriend_button(self.FriendAndFollowBox))
                self.FriendAndFollowBox.add_widget(self.FollowFriend_button(self.FriendAndFollowBox))
        class FriendsButton(Button):
            def __init__(self, user_id, destination_id, screen_manager, **kwargs):
                super(Page.ProfilePage.FriendsButton, self).__init__(**kwargs)
                self.user_id = user_id
                self.destination_id = destination_id
                self.screen_manager = screen_manager
                self.text='Friends'
            def on_release(self):
                Friends_screen = Screen(name='Friends')
                Friends_screen.add_widget(Page.FriendsPage( user_id=self.user_id, destination_id=self.destination_id, screen_manager=self.screen_manager))
                self.screen_manager.add_widget(Friends_screen)
                self.screen_manager.current = Friends_screen.name
        class FollowersButton(Button):
            def __init__(self, user_id, destination_id, screen_manager, **kwargs):
                super(Page.ProfilePage.FollowersButton, self).__init__(**kwargs)
                self.user_id = user_id
                self.destination_id = destination_id
                self.screen_manager = screen_manager
                self.text='Followers'

            def on_release(self):
                Followers_screen = Screen(name='Followers')
                Followers_screen.add_widget(
                    Page.FollowersPage(user_id=self.user_id, destination_id=self.destination_id,
                                         screen_manager=self.screen_manager))
                self.screen_manager.add_widget(Followers_screen)
                self.screen_manager.current = Followers_screen.name
        class FolloweesButton(Button):
            def __init__(self, user_id, destination_id, screen_manager, **kwargs):
                super(Page.ProfilePage.FolloweesButton, self).__init__(**kwargs)
                self.user_id = user_id
                self.destination_id = destination_id
                self.screen_manager = screen_manager
                self.text='Followees'
            def on_release(self):
                Followees_screen = Screen(name='Followees')
                Followees_screen.add_widget(
                    Page.FolloweesPage(user_id=self.user_id, destination_id=self.destination_id,
                                         screen_manager=self.screen_manager))
                self.screen_manager.add_widget(Followees_screen)
                self.screen_manager.current = Followees_screen.name

        def __init__(self, user_id, destination_id, screen_manager, **kwargs):
            super(Page.ProfilePage, self).__init__(**kwargs)
            self.user_id = user_id
            self.destination_id = destination_id
            self.screen_manager = screen_manager
            self.orientation='vertical'
            self.add_widget(Label(text='Profile',size_hint_y =.05))
            #EditButton = Button(text='Edit Profile',on_release=self.editProfilePopup().open)

            headerData = BoxLayout( orientation='vertical', padding=10, spacing=5)
            headerData.add_widget(Label(text='Gender:'+amber.database[user_id].gender, font_size=14))
            headerData.add_widget(Label(text='E-mail:'+str(amber.database[user_id].master_email), font_size=14))
            headerData.add_widget(Label(text='Phone Number:'+str(amber.database[user_id].master_phone_number), font_size=14))
            Profileheader = BoxLayout(orientation='horizontal',size_hint_y=0.2, padding=10, spacing=5)
            Profileheader.add_widget(Label(text=amber.database[user_id].name,font_size=24))
            Profileheader.add_widget(headerData)
            self.FriendAndFollowBox = BoxLayout(orientation='horizontal', padding=5, spacing=5)
            if self.user_id==self.destination_id:
                Profileheader.add_widget(self.editprofile_button())
            else :
                if self.destination_id in amber.database[self.user_id].friends:
                    self.FriendAndFollowBox.add_widget(self.RemoveFriend_button(self.FriendAndFollowBox))
                else:
                    self.FriendAndFollowBox.add_widget(self.AddFriend_button(self.FriendAndFollowBox))
                if self.destination_id in amber.database[self.user_id].followees:
                    self.FriendAndFollowBox.add_widget(self.UnFollowFriend_button(self.FriendAndFollowBox))
                else:
                    self.FriendAndFollowBox.add_widget(self.FollowFriend_button(self.FriendAndFollowBox))
                Profileheader.add_widget(self.FriendAndFollowBox)

            self.add_widget(Profileheader)
            Profileshipsview = ScrollView()
            Profileships = BoxLayout( orientation='vertical', padding=10, spacing=5)
            # Profileships.add_widget(Page.Post(user_id, screen_manager, **kwargs))
            # Profileships.add_widget(Page.Post(user_id, screen_manager, **kwargs))
            # Profileships.add_widget(Page.Post(user_id, screen_manager, **kwargs))
            # Profileships.add_widget(Page.Post(user_id, screen_manager, **kwargs))
            # Profileships.add_widget(Page.Post(user_id, screen_manager, **kwargs))
            # Profileships.add_widget(Page.Post(user_id, screen_manager, **kwargs))
            # Profileships.add_widget(Label(text='Ship 1'))
            # Profileships.add_widget(Button(text='Ship 2',hieght=50))
            # Profileships.add_widget(Button(text='Ship 3'))
            # Profileships.add_widget(Button(text='Ship 4'))
            Profileshipsview.add_widget(Profileships)
            PersonalDatacol = BoxLayout( orientation='vertical',size_hint_x=.3 ,padding=10, spacing=5)
            PersonalDatacol.add_widget(Label(text='Gender: ' + amber.database[user_id].gender, size_hint_y=0.1,font_size=14))
            PersonalDatacol.add_widget(Label(text='E-mail: ' + str(amber.database[user_id].master_email),size_hint_y=0.1, font_size=14))
            PersonalDatacol.add_widget(Label(text='Phone Number: ' + str(amber.database[user_id].master_phone_number),size_hint_y=0.1, font_size=14))
            PersonalDatacol.add_widget(Label(text='birthday: ' + str(amber.database[user_id].birthday),size_hint_y=0.1, font_size=14))
            PersonalDatacol.add_widget(Label(text='', font_size=14))
            PersonalDatacol.add_widget(self.Friends_button())
            PersonalDatacol.add_widget(self.Followers_button())
            PersonalDatacol.add_widget(self.Followees_button())

            Profilecontents = BoxLayout( orientation='horizontal', padding=10, spacing=5)
            Profilecontents.add_widget(PersonalDatacol)
            Profilecontents.add_widget(Profileshipsview)
            self.add_widget(Profilecontents)

        def editprofile_button(self, **kwargs):
            return Page.ProfilePage.EditprofileButton(user_id=self.user_id,destination_id=self.destination_id, screen_manager=self.screen_manager, **kwargs)
        def AddFriend_button(self,FriendAndFollowBox, **kwargs):
            return Page.ProfilePage.AddFriendButton(user_id=self.user_id,destination_id=self.destination_id, screen_manager=self.screen_manager,FriendAndFollowBox=FriendAndFollowBox, **kwargs)
        def RemoveFriend_button(self,FriendAndFollowBox, **kwargs):
            return Page.ProfilePage.RemoveFriendButton(user_id=self.user_id,destination_id=self.destination_id, screen_manager=self.screen_manager,FriendAndFollowBox=FriendAndFollowBox, **kwargs)
        def FollowFriend_button(self,FriendAndFollowBox, **kwargs):
            return Page.ProfilePage.FollowFriendButton(user_id=self.user_id,destination_id=self.destination_id, screen_manager=self.screen_manager,FriendAndFollowBox=FriendAndFollowBox, **kwargs)
        def UnFollowFriend_button(self,FriendAndFollowBox, **kwargs):
            return Page.ProfilePage.UnFollowFriendButton(user_id=self.user_id,destination_id=self.destination_id, screen_manager=self.screen_manager,FriendAndFollowBox=FriendAndFollowBox, **kwargs)

        def Friends_button(self, **kwargs):
            return Page.ProfilePage.FriendsButton(user_id=self.user_id,destination_id=self.destination_id, screen_manager=self.screen_manager, **kwargs)
        def Followers_button(self, **kwargs):
            return Page.ProfilePage.FollowersButton(user_id=self.user_id,destination_id=self.destination_id, screen_manager=self.screen_manager, **kwargs)
        def Followees_button(self, **kwargs):
            return Page.ProfilePage.FolloweesButton(user_id=self.user_id,destination_id=self.destination_id, screen_manager=self.screen_manager, **kwargs)


    class EditProfilePage(BoxLayout):
        class EditAboutButton(Button):
            def __init__(self, user_id, destination_id, screen_manager, **kwargs):
                super(Page.EditProfilePage.EditAboutButton, self).__init__(**kwargs)
                self.user_id = user_id
                self.destination_id = destination_id
                self.screen_manager = screen_manager
                self.text='Edit About and BasicInfo'
            def on_release(self):
                Edit_About_screen = Screen(name='About')
                Edit_About_screen.add_widget(Page.EditAboutPage( user_id=self.user_id, destination_id=self.destination_id, screen_manager=self.screen_manager))
                self.screen_manager.add_widget(Edit_About_screen)
                self.screen_manager.current = Edit_About_screen.name
        class EditEducationAndPlacesButton(Button):
            def __init__(self, user_id, destination_id, screen_manager, **kwargs):
                super(Page.EditProfilePage.EditEducationAndPlacesButton, self).__init__(**kwargs)
                self.user_id = user_id
                self.destination_id = destination_id
                self.screen_manager = screen_manager
                self.text='Edit Education & Living Places'

            def on_release(self):
                Edit_Education_Places_screen = Screen(name='EduAndPlaces')
                Edit_Education_Places_screen.add_widget(Page.EditEduPage( user_id=self.user_id, destination_id=self.destination_id, screen_manager=self.screen_manager))
                self.screen_manager.add_widget(Edit_Education_Places_screen)
                self.screen_manager.current = Edit_Education_Places_screen.name
        class EditContactButton(Button):
            def __init__(self, user_id, destination_id, screen_manager, **kwargs):
                super(Page.EditProfilePage.EditContactButton, self).__init__(**kwargs)
                self.user_id = user_id
                self.destination_id = destination_id
                self.screen_manager = screen_manager
                self.text='Edit Contact Information'

            def on_release(self):
                Edit_Contact_screen = Screen(name='contactinfo')
                Edit_Contact_screen.add_widget(Page.EditContactPage( user_id=self.user_id, destination_id=self.destination_id, screen_manager=self.screen_manager))
                self.screen_manager.add_widget(Edit_Contact_screen)
                self.screen_manager.current = Edit_Contact_screen.name
        class EditRelationshipsButton(Button):
            def __init__(self, user_id, destination_id, screen_manager, **kwargs):
                super(Page.EditProfilePage.EditRelationshipsButton, self).__init__(**kwargs)
                self.user_id = user_id
                self.destination_id = destination_id
                self.screen_manager = screen_manager
                self.text = 'Edit Relationships and Family members'

            def on_release(self):
                Edit_Relashionships_screen = Screen(name='Relashionships')
                Edit_Relashionships_screen.add_widget(
                    Page.EditRelationsPage(user_id=self.user_id, destination_id=self.destination_id,
                                       screen_manager=self.screen_manager))
                self.screen_manager.add_widget(Edit_Relashionships_screen)
                self.screen_manager.current = Edit_Relashionships_screen.name


        def __init__(self, user_id, destination_id, screen_manager, **kwargs):
            super(Page.EditProfilePage, self).__init__(**kwargs)
            self.user_id = user_id
            self.destination_id = destination_id
            self.screen_manager = screen_manager
            self.orientation = 'vertical'
            self.add_widget(Label(text='Edit Profile',size_hint_y =.05))
            self.edit_buttons = GridLayout(cols=2,padding=30,spacing=10)
            self.edit_buttons.add_widget(self.EditAbout_button())
            self.edit_buttons.add_widget(self.EditEducationAndPlaces_button())
            self.edit_buttons.add_widget(self.EditContact_button())
            self.edit_buttons.add_widget(self.EditRelationships_button())

            self.add_widget(self.edit_buttons)
            '''
            self.datascrollview = ScrollView(size_hint=(1, 0.5))
            ###master phone
            self.profileData.add_widget(
                Label(text='Phone Number(Master):', size_hint_y=None, size_hint_x=None, width=150, height=40))
            self.masterphoneinput = TextInput(text=str(amber.database[user_id].master_phone_number),
                                           size_hint_y=None,
                                           height=40)
            self.profileData.add_widget(self.masterphoneinput)
            ###other phone numbers

            self.profileData.add_widget(
                Label(text='Phone Number', size_hint_y=None, size_hint_x=None, width=150, height=40))
            self.masterphoneinput = TextInput(text=str(amber.database[user_id].master_phone_number),
                                              size_hint_y=None,
                                              height=40)
            self.profileData.add_widget(self.masterphoneinput)
            self.datascrollview.add_widget(self.profileData)
            self.add_widget(self.datascrollview)

            self.add_widget(self.Save_button())
            #self.add_widget(self.Save_button())
            '''
        def EditAbout_button(self, **kwargs):
            return Page.EditProfilePage.EditAboutButton(user_id=self.user_id,destination_id=self.destination_id, screen_manager=self.screen_manager, **kwargs)
        def EditEducationAndPlaces_button(self, **kwargs):
            return Page.EditProfilePage.EditEducationAndPlacesButton(user_id=self.user_id,destination_id=self.destination_id, screen_manager=self.screen_manager, **kwargs)
        def EditContact_button(self, **kwargs):
            return Page.EditProfilePage.EditContactButton(user_id=self.user_id,destination_id=self.destination_id, screen_manager=self.screen_manager, **kwargs)
        def EditRelationships_button(self, **kwargs):
            return Page.EditProfilePage.EditRelationshipsButton(user_id=self.user_id,destination_id=self.destination_id, screen_manager=self.screen_manager, **kwargs)

    class EditAboutPage(BoxLayout):
        '''
            THIS PAGE CAN EDIT:
                Activation      :done
                Name            :done
                Date of birth   :done
                gender          :using spinner
                password        :check & validation
                special_fields  :X
        '''
        class SaveButton(Button):
            def __init__(self, user_id, destination_id, screen_manager,deactivateInput,nameinput,
                         genderinput,dateofbirth_year,dateofbirth_Month,dateofbirth_Day,
                         oldpass,newpass,confirmnewpass, **kwargs):
                super(Page.EditAboutPage.SaveButton, self).__init__(**kwargs)
                self.user_id = user_id
                self.destination_id = destination_id
                self.screen_manager = screen_manager
                self.size_hint_y = None
                self.deactivateInput=deactivateInput
                self.nameinput = nameinput
                self.genderinput=genderinput
                self.dateofbirth_year = dateofbirth_year
                self.dateofbirth_Month=dateofbirth_Month
                self.dateofbirth_Day = dateofbirth_Day
                self.oldpass=oldpass
                self.newpass=newpass
                self.confirmnewpass=confirmnewpass
                self.height=50
                self.text = 'Save changes'
            def on_release(self):
                if self.deactivateInput.active==True:
                    personal_docks.PersonalDock.deactivate_account(amber.database[self.user_id])
                # else:
                #     personal_docks.PersonalDock.activate_account(amber.database[self.user_id])
                print(amber.database[self.user_id].active)
                personal_docks.PersonalDock.change_name(amber.database[self.user_id],self.nameinput.text)
                personal_docks.PersonalDock.change_gender(amber.database[self.user_id],self.genderinput.text)
                birthday = datetime.datetime(int(self.dateofbirth_year.text),int(self.dateofbirth_Month.text),int(self.dateofbirth_Day.text))
                personal_docks.PersonalDock.change_birthday(amber.database[self.user_id],birthday)
                if personal_docks.PersonalDock.check_password(amber.database[self.user_id],self.oldpass.text) and self.newpass.text==self.confirmnewpass.text:
                    personal_docks.PersonalDock.change_password(amber.database[self.user_id],self.newpass.text)
                edit_profile_screen = Screen(name='edit')
                edit_profile_screen.add_widget(Page.EditProfilePage(user_id=self.user_id, destination_id=self.destination_id,
                                                               screen_manager=self.screen_manager))
                self.screen_manager.add_widget(edit_profile_screen)
                self.screen_manager.current = edit_profile_screen.name

        def __init__(self, user_id, destination_id, screen_manager, **kwargs):
            super(Page.EditAboutPage, self).__init__(**kwargs)
            self.user_id = user_id
            self.destination_id = destination_id
            self.screen_manager = screen_manager
            self.orientation = 'vertical'
            self.add_widget(Label(text='Edit About Information',size_hint_y=0.05))
            self.profileData = GridLayout(cols=2, padding=30, spacing=10)
            self.profileData.height = 200
            #activation
            self.profileData.add_widget(
                Label(text='Deactivate account:', size_hint_y=None, size_hint_x=None, width=150, height=40))
            self.deactivateInput = Switch(active=not(amber.database[user_id].active), size_hint_y=None, height=40)
            self.profileData.add_widget(self.deactivateInput)
            # name
            self.profileData.add_widget(
                Label(text='Name:', size_hint_y=None, size_hint_x=None, width=150, height=40))
            self.nameinput = TextInput(text=amber.database[user_id].name, size_hint_y=None, height=40)
            self.profileData.add_widget(self.nameinput)
            ###newpassword
            self.profileData.add_widget(
                Label(text='Create new password:', size_hint_y=None, size_hint_x=None, width=150, height=40))
            self.newpassinput = TextInput(text=amber.database[user_id].password, password=True, size_hint_y=None,
                                          height=40)
            self.profileData.add_widget(self.newpassinput)
            ###confirm password
            self.profileData.add_widget(
                Label(text='confirm new password:', size_hint_y=None, size_hint_x=None, width=150, height=40))
            self.confirmnewpassinput = TextInput(text=amber.database[user_id].password, password=True, size_hint_y=None,
                                                 height=40)
            self.profileData.add_widget(self.confirmnewpassinput)
            ###old password
            self.profileData.add_widget(
                Label(text='old password:', size_hint_y=None, size_hint_x=None, width=150, height=40))

            self.oldpassinput = TextInput(text="", password=True, size_hint_y=None,
                                          height=40)
            self.profileData.add_widget(self.oldpassinput)
            ###Gender
            self.profileData.add_widget(
                 Label(text='Gender:', size_hint_y=None, size_hint_x=None, width=150, height=40))
            # self.genderinput = Spinner(text=amber.database[user_id].gender,values=('male','female','other'), size_hint_y=None,
            #                                height=40)
            self.genderinput = TextInput(text=amber.database[user_id].gender,
                                       size_hint_y=None,
                                       height=40)
            self.profileData.add_widget(self.genderinput)

            ###birthday
            Birthday = str(amber.database[user_id].birthday).split(' ')
            BirthdayValues= Birthday[0].split('-')
            self.birthdayinputRow = BoxLayout(orientation='horizontal',size_hint_y=None,height=40)
            self.profileData.add_widget(
                Label(text='Birthday:', size_hint_y=None, size_hint_x=None, width=150, height=40))
            self.birthdayinputyear = TextInput(text=str(BirthdayValues[0]),size_hint_y=None,height=40)
            self.birthdayinputmonth = TextInput(text=str(BirthdayValues[1]),size_hint_y=None,height=40)
            self.birthdayinputday = TextInput(text=str(BirthdayValues[2]),size_hint_y=None,height=40)
            self.birthdayinputRow.add_widget(self.birthdayinputyear)
            self.birthdayinputRow.add_widget(self.birthdayinputmonth)
            self.birthdayinputRow.add_widget(self.birthdayinputday)
            self.profileData.add_widget(self.birthdayinputRow)



            self.add_widget(self.profileData)
            self.add_widget(self.Save_button())
        def Save_button(self, **kwargs):
            return Page.EditAboutPage.SaveButton(user_id=self.user_id, destination_id=self.destination_id,
                                                 deactivateInput=self.deactivateInput,
                                                   nameinput=self.nameinput,
                                                   genderinput=self.genderinput,
                                                 dateofbirth_year=self.birthdayinputyear,
                                                 dateofbirth_Month=self.birthdayinputmonth,
                                                 dateofbirth_Day=self.birthdayinputday,
                                                   oldpass=self.oldpassinput,
                                                   newpass=self.newpassinput,
                                                   confirmnewpass=self.confirmnewpassinput,
                                                   screen_manager=self.screen_manager, **kwargs)

    class EditEduPage(BoxLayout):
        '''
            THIS PAGE CAN EDIT AND ADD NEW:
                Education       :using spinneer for dates , and replace textinput by solid buttons after save
                Living PLaces   :using spinneer for dates , and replace textinput by solid buttons after save
        '''
        class RemoveEduButton(Button):
            def __init__(self, user_id, destination_id, screen_manager,parentwidget,eduArray,eduBoxWidget,majoredu,placeedu, **kwargs):
                super(Page.EditEduPage.RemoveEduButton, self).__init__(**kwargs)
                self.user_id = user_id
                self.destination_id = destination_id
                self.screen_manager = screen_manager
                self.parentwidget=parentwidget
                self.eduArray=eduArray
                self.eduBoxWidget=eduBoxWidget
                self.majoredu=majoredu
                self.placeedu=placeedu
                self.size_hint_y = None
                self.size_hint_x = 0.05
                self.height = 30
                self.text = '-'
                self.font_size=70

            def on_release(self):
                if self.majoredu.text!='' and self.placeedu.text!='':
                    personal_docks.PersonalDock.remove_education(amber.database[self.user_id],
                                                                 self.majoredu.text,
                                                                 self.placeedu.text)
                self.parentwidget.remove_widget(self.eduBoxWidget)
                index = self.eduArray.index(self.eduBoxWidget)
                self.eduArray.pop(index)
        class EditEduButton(Button):
            def __init__(self, user_id, destination_id, screen_manager,parentwidget,eduArray,
                         eduBoxWidget,majoredu,placeedu,startdate,enddate, **kwargs):
                super(Page.EditEduPage.EditEduButton, self).__init__(**kwargs)
                self.user_id = user_id
                self.destination_id = destination_id
                self.screen_manager = screen_manager
                self.parentwidget = parentwidget
                self.eduArray = eduArray
                self.eduBoxWidget = eduBoxWidget
                self.majoredu = majoredu
                self.placeedu = placeedu
                self.startdate = startdate
                self.enddate = enddate
                self.size_hint_y = None
                self.size_hint_x = 0.05
                self.height = 30
                self.text = 'Edit'
                self.font_size = 14

            def on_release(self):
                # self.eduBoxWidget.remove_widget(self.startdate)
                # self.eduBoxWidget.remove_widget(self.enddate)
                self.eduBoxWidget.clear_widgets()

                self.majoredu=Button(text=self.majoredu.text,
                                        size_hint_x=0.4, size_hint_y=None, height=30)
                self.placeedu=Button(text=self.placeedu.text,
                                        size_hint_x=0.4, size_hint_y=None, height=30)
                self.startdate = TextInput(text=self.startdate.text,
                                        size_hint_x=0.1, size_hint_y=None, height=30)
                self.enddate = TextInput(text=self.enddate.text,
                                      size_hint_x=0.1, size_hint_y=None, height=30)
                self.eduBoxWidget.add_widget(self.majoredu)
                self.eduBoxWidget.add_widget(self.placeedu)
                self.eduBoxWidget.add_widget(self.startdate)
                self.eduBoxWidget.add_widget(self.enddate)
                self.eduBoxWidget.add_widget(Page.EditEduPage.SaveEdu_button(self, self.parentwidget,
                                                                             self.eduArray,
                                                                             self.eduBoxWidget,
                                                                             self.majoredu,
                                                                             self.placeedu,
                                                                             self.startdate,
                                                                             self.enddate))
                self.eduBoxWidget.add_widget(Page.EditEduPage.RemoveEdu_button(self, self.parentwidget,
                                                                               self.eduArray,
                                                                               self.eduBoxWidget,
                                                                               self.majoredu,
                                                                               self.placeedu))

        class SaveEduButton(Button):
            def __init__(self, user_id, destination_id, screen_manager,parentwidget,eduArray,
                         eduBoxWidget,majoredu,placeedu,startdate,enddate, **kwargs):
                super(Page.EditEduPage.SaveEduButton, self).__init__(**kwargs)
                self.user_id = user_id
                self.destination_id = destination_id
                self.screen_manager = screen_manager
                self.parentwidget=parentwidget
                self.eduArray=eduArray
                self.eduBoxWidget=eduBoxWidget
                self.majoredu=majoredu
                self.placeedu=placeedu
                self.startdate = startdate
                self.enddate = enddate
                self.size_hint_y = None
                self.size_hint_x = 0.05
                self.height = 30
                self.text = 'Save'
                self.font_size=14

            def on_release(self):
                if self.majoredu.text!='' and self.placeedu.text!='' and self.startdate.text!='' and self.enddate.text !='' :

                    if not personal_docks.PersonalDock.edit_education(amber.database[self.user_id],
                                                               self.majoredu.text,
                                                               self.placeedu.text,
                                                               self.startdate.text,
                                                               self.enddate.text):

                        personal_docks.PersonalDock.add_education(amber.database[self.user_id],
                                                              self.majoredu.text,
                                                              self.placeedu.text,
                                                              self.startdate.text,
                                                              self.enddate.text)

                    self.eduBoxWidget.clear_widgets()

                    self.majoredu = Button(text=self.majoredu.text,
                                           size_hint_x=0.4, size_hint_y=None, height=30)
                    self.placeedu = Button(text=self.placeedu.text,
                                           size_hint_x=0.4, size_hint_y=None, height=30)
                    self.startdate = Button(text=self.startdate.text,
                                                     size_hint_x=0.1, size_hint_y=None, height=30)
                    self.enddate = Button(text=self.enddate.text,
                                                         size_hint_x=0.1, size_hint_y=None, height=30)
                    self.eduBoxWidget.add_widget(self.majoredu)
                    self.eduBoxWidget.add_widget(self.placeedu)
                    self.eduBoxWidget.add_widget(self.startdate)
                    self.eduBoxWidget.add_widget(self.enddate)
                    self.eduBoxWidget.add_widget(Page.EditEduPage.EditEdu_button(self, self.parentwidget,
                                                                                 self.eduArray,
                                                                                 self.eduBoxWidget,
                                                                                 self.majoredu,
                                                                                 self.placeedu,
                                                                                 self.startdate,
                                                                                 self.enddate))
                    self.eduBoxWidget.add_widget(Page.EditEduPage.RemoveEdu_button(self, self.parentwidget,
                                                                                               self.eduArray,
                                                                                               self.eduBoxWidget,
                                                                                               self.majoredu,
                                                                                               self.placeedu))

        class AddEduButton(Button):
            def __init__(self, user_id, destination_id, screen_manager,edubox,eduArray, **kwargs):
                super(Page.EditEduPage.AddEduButton, self).__init__(**kwargs)
                self.user_id = user_id
                self.destination_id = destination_id
                self.screen_manager = screen_manager
                self.edubox=edubox
                self.eduArray=eduArray
                self.size_hint_y = None
                self.size_hint_x = 1
                self.height = 50
                self.text = 'Add Education'

            def on_release(self):
                self.edubox.remove_widget(self)

                index = len(self.eduArray)
                self.eduArray.append(BoxLayout(orientation='horizontal', size_hint_y=None,height=50, padding=5, spacing=10))
                # self.eduArray[index].edulabelnum = Label(text=str(index + 1), size_hint_x=None, width=50,
                #                         size_hint_y=None, height=50)
                # # with edulabelnum.canvas:
                # #     Color(1, 1, 1, 0.2)
                # #     Rectangle(pos=edulabelnum.pos, size=edulabelnum.size)
                # self.eduArray[index].add_widget(self.eduArray[index].edulabelnum)
                self.eduArray[index].majorinput = TextInput( size_hint_x=0.4,
                                           size_hint_y=None, height=30)
                self.eduArray[index].add_widget(self.eduArray[index].majorinput)
                self.eduArray[index].placeinput = TextInput( size_hint_x=0.4,
                                           size_hint_y=None, height=30)
                self.eduArray[index].add_widget(self.eduArray[index].placeinput)
                self.eduArray[index].startdateinput = TextInput( size_hint_x=0.1,
                                               size_hint_y=None, height=30)
                self.eduArray[index].add_widget(self.eduArray[index].startdateinput)
                self.eduArray[index].finishdateinput = TextInput( size_hint_x=0.1,
                                                size_hint_y=None, height=30)
                self.eduArray[index].add_widget(self.eduArray[index].finishdateinput)
                self.eduArray[index].add_widget(Page.EditEduPage.SaveEdu_button(self,self.edubox,
                                                                                self.eduArray,
                                                                                self.eduArray[index],
                                                                                self.eduArray[index].majorinput,
                                                                                self.eduArray[index].placeinput,
                                                                                self.eduArray[index].startdateinput,
                                                                                self.eduArray[index].finishdateinput))
                self.eduArray[index].add_widget(Page.EditEduPage.RemoveEdu_button(self,self.edubox,
                                                                                  self.eduArray,
                                                                                  self.eduArray[index],
                                                                                  self.eduArray[index].majorinput,
                                                                                  self.eduArray[index].placeinput))
                self.edubox.add_widget(self.eduArray[index])
                self.edubox.add_widget(Page.EditEduPage.AddEdu_button(self,self.edubox, self.eduArray))

        class RemovePlaceButton(Button):
            def __init__(self, user_id, destination_id, screen_manager,parentwidget,placeArray,placeBoxWidget,place, **kwargs):
                super(Page.EditEduPage.RemovePlaceButton, self).__init__(**kwargs)
                self.user_id = user_id
                self.destination_id = destination_id
                self.screen_manager = screen_manager
                self.parentwidget=parentwidget
                self.placeArray=placeArray
                self.placeBoxWidget=placeBoxWidget
                self.place=place
                self.size_hint_y = None
                self.size_hint_x = 0.05
                self.height = 30
                self.text = '-'
                self.font_size=50

            def on_release(self):
                if self.place.text != '':
                    personal_docks.PersonalDock.remove_living_place(amber.database[self.user_id],
                                                                 self.place.text)
                self.parentwidget.remove_widget(self.placeBoxWidget)
                index = self.placeArray.index(self.placeBoxWidget)
                self.placeArray.pop(index)
        class SavePlaceButton(Button):
            def __init__(self, user_id, destination_id, screen_manager,parentwidget,placeArray,
                         placeBoxWidget,place,startdate,enddate, **kwargs):
                super(Page.EditEduPage.SavePlaceButton, self).__init__(**kwargs)
                self.user_id = user_id
                self.destination_id = destination_id
                self.screen_manager = screen_manager
                self.parentwidget=parentwidget
                self.placeArray=placeArray
                self.placeBoxWidget=placeBoxWidget
                self.place=place
                self.startdate = startdate
                self.enddate = enddate
                self.size_hint_y = None
                self.size_hint_x = 0.05
                self.height = 30
                self.text = 'save'
                self.font_size=14

            def on_release(self):
                if not personal_docks.PersonalDock.edit_living_place(amber.database[self.user_id],
                                                           self.place.text,
                                                           self.startdate.text,
                                                           self.enddate.text):

                    personal_docks.PersonalDock.add_living_place(amber.database[self.user_id],
                                                          self.place.text,
                                                          self.startdate.text,
                                                          self.enddate.text)
                self.placeBoxWidget.clear_widgets()

                self.place = Button(text=self.place.text,
                                       size_hint_x=0.4, size_hint_y=None, height=30)
                self.startdate = Button(text=self.startdate.text,
                                        size_hint_x=0.1, size_hint_y=None, height=30)
                self.enddate = Button(text=self.enddate.text,
                                      size_hint_x=0.1, size_hint_y=None, height=30)
                self.placeBoxWidget.add_widget(self.place)
                self.placeBoxWidget.add_widget(self.startdate)
                self.placeBoxWidget.add_widget(self.enddate)
                self.placeBoxWidget.add_widget(Page.EditEduPage.EditPlace_button(self, self.parentwidget,
                                                                             self.placeArray,
                                                                             self.placeBoxWidget,
                                                                             self.place,
                                                                             self.startdate,
                                                                             self.enddate))
                self.placeBoxWidget.add_widget(Page.EditEduPage.RemovePlace_button(self, self.parentwidget,
                                                                               self.placeArray,
                                                                               self.placeBoxWidget,
                                                                               self.place))


        class EditPlaceButton(Button):
            def __init__(self, user_id, destination_id, screen_manager,parentwidget,placeArray,
                         placeBoxWidget,place,startdate,enddate, **kwargs):
                super(Page.EditEduPage.EditPlaceButton, self).__init__(**kwargs)
                self.user_id = user_id
                self.destination_id = destination_id
                self.screen_manager = screen_manager
                self.parentwidget=parentwidget
                self.placeArray=placeArray
                self.placeBoxWidget=placeBoxWidget
                self.place=place
                self.startdate = startdate
                self.enddate = enddate
                self.size_hint_y = None
                self.size_hint_x = 0.05
                self.height = 30
                self.text = 'Edit'
                self.font_size=14

            def on_release(self):
                self.placeBoxWidget.clear_widgets()

                self.place = Button(text=self.place.text,
                                       size_hint_x=0.4, size_hint_y=None, height=30)
                self.startdate = TextInput(text=self.startdate.text,
                                        size_hint_x=0.1, size_hint_y=None, height=30)
                self.enddate = TextInput(text=self.enddate.text,
                                      size_hint_x=0.1, size_hint_y=None, height=30)
                self.placeBoxWidget.add_widget(self.place)
                self.placeBoxWidget.add_widget(self.startdate)
                self.placeBoxWidget.add_widget(self.enddate)
                self.placeBoxWidget.add_widget(Page.EditEduPage.SavePlace_button(self, self.parentwidget,
                                                                             self.placeArray,
                                                                             self.placeBoxWidget,
                                                                             self.place,
                                                                             self.startdate,
                                                                             self.enddate))
                self.placeBoxWidget.add_widget(Page.EditEduPage.RemovePlace_button(self, self.parentwidget,
                                                                               self.placeArray,
                                                                               self.placeBoxWidget,
                                                                               self.place))


        class AddPlaceButton(Button):
            def __init__(self, user_id, destination_id, screen_manager,placebox,placeArray,**kwargs):
                super(Page.EditEduPage.AddPlaceButton, self).__init__(**kwargs)
                self.user_id = user_id
                self.destination_id = destination_id
                self.screen_manager = screen_manager
                self.placebox=placebox
                self.placeArray=placeArray
                self.size_hint_y = None
                self.size_hint_x = 1
                self.height = 50
                self.text = 'Add Place'

            def on_release(self):
                self.placebox.remove_widget(self)

                index = len(self.placeArray)
                self.placeArray.append(BoxLayout(orientation='horizontal', size_hint_y=None,height=50, padding=5, spacing=10))
                # self.placeArray[index].placelabelnum = Label(text=str(index + 1), size_hint_x=None, width=50,
                #                         size_hint_y=None, height=50)
                # # with edulabelnum.canvas:
                # #     Color(1, 1, 1, 0.2)
                # #     Rectangle(pos=edulabelnum.pos, size=edulabelnum.size)
                # self.placeArray[index].add_widget(self.placeArray[index].placelabelnum)
                self.placeArray[index].placeinput = TextInput( size_hint_x=0.4,
                                           size_hint_y=None, height=30)
                self.placeArray[index].add_widget(self.placeArray[index].placeinput)
                self.placeArray[index].startdateinput = TextInput( size_hint_x=0.1,
                                               size_hint_y=None, height=30)
                self.placeArray[index].add_widget(self.placeArray[index].startdateinput)
                self.placeArray[index].finishdateinput = TextInput( size_hint_x=0.1,
                                                size_hint_y=None, height=30)
                self.placeArray[index].add_widget(self.placeArray[index].finishdateinput)
                self.placeArray[index].add_widget(Page.EditEduPage.SavePlace_button(self,self.placebox,
                                                                                self.placeArray,
                                                                                self.placeArray[index],
                                                                                self.placeArray[index].placeinput,
                                                                                self.placeArray[index].startdateinput,
                                                                                self.placeArray[index].finishdateinput))
                self.placeArray[index].add_widget(Page.EditEduPage.RemovePlace_button(self,self.placebox,self.placeArray,
                                                                                      self.placeArray[index],
                                                                                      self.placeArray[index].placeinput))
                self.placebox.add_widget(self.placeArray[index])
                self.placebox.add_widget(Page.EditEduPage.AddPlace_button(self,self.placebox, self.placeArray))


        def __init__(self, user_id, destination_id, screen_manager, **kwargs):
            super(Page.EditEduPage, self).__init__(**kwargs)
            self.user_id = user_id
            self.destination_id = destination_id
            self.screen_manager = screen_manager
            self.orientation = 'vertical'
            self.clear_widgets()
            ###Education information
            self.edulabel=Label(text='Edit Education', size_hint_y= None,height=40)
            # with self.edulabel.canvas:
            #     Color(1, 1, 1, 0.2)
            #     # Rectangle(pos=(0,400), size_hint_y=None , height=20)
            #     Rectangle(pos=self.edulabel.pos, size=self.edulabel.size)
            # self.add_widget(self.edulabel)
            self.eduheader = BoxLayout(orientation='horizontal', size_hint_y=None, height=40, padding=10, spacing=10)
            self.eduheader.add_widget(Button(text='Major', size_hint_x=0.4, size_hint_y=None, height=30,disabled=True))
            self.eduheader.add_widget(Button(text='university', size_hint_x=0.4, size_hint_y=None, height=30,disabled=True))
            self.eduheader.add_widget(Button(text='Start\ndate', size_hint_x=0.1, size_hint_y=None, height=30,disabled=True))
            self.eduheader.add_widget(Button(text='Finish\ndate', size_hint_x=0.1, size_hint_y=None, height=30,disabled=True))
            self.eduheader.add_widget(Button(text='+', size_hint_x=0.05, size_hint_y=None, height=30,disabled=True))
            self.eduheader.add_widget(Button(text='-', size_hint_x=0.05, size_hint_y=None, height=30,disabled=True))
            self.add_widget(self.eduheader)


            self.EducationBoxes = []
            # edu is tuple of four elements (major, place of education, starting date, finishing date)
            for edu in amber.database[user_id].education:
                self.EducationBoxes.append(BoxLayout(orientation='horizontal',size_hint_y=None , padding=5, spacing=10))

            self.EduBox = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint_y=None)
            for index,edu in enumerate(self.EducationBoxes):
                # edu.edulabelnum = Label(text=str(index+1),size_hint_x=None ,width=50,
                #                         size_hint_y=None, height=50)
                #
                # edu.add_widget(edu.edulabelnum)
                edu.majorinput=Button(text=amber.database[user_id].education[index][0], size_hint_x=0.4,
                                         size_hint_y=None , height=30)
                edu.add_widget(edu.majorinput)
                edu.placeinput = Button(text=amber.database[user_id].education[index][1], size_hint_x=0.4,
                                           size_hint_y=None, height=30)
                edu.add_widget(edu.placeinput)
                edu.startdateinput = Button(text=amber.database[user_id].education[index][2], size_hint_x=0.1,
                                              size_hint_y=None, height=30)
                edu.add_widget(edu.startdateinput)
                edu.finishdateinput = Button(text=amber.database[user_id].education[index][3], size_hint_x=0.1,
                                                size_hint_y=None, height=30)
                edu.add_widget(edu.finishdateinput)
                edu.add_widget(self.EditEdu_button(self.EduBox,
                                                    self.EducationBoxes,
                                                    edu,edu.majorinput,
                                                    edu.placeinput,
                                                    edu.startdateinput,
                                                    edu.finishdateinput))
                edu.add_widget(self.RemoveEdu_button(self.EduBox,self.EducationBoxes,edu,edu.majorinput,edu.placeinput))

                # edu.RemoveButton.on_release(print('pressed'))
                self.EduBox.add_widget(edu)
            self.EduBox.add_widget(self.AddEdu_button(self.EduBox,self.EducationBoxes))
            self.EduBox.bind(minimum_height=self.EduBox.setter('height'))
            self.EduBoxScrollView = ScrollView(size_hint=(1, None), size=(200,200))
            self.EduBoxScrollView.add_widget(self.EduBox)
            self.add_widget(self.EduBoxScrollView)

            ###places information
            self.placelabel = Label(text='Edit places', size_hint_y=0.05, height=30, width=2000, pos=(0, 250))
            # with self.placelabel.canvas:
            #     Color(1, 1, 1, 0.2)
            #     # Rectangle(pos=(0,400), size_hint_y=None , height=20)
            #     Rectangle(pos=self.placelabel.pos, size=self.placelabel.size)

            self.add_widget(self.placelabel)
            self.placesheader = BoxLayout(orientation='horizontal', size_hint_y=None,height=50, padding=5, spacing=10)
            self.placesheader.add_widget(Label(text='Location',size_hint_x=0.3,size_hint_y=None, height=50))
            self.placesheader.add_widget(Label(text='From(start date)',size_hint_x=0.3, size_hint_y = None, height = 50))
            self.placesheader.add_widget(Label(text='to(end date)',size_hint_x=0.3, size_hint_y = None, height = 50))
            self.placesheader.add_widget(Label(text='Save/Remove',size_hint_x=0.1, size_hint_y = None, height = 50))
            self.add_widget(self.placesheader)
            self.PlacesBoxes = []
            # edu is tuple of four elements (major, place of education, starting date, finishing date)
            for place in amber.database[user_id].living_in:
                self.PlacesBoxes.append(BoxLayout(orientation='horizontal', size_hint_y=None, padding=5, spacing=10))

            self.placesBox = BoxLayout(orientation='vertical', height=50, padding=5, spacing=10, size_hint_y=None)
            for index, place in enumerate(self.PlacesBoxes):
                place.placeinput = Button(text=amber.database[user_id].living_in[index][0], size_hint_x=0.3,
                                           size_hint_y=None, height=30)
                place.add_widget(place.placeinput)
                place.startdateinput = Button(text=amber.database[user_id].living_in[index][1], size_hint_x=0.3,
                                               size_hint_y=None, height=30)
                place.add_widget(place.startdateinput)
                place.finishdateinput = Button(text=amber.database[user_id].living_in[index][2], size_hint_x=0.3,
                                                size_hint_y=None, height=30)
                place.add_widget(place.finishdateinput)
                place.add_widget(
                    self.RemovePlace_button(self.placesBox, self.PlacesBoxes, place, place.placeinput))


                self.placesBox.add_widget(place)
            self.placesBox.add_widget(self.AddPlace_button(self.placesBox, self.PlacesBoxes))
            self.placesBox.bind(minimum_height=self.placesBox.setter('height'))
            self.placesBoxScrollView = ScrollView(size_hint=(1, None), size=(200, 200))
            self.placesBoxScrollView.add_widget(self.placesBox)
            self.add_widget(self.placesBoxScrollView)
            # self.add_widget(self.Save_button())

            # self.EduBox.remove_widget(self.EducationBoxes[0])
        def RemoveEdu_button(self,edubox,eduArray,edu,major,place, **kwargs):
            return Page.EditEduPage.RemoveEduButton(user_id=self.user_id, destination_id=self.destination_id,screen_manager=self.screen_manager ,
                                                    parentwidget=edubox,
                                                    eduArray=eduArray,
                                                    eduBoxWidget=edu,
                                                    majoredu=major, placeedu=place,**kwargs)
        def SaveEdu_button(self,edubox,eduArray,edu,major,place,startdate,enddate, **kwargs):
            return Page.EditEduPage.SaveEduButton(user_id=self.user_id, destination_id=self.destination_id,screen_manager=self.screen_manager ,
                                                    parentwidget=edubox,
                                                    eduArray=eduArray,
                                                    eduBoxWidget=edu,
                                                    majoredu=major, placeedu=place,
                                                    startdate=startdate, enddate=enddate,**kwargs)
        def AddEdu_button(self,edubox,eduArray,**kwargs):
            return Page.EditEduPage.AddEduButton(user_id=self.user_id, destination_id=self.destination_id,screen_manager=self.screen_manager ,
                                                  edubox=edubox,eduArray=eduArray,
                                                 **kwargs)

        def EditEdu_button(self,edubox,eduArray,edu,major,place,startdate,enddate, **kwargs):
            return Page.EditEduPage.EditEduButton(user_id=self.user_id, destination_id=self.destination_id,
                                                  screen_manager=self.screen_manager,
                                                  parentwidget=edubox,
                                                  eduArray=eduArray,
                                                  eduBoxWidget=edu,
                                                  majoredu=major, placeedu=place,
                                                  startdate=startdate, enddate=enddate, **kwargs)


        def RemovePlace_button(self,placebox,placeArray,oneplace,place, **kwargs):
            return Page.EditEduPage.RemovePlaceButton(user_id=self.user_id, destination_id=self.destination_id,screen_manager=self.screen_manager ,
                                                    parentwidget=placebox,
                                                    placeArray=placeArray,
                                                    placeBoxWidget=oneplace,
                                                    place=place,**kwargs)
        def SavePlace_button(self,placebox,placeArray,oneplace,place,startdate,enddate, **kwargs):
            return Page.EditEduPage.SavePlaceButton(user_id=self.user_id, destination_id=self.destination_id,screen_manager=self.screen_manager ,
                                                    parentwidget=placebox,
                                                    placeArray=placeArray,
                                                    placeBoxWidget=oneplace,
                                                    place=place,
                                                    startdate=startdate, enddate=enddate,**kwargs)
        def EditPlace_button(self,placebox,placeArray,oneplace,place,startdate,enddate, **kwargs):
            return Page.EditEduPage.EditPlaceButton(user_id=self.user_id, destination_id=self.destination_id,screen_manager=self.screen_manager ,
                                                    parentwidget=placebox,
                                                    placeArray=placeArray,
                                                    placeBoxWidget=oneplace,
                                                    place=place,
                                                    startdate=startdate, enddate=enddate,**kwargs)

        def AddPlace_button(self,placebox,placeArray,**kwargs):
            return Page.EditEduPage.AddPlaceButton(user_id=self.user_id, destination_id=self.destination_id,screen_manager=self.screen_manager ,
                                                  placebox=placebox,placeArray=placeArray,
                                                 **kwargs)

    class EditContactPage(BoxLayout):
        '''
            THIS PAGE CAN EDIT AND ADD NEW:
                Emails          :Done without test
                Phone Number    :Done without test
                Links           :Done without test
        '''
        class EditMasterPhoneButton(Button):
            def __init__(self,user_id, destination_id, screen_manager,MasterPhoneBox,PhoneNumWidget,**kwargs):
                super(Page.EditContactPage.EditMasterPhoneButton, self).__init__(**kwargs)
                self.user_id = user_id
                self.destination_id = destination_id
                self.screen_manager = screen_manager
                self.MasterPhoneBox=MasterPhoneBox
                self.PhoneNumWidget=PhoneNumWidget
                self.size_hint_y = None
                self.size_hint_x = 0.05
                self.height = 30
                self.text = 'Edit'
                self.font_size = 10
            def on_release(self):
                self.MasterPhoneBox.remove_widget(self)
                self.MasterPhoneBox.remove_widget(self.PhoneNumWidget)
                self.PhoneNuminput=TextInput(text=str(amber.database[self.user_id].master_phone_number),
                                            size_hint_x=0.3,size_hint_y=None, height=30)
                self.MasterPhoneBox.add_widget(self.PhoneNuminput)
                self.MasterPhoneBox.add_widget(Page.EditContactPage.SaveMasterPhone_button(self,self.MasterPhoneBox,self.PhoneNuminput))
        class SaveMasterPhoneButton(Button):
            def __init__(self,user_id, destination_id, screen_manager,MasterPhoneBox,PhoneNumWidget,**kwargs):
                super(Page.EditContactPage.SaveMasterPhoneButton, self).__init__(**kwargs)
                self.user_id = user_id
                self.destination_id = destination_id
                self.screen_manager = screen_manager
                self.MasterPhoneBox=MasterPhoneBox
                self.PhoneNumWidget=PhoneNumWidget
                self.size_hint_y = None
                self.size_hint_x = 0.05
                self.height = 30
                self.text = 'Save'
                self.font_size = 10
            def on_release(self):
                valid_number = True
                for digit in self.PhoneNumWidget.text:
                    if not digit.isdigit():
                        valid_number = False
                UsersId= amber.generate_personal_docks()
                for id in UsersId :
                    if amber.database[id].master_phone_number == self.PhoneNumWidget.text:
                        valid_number = False

                if self.PhoneNumWidget.text == '' :
                    valid_number = False

                if valid_number :
                    personal_docks.PersonalDock.change_master_phone_number(amber.database[self.user_id],
                                                                 self.PhoneNumWidget.text)
                    self.MasterPhoneBox.remove_widget(self)
                    self.MasterPhoneBox.remove_widget(self.PhoneNumWidget)
                    self.PhoneNum = Button(text=str(amber.database[self.user_id].master_phone_number),
                                           size_hint_x=0.3, size_hint_y=None, height=30)
                    self.MasterPhoneBox.add_widget(self.PhoneNum)
                    self.MasterPhoneBox.add_widget(
                        Page.EditContactPage.EditMasterPhone_button(self, self.MasterPhoneBox, self.PhoneNum))
                else :
                    self.PhoneNumWidget.text = '!Sorry,This Phone Number is not Valid'
                    self.PhoneNumWidget.background_color = (1,0,0.1,1)

        class EditMasterMailButton(Button):
            def __init__(self, user_id, destination_id, screen_manager, MasterMailBox, MailNumWidget, **kwargs):
                super(Page.EditContactPage.EditMasterMailButton, self).__init__(**kwargs)
                self.user_id = user_id
                self.destination_id = destination_id
                self.screen_manager = screen_manager
                self.MasterMailBox = MasterMailBox
                self.MailNumWidget = MailNumWidget
                self.size_hint_y = None
                self.size_hint_x = 0.05
                self.height = 30
                self.text = 'Edit'
                self.font_size = 10

            def on_release(self):
                self.MasterMailBox.remove_widget(self)
                self.MasterMailBox.remove_widget(self.MailNumWidget)
                self.MailNuminput = TextInput(text=str(amber.database[self.user_id].master_email),
                                               size_hint_x=0.3, size_hint_y=None, height=30)
                self.MasterMailBox.add_widget(self.MailNuminput)
                self.MasterMailBox.add_widget(Page.EditContactPage.SaveMasterMail_button(self,self.MasterMailBox, self.MailNuminput))
        class SaveMasterMailButton(Button):
            def __init__(self, user_id, destination_id, screen_manager, MasterMailBox, MailNumWidget, **kwargs):
                super(Page.EditContactPage.SaveMasterMailButton, self).__init__(**kwargs)
                self.user_id = user_id
                self.destination_id = destination_id
                self.screen_manager = screen_manager
                self.MasterMailBox = MasterMailBox
                self.MailNumWidget = MailNumWidget
                self.size_hint_y = None
                self.size_hint_x = 0.05
                self.height = 30
                self.text = 'Save'
                self.font_size = 10

            def on_release(self):
                valid_mail=True
                UsersId = amber.generate_personal_docks()
                for id in UsersId:
                    if amber.database[id].master_email == self.MailNumWidget.text:
                        valid_mail = False
                if self.MailNumWidget.text == '' :
                    valid_mail = False

                if not '@' in self.MailNumWidget.text or not '.com' in self.MailNumWidget.text:
                    valid_mail = False

                if valid_mail :
                    personal_docks.PersonalDock.change_master_email(amber.database[self.user_id],
                                                                           self.MailNumWidget.text)
                    self.MasterMailBox.remove_widget(self)
                    self.MasterMailBox.remove_widget(self.MailNumWidget)
                    self.MailNum = Button(text=str(amber.database[self.user_id].master_email),
                                           size_hint_x=0.3, size_hint_y=None, height=30)
                    self.MasterMailBox.add_widget(self.MailNum)
                    self.MasterMailBox.add_widget(Page.EditContactPage.EditMasterMail_button(self,self.MasterMailBox,self.MailNum))
                else:
                    self.MailNumWidget.text = '!Sorry,This E-Mail is not Valid'
                    self.MailNumWidget.background_color = (1, 0, 0.1, 1)


        class RemovePhoneButton(Button):
            def __init__(self, user_id, destination_id, screen_manager,parentwidget,Phonelist,PhoneBoxWidget,PhoneNum, **kwargs):
                super(Page.EditContactPage.RemovePhoneButton, self).__init__(**kwargs)
                self.user_id = user_id
                self.destination_id = destination_id
                self.screen_manager = screen_manager
                self.parentwidget=parentwidget
                self.Phonelist=Phonelist
                self.PhoneBoxWidget=PhoneBoxWidget
                self.PhoneNum=PhoneNum
                self.size_hint_y = None
                self.size_hint_x = 0.05
                self.height = 30
                self.text = '-'
                self.font_size=20

            def on_release(self):
                if self.PhoneNum.text != '':
                    personal_docks.PersonalDock.remove_phone_number(amber.database[self.user_id],
                                                                 self.PhoneNum.text)
                self.parentwidget.remove_widget(self.PhoneBoxWidget)
                index = self.Phonelist.index(self.PhoneBoxWidget)
                self.Phonelist.pop(index)
        class SavePhoneButton(Button):
            def __init__(self, user_id, destination_id, screen_manager,parentwidget,PhoneList,
                         PhoneBoxWidget,PhoneNum, **kwargs):
                super(Page.EditContactPage.SavePhoneButton, self).__init__(**kwargs)
                self.user_id = user_id
                self.destination_id = destination_id
                self.screen_manager = screen_manager
                self.parentwidget=parentwidget
                self.PhoneList=PhoneList
                self.PhoneBoxWidget=PhoneBoxWidget
                self.PhoneNum=PhoneNum
                self.size_hint_y = None
                self.size_hint_x = 0.05
                self.height = 30
                self.text = '+'
                self.font_size=30

            def on_release(self):
                valid_number=True
                for digit in self.PhoneNum.text:
                    if not digit.isdigit():
                        valid_number=False
                if valid_number and self.PhoneNum.text!='':
                    personal_docks.PersonalDock.add_phone_number(amber.database[self.user_id],
                                                              self.PhoneNum.text)
                    self.PhoneBoxWidget.remove_widget(self)
                    self.PhoneBoxWidget.remove_widget(self.PhoneNum)
                    savedphone=Button(text=str(self.PhoneNum.text) , size_hint_x=0.3,
                                             size_hint_y=None , height=30 )
                    self.PhoneBoxWidget.add_widget(savedphone)
                    self.PhoneBoxWidget.add_widget(Page.EditContactPage.RemovePhone_button(self,self.parentwidget,
                                                                                            self.PhoneList,
                                                                                            self.PhoneBoxWidget,self.PhoneNum))
                else :
                    self.PhoneBoxWidget.remove_widget(self)
                    self.PhoneBoxWidget.remove_widget(self.PhoneNum)
                    self.parentwidget.remove_widget(self.PhoneBoxWidget)
                    # self.PhoneBoxWidget.add_widget(Label(text='!sorry , Wrong number' , size_hint_x=0.3,
                    #                          size_hint_y=None , height=30 ))
        class AddPhoneButton(Button):
            def __init__(self, user_id, destination_id, screen_manager,PhoneBox,Phonelist,**kwargs):
                super(Page.EditContactPage.AddPhoneButton, self).__init__(**kwargs)
                self.user_id = user_id
                self.destination_id = destination_id
                self.screen_manager = screen_manager
                self.PhoneBox=PhoneBox
                self.Phonelist=Phonelist
                self.size_hint_y = None
                self.size_hint_x = 1
                self.height = 50
                self.text = 'Add Phone'

            def on_release(self):
                self.PhoneBox.remove_widget(self)

                index = len(self.Phonelist)
                self.Phonelist.append(BoxLayout(orientation='horizontal', size_hint_y=None,height=50, padding=5, spacing=10))
                self.Phonelist[index].Phoneinput = TextInput( size_hint_x=0.3,
                                                            size_hint_y=None, height=30)
                self.Phonelist[index].add_widget(self.Phonelist[index].Phoneinput)
                self.Phonelist[index].add_widget(Page.EditContactPage.SavePhone_button(self,self.PhoneBox,
                                                                                self.Phonelist,
                                                                                self.Phonelist[index],
                                                                                self.Phonelist[index].Phoneinput))

                self.PhoneBox.add_widget(self.Phonelist[index])
                self.PhoneBox.add_widget(Page.EditContactPage.AddPhone_button(self,self.PhoneBox, self.Phonelist))


        class RemoveMailButton(Button):
            def __init__(self, user_id, destination_id, screen_manager,MailColumn,MailList,MailBoxWidget,MailWidget, **kwargs):
                super(Page.EditContactPage.RemoveMailButton, self).__init__(**kwargs)
                self.user_id = user_id
                self.destination_id = destination_id
                self.screen_manager = screen_manager
                self.MailColumn=MailColumn
                self.MailList=MailList
                self.MailBoxWidget=MailBoxWidget
                self.MailWidget=MailWidget
                self.size_hint_y = None
                self.size_hint_x = 0.05
                self.height = 30
                self.text = '-'
                self.font_size=20

            def on_release(self):
                if self.MailWidget.text != '':
                    personal_docks.PersonalDock.remove_email(amber.database[self.user_id],
                                                                 self.MailWidget.text)
                self.MailColumn.remove_widget(self.MailBoxWidget)
                index = self.MailList.index(self.MailBoxWidget)
                self.MailList.pop(index)
        class SaveMailButton(Button):
            def __init__(self, user_id, destination_id, screen_manager,MailColumn,MailList,
                         MailBoxWidget,MailWidget, **kwargs):
                super(Page.EditContactPage.SaveMailButton, self).__init__(**kwargs)
                self.user_id = user_id
                self.destination_id = destination_id
                self.screen_manager = screen_manager
                self.MailColumn=MailColumn
                self.MailList=MailList
                self.MailBoxWidget=MailBoxWidget
                self.MailWidget=MailWidget
                self.size_hint_y = None
                self.size_hint_x = 0.05
                self.height = 30
                self.text = '+'
                self.font_size=30

            def on_release(self):
                if self.MailWidget.text!='':
                    personal_docks.PersonalDock.add_email(amber.database[self.user_id],
                                                              self.MailWidget.text)
                    self.MailBoxWidget.remove_widget(self)
                    self.MailBoxWidget.remove_widget(self.MailWidget)
                    savedMail=Button(text=str(self.MailWidget.text) , size_hint_x=0.3,
                                             size_hint_y=None , height=30 )
                    self.MailBoxWidget.add_widget(savedMail)
                    self.MailBoxWidget.add_widget(Page.EditContactPage.RemoveMail_button(self,self.MailColumn,
                                                                                            self.MailList,
                                                                                            self.MailBoxWidget,self.MailWidget))
                else :
                    self.MailBoxWidget.remove_widget(self)
                    self.MailBoxWidget.remove_widget(self.MailWidget)
                    self.MailColumn.remove_widget(self.MailBoxWidget)
                    # self.MailBoxWidget.add_widget(Label(text='!sorry , Wrong number' , size_hint_x=0.3,
                    #                          size_hint_y=None , height=30 ))
        class AddMailButton(Button):
            def __init__(self, user_id, destination_id, screen_manager,MailColumn,MailList,**kwargs):
                super(Page.EditContactPage.AddMailButton, self).__init__(**kwargs)
                self.user_id = user_id
                self.destination_id = destination_id
                self.screen_manager = screen_manager
                self.MailColumn=MailColumn
                self.MailList=MailList
                self.size_hint_y = None
                self.size_hint_x = 1
                self.height = 50
                self.text = 'Add E-Mail'

            def on_release(self):
                self.MailColumn.remove_widget(self)

                index = len(self.MailList)
                self.MailList.append(BoxLayout(orientation='horizontal', size_hint_y=None,height=50, padding=5, spacing=10))
                self.MailList[index].Mailinput = TextInput( size_hint_x=0.3,
                                                            size_hint_y=None, height=30)
                self.MailList[index].add_widget(self.MailList[index].Mailinput)
                self.MailList[index].add_widget(Page.EditContactPage.SaveMail_button(self,self.MailColumn,
                                                                                self.MailList,
                                                                                self.MailList[index],
                                                                                self.MailList[index].Mailinput))

                self.MailColumn.add_widget(self.MailList[index])
                self.MailColumn.add_widget(Page.EditContactPage.AddMail_button(self,self.MailColumn, self.MailList))

        class RemoveLinkButton(Button):
            def __init__(self,user_id, destination_id, screen_manager,LinksColumn,LinksList,LinkBox,LinkStrWidget,LinkURLWidget, **kwargs):
                super(Page.EditContactPage.RemoveLinkButton, self).__init__(**kwargs)
                self.user_id = user_id
                self.destination_id = destination_id
                self.screen_manager = screen_manager
                self.LinksColumn = LinksColumn
                self.LinksList = LinksList
                self.LinkBox=LinkBox
                self.LinkStrWidget = LinkStrWidget
                self.LinkURLWidget = LinkURLWidget
                self.size_hint_y = None
                self.size_hint_x = 0.05
                self.height = 30
                self.text = '-'
                self.font_size = 20
            def on_release(self):
                if self.LinkStrWidget.text != '' and self.LinkURLWidget.text != '':
                    personal_docks.PersonalDock.remove_link(amber.database[self.user_id],
                                                            self.LinkStrWidget.text)
                self.LinksColumn.remove_widget(self.LinkBox)
                index = self.LinksList.index(self.LinkBox)
                self.LinksList.pop(index)
        class SaveLinkButton(Button):
            def __init__(self, user_id, destination_id, screen_manager, LinksColumn, LinksList,LinkBox, LinkStrWidget,
                         LinkURLWidget, **kwargs):
                super(Page.EditContactPage.SaveLinkButton, self).__init__(**kwargs)
                self.user_id = user_id
                self.destination_id = destination_id
                self.screen_manager = screen_manager
                self.LinksColumn = LinksColumn
                self.LinksList = LinksList
                self.LinkBox=LinkBox
                self.LinkStrWidget = LinkStrWidget
                self.LinkURLWidget = LinkURLWidget
                self.size_hint_y = None
                self.size_hint_x = 0.05
                self.height = 30
                self.text = '+'
                self.font_size = 20
            def on_release(self):
                if self.LinkStrWidget.text != '' and self.LinkURLWidget.text != '':
                    personal_docks.PersonalDock.add_link(amber.database[self.user_id],
                                                          self.LinkStrWidget.text,self.LinkURLWidget.text)
                    # self.LinkBox.remove_widget(self)
                    # self.LinkBox.remove_widget(self.LinkStrWidget)
                    # self.LinkBox.remove_widget(self.LinkURLWidget)
                    self.LinkBox.clear_widgets()

                    self.savedLinkstr = Button(text=str(self.LinkStrWidget.text), size_hint_x=0.3,
                                       size_hint_y=None, height=30)
                    self.savedLinkurl = Button(text=str(self.LinkURLWidget.text), size_hint_x=0.3,
                                          size_hint_y=None, height=30)
                    self.LinkBox.add_widget(self.savedLinkstr)
                    self.LinkBox.add_widget(self.savedLinkurl)
                    self.LinkBox.add_widget(Page.EditContactPage.EditLink_button(self,self.LinksColumn,
                                                                                self.LinksList,
                                                                                self.LinkBox,
                                                                                self.savedLinkstr,
                                                                                self.savedLinkurl))
                    self.LinkBox.add_widget(Page.EditContactPage.RemoveLink_button(self,self.LinksColumn,
                                                                                self.LinksList,
                                                                                self.LinkBox,
                                                                                self.savedLinkstr,
                                                                                self.savedLinkurl))
        class EditLinkButton(Button):
            def __init__(self, user_id, destination_id, screen_manager, LinksColumn, LinksList,LinkBox, LinkStrWidget,
                         LinkURLWidget, **kwargs):
                super(Page.EditContactPage.EditLinkButton, self).__init__(**kwargs)
                self.user_id = user_id
                self.destination_id = destination_id
                self.screen_manager = screen_manager
                self.LinksColumn = LinksColumn
                self.LinksList = LinksList
                self.LinkBox=LinkBox
                self.LinkStrWidget = LinkStrWidget
                self.LinkURLWidget = LinkURLWidget
                self.size_hint_y = None
                self.size_hint_x = 0.05
                self.height = 30
                self.text = 'Edit'
                # self.font_size = 20
            def on_release(self):
                # self.LinkBox.remove_widget(self)
                # self.LinkBox.remove_widget(self.LinkStrWidget)
                # self.LinkBox.remove_widget(self.LinkURLWidget)
                self.LinkBox.clear_widgets()
                self.LinkStrInput = TextInput(text=self.LinkStrWidget.text,
                                              size_hint_x=0.3, size_hint_y=None, height=30)
                self.LinkURLInput = TextInput(text=self.LinkURLWidget.text,
                                              size_hint_x=0.3, size_hint_y=None, height=30)
                self.LinkBox.add_widget(self.LinkStrInput)
                self.LinkBox.add_widget(self.LinkURLInput)
                self.LinkBox.add_widget(Page.EditContactPage.SaveLink_button(self,self.LinksColumn,
                                                                                self.LinksList,
                                                                                self.LinkBox,
                                                                                self.LinkStrInput,
                                                                                self.LinkURLInput))
                self.LinkBox.add_widget(Page.EditContactPage.RemoveLink_button(self,self.LinksColumn,
                                                                                self.LinksList,
                                                                                self.LinkBox,
                                                                                self.LinkStrInput,
                                                                                self.LinkURLInput))
        class AddLinkButton(Button):
            def __init__(self, user_id, destination_id, screen_manager, LinksColumn, LinksList, **kwargs):
                super(Page.EditContactPage.AddLinkButton, self).__init__(**kwargs)
                self.user_id = user_id
                self.destination_id = destination_id
                self.screen_manager = screen_manager
                self.LinksColumn = LinksColumn
                self.LinksList = LinksList
                self.size_hint_y = None
                self.size_hint_x = 1
                self.height = 50
                self.text = 'Add Link URL'
            def on_release(self):
                self.LinksColumn.remove_widget(self)

                index = len(self.LinksList)
                self.LinksList.append(BoxLayout(orientation='horizontal', size_hint_y=None,height=50, padding=5, spacing=10))
                self.LinksList[index].LinkStrinput = TextInput( size_hint_x=0.3,
                                                            size_hint_y=None, height=30)
                self.LinksList[index].LinkURlinput = TextInput(size_hint_x=0.3,
                                                               size_hint_y=None, height=30)
                self.LinksList[index].add_widget(self.LinksList[index].LinkStrinput)
                self.LinksList[index].add_widget(self.LinksList[index].LinkURlinput)
                self.LinksList[index].add_widget(Page.EditContactPage.SaveLink_button(self,self.LinksColumn,
                                                                                self.LinksList,
                                                                                self.LinksList[index],
                                                                                self.LinksList[index].LinkStrinput,
                                                                                self.LinksList[index].LinkURlinput))
                self.LinksList[index].add_widget(Page.EditContactPage.RemoveLink_button(self,self.LinksColumn,
                                                                                self.LinksList,
                                                                                self.LinksList[index],
                                                                                self.LinksList[index].LinkStrinput,
                                                                                self.LinksList[index].LinkURlinput))

                self.LinksColumn.add_widget(self.LinksList[index])
                self.LinksColumn.add_widget(Page.EditContactPage.AddLink_button(self,self.LinksColumn, self.LinksList))



        def __init__(self, user_id, destination_id, screen_manager, **kwargs):
            super(Page.EditContactPage, self).__init__(**kwargs)
            self.user_id = user_id
            self.destination_id = destination_id
            self.screen_manager = screen_manager
            self.orientation = 'vertical'
            size_hint_y = 3
            self.add_widget(Label(text='',size_hint_y=1, height=50))
            self.Phonecolumn = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint_y=1)
            self.Emailcolumn = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint_y=1)
            self.LinksRow = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint_y=1)
            # self.contactheader = BoxLayout(orientation='horizontal', size_hint_y=None,height=40, padding=5, spacing=10)
            ###master phone and master mail
            self.MasterPhoneheader = Label(text='Master Mobile Phone', size_hint_x=1, size_hint_y=3, height=50)
            self.MasterEmailheader = Label(text='Master Email', size_hint_x=1, size_hint_y=3, height=50)
            self.Phonecolumn.add_widget(self.MasterPhoneheader)
            self.Emailcolumn.add_widget(self.MasterEmailheader)

            self.MasterPhoneBox = BoxLayout(orientation='horizontal', size_hint_y=None,height=50, padding=5, spacing=10)
            self.MasterPhoneButton = Button(text=str(amber.database[user_id].master_phone_number), size_hint_x=0.3,
                                size_hint_y=None, height=30)
            self.MasterPhoneBox.add_widget(self.MasterPhoneButton)
            self.MasterPhoneBox.add_widget(self.EditMasterPhone_button(self.MasterPhoneBox,self.MasterPhoneButton))

            self.Phonecolumn.add_widget(self.MasterPhoneBox)

            self.MasterMailBox = BoxLayout(orientation='horizontal', size_hint_y=None, height=50, padding=5,
                                            spacing=10)
            self.MasterMailButton = Button(text=str(amber.database[user_id].master_email), size_hint_x=0.3,
                                            size_hint_y=None, height=30)
            self.MasterMailBox.add_widget(self.MasterMailButton)
            self.MasterMailBox.add_widget(self.EditMasterMail_button(self.MasterMailBox,self.MasterMailButton))

            self.Emailcolumn.add_widget(self.MasterMailBox)

            self.Phoneheader = Label(text='Mobile Numbers',size_hint_x=1,size_hint_y=1, height=50)
            self.Emailheader = Label(text='Emails', size_hint_x=1, size_hint_y=1, height=50)
            self.Linksheader = Label(text='Links(Subject & URL)', size_hint_x=1, size_hint_y=1, height=50)

            self.Phonecolumn.add_widget(self.Phoneheader)
            self.Emailcolumn.add_widget(self.Emailheader)
            self.LinksRow.add_widget(self.Linksheader)


            ###Phone Information
            self.PhoneBox = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint_y=None)
            self.PhoneList =[]
            for index, Number in enumerate(amber.database[user_id].phone_numbers):
                # if index != 0:
                self.PhoneList.append(BoxLayout(orientation='horizontal', size_hint_y=None, padding=5, spacing=10))
            for index, Number in enumerate(self.PhoneList):
                if index != 0 :
                    Number.Phoneinput = Button(text=amber.database[user_id].phone_numbers[index], size_hint_x=0.3,
                                                 size_hint_y=None, height=30)
                    Number.add_widget(Number.Phoneinput)
                    Number.add_widget(
                        self.RemovePhone_button(self.PhoneBox, self.PhoneList, Number, Number.Phoneinput))

                    self.PhoneBox.add_widget(Number)
            self.PhoneBox.add_widget(self.AddPhone_button(self.PhoneBox, self.PhoneList))
            self.PhoneBox.bind(minimum_height=self.PhoneBox.setter('height'))
            self.PhoneBoxScrollView = ScrollView(size_hint=(1, None),size=(200,200))
            self.PhoneBoxScrollView.add_widget(self.PhoneBox)
            self.Phonecolumn.add_widget(self.PhoneBoxScrollView)

            ###Emails Information
            self.EmailBox = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint_y=None)
            self.EmailList=[]
            for index, mail in enumerate(amber.database[user_id].emails):
                # if index != 0:
                self.EmailList.append(BoxLayout(orientation='horizontal', size_hint_y=None, padding=5, spacing=10))
            for index, mail in enumerate(self.PhoneList):
                if index != 0 :
                    mail.mailinput = Button(text=amber.database[user_id].emails[index], size_hint_x=0.3,
                                                 size_hint_y=None, height=30)
                    mail.add_widget(mail.mailinput)
                    mail.add_widget(
                        self.RemoveMail_button(self.EmailBox, self.EmailList, mail, mail.mailinput))

                    self.EmailBox.add_widget(mail)
            self.EmailBox.add_widget(self.AddMail_button(self.EmailBox, self.EmailList))
            self.EmailBox.bind(minimum_height=self.EmailBox.setter('height'))
            self.EmailBoxScrollView = ScrollView(size_hint=(1, None), size=(200, 200))
            self.EmailBoxScrollView.add_widget(self.EmailBox)
            self.Emailcolumn.add_widget(self.EmailBoxScrollView)

            ###Links Information
            self.LinksBox = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint_y=None)
            self.LinksList=[]
            for  link in amber.database[user_id].links:
                # if index != 0:
                self.LinksList.append(BoxLayout(orientation='horizontal', size_hint_y=None, padding=5, spacing=10))
            for index, link in enumerate(self.LinksList):
                if index != 0 :
                    link.linkstrwidget = Button(text=amber.database[user_id].links[index][0], size_hint_x=0.3,
                                                 size_hint_y=None, height=30)
                    link.linkURLwidget = Button(text=amber.database[user_id].links[index][1], size_hint_x=0.3,
                                                size_hint_y=None, height=30)
                    link.add_widget(link.linkstrwidget)
                    link.add_widget(link.linkURLwidget)
                    link.add_widget(Page.EditContactPage.EditLink_button(self.LinksBox,
                                                                            self.LinksList,
                                                                            self.LinkBox,
                                                                            link.linkstrwidget,
                                                                            link.linkURLwidget))
                    link.add_widget(Page.EditContactPage.RemoveLink_button(self.LinksBox,
                                                                            self.LinksList,
                                                                            self.LinkBox,
                                                                            link.linkstrwidget,
                                                                            link.linkURLwidget))


                    self.LinksBox.add_widget(link)
            self.LinksBox.add_widget(self.AddLink_button(self.LinksBox, self.LinksList))
            self.LinksBox.bind(minimum_height=self.LinksBox.setter('height'))
            self.LinksBoxScrollView = ScrollView(size_hint=(1, None), size=(200, 200))
            self.LinksBoxScrollView.add_widget(self.LinksBox)
            self.LinksRow.add_widget(self.LinksBoxScrollView)
            self.PhoneAndMailRow = BoxLayout(orientation='horizontal', padding=10, spacing=10, size_hint_y=None)
            self.PhoneAndMailRow.add_widget(self.Phonecolumn)
            self.PhoneAndMailRow.add_widget(self.Emailcolumn)
            self.add_widget(self.PhoneAndMailRow)
            self.add_widget(self.LinksRow)

        def EditMasterPhone_button(self,MasterPhoneBox,PhoneNumWidget, **kwargs):
            return Page.EditContactPage.EditMasterPhoneButton(user_id=self.user_id,
                                                              destination_id=self.destination_id,
                                                              screen_manager=self.screen_manager,
                                                              MasterPhoneBox=MasterPhoneBox,
                                                              PhoneNumWidget=PhoneNumWidget)
        def SaveMasterPhone_button(self,MasterPhoneBox,PhoneNumWidget, **kwargs):
            return Page.EditContactPage.SaveMasterPhoneButton(user_id=self.user_id,
                                                              destination_id=self.destination_id,
                                                              screen_manager=self.screen_manager,
                                                              MasterPhoneBox=MasterPhoneBox,
                                                              PhoneNumWidget=PhoneNumWidget)
        def EditMasterMail_button(self,MasterMailBox, MailNumWidget, **kwargs):
            return Page.EditContactPage.EditMasterMailButton(user_id=self.user_id,
                                                              destination_id=self.destination_id,
                                                              screen_manager=self.screen_manager,
                                                             MasterMailBox=MasterMailBox,
                                                             MailNumWidget=MailNumWidget)
        def SaveMasterMail_button(self,MasterMailBox, MailNumWidget, **kwargs):
            return Page.EditContactPage.SaveMasterMailButton(user_id=self.user_id,
                                                              destination_id=self.destination_id,
                                                              screen_manager=self.screen_manager,
                                                             MasterMailBox=MasterMailBox,
                                                             MailNumWidget=MailNumWidget)

        def RemovePhone_button(self,PhoneBox,Phonelist,PhoneBoxWidget,PhoneNum, **kwargs):
            return Page.EditContactPage.RemovePhoneButton(user_id=self.user_id, destination_id=self.destination_id,
                                                      screen_manager=self.screen_manager,
                                                      parentwidget=PhoneBox,
                                                      Phonelist=Phonelist,
                                                      PhoneBoxWidget=PhoneBoxWidget,
                                                      PhoneNum=PhoneNum, **kwargs)
        def SavePhone_button(self,PhoneBox,Phonelist,PhoneBoxWidget,PhoneNum, **kwargs):
            return Page.EditContactPage.SavePhoneButton(user_id=self.user_id, destination_id=self.destination_id,
                                                      screen_manager=self.screen_manager,
                                                      parentwidget=PhoneBox,
                                                      PhoneList=Phonelist,
                                                      PhoneBoxWidget=PhoneBoxWidget,
                                                      PhoneNum=PhoneNum, **kwargs)
        def AddPhone_button(self,PhoneBox,Phonelist,**kwargs):
            return Page.EditContactPage.AddPhoneButton(user_id=self.user_id, destination_id=self.destination_id,
                                                      screen_manager=self.screen_manager,
                                                        PhoneBox=PhoneBox,
                                                      Phonelist=Phonelist,
                                                      **kwargs)

        def RemoveMail_button(self,MailColumn,MailList,MailBoxWidget,MailWidget,**kwargs):
            return Page.EditContactPage.RemoveMailButton(user_id=self.user_id,
                                                         destination_id=self.destination_id,
                                                         screen_manager=self.screen_manager,
                                                         MailColumn=MailColumn,
                                                         MailList=MailList,
                                                         MailBoxWidget=MailBoxWidget,
                                                         MailWidget=MailWidget, **kwargs)
        def SaveMail_button(self,MailColumn,MailList,MailBoxWidget,MailWidget,**kwargs):
            return Page.EditContactPage.SaveMailButton(user_id=self.user_id,
                                                       destination_id=self.destination_id,
                                                       screen_manager=self.screen_manager,
                                                       MailColumn=MailColumn,
                                                       MailList=MailList,
                                                       MailBoxWidget=MailBoxWidget,
                                                       MailWidget=MailWidget, **kwargs)
        def AddMail_button(self,MailColumn,MailList,**kwargs):
            return Page.EditContactPage.AddMailButton(user_id=self.user_id,
                                                      destination_id=self.destination_id,
                                                      screen_manager=self.screen_manager,
                                                      MailColumn=MailColumn,
                                                      MailList=MailList,**kwargs)

        def RemoveLink_button(self, LinksColumn, LinksList, LinkBox, LinkStrWidget,LinkURLWidget, **kwargs):
            return Page.EditContactPage.RemoveLinkButton(user_id=self.user_id,
                                                         destination_id=self.destination_id,
                                                         screen_manager=self.screen_manager,
                                                         LinksColumn=LinksColumn,
                                                         LinksList=LinksList,
                                                         LinkBox=LinkBox,
                                                         LinkStrWidget=LinkStrWidget,
                                                         LinkURLWidget=LinkURLWidget,**kwargs)
        def SaveLink_button(self, LinksColumn, LinksList, LinkBox, LinkStrWidget,LinkURLWidget, **kwargs):
            return Page.EditContactPage.SaveLinkButton(user_id=self.user_id,
                                                         destination_id=self.destination_id,
                                                         screen_manager=self.screen_manager,
                                                         LinksColumn=LinksColumn,
                                                         LinksList=LinksList,
                                                         LinkBox=LinkBox,
                                                         LinkStrWidget=LinkStrWidget,
                                                         LinkURLWidget=LinkURLWidget,**kwargs)
        def EditLink_button(self, LinksColumn, LinksList, LinkBox, LinkStrWidget,LinkURLWidget, **kwargs):
            return Page.EditContactPage.EditLinkButton(user_id=self.user_id,
                                                         destination_id=self.destination_id,
                                                         screen_manager=self.screen_manager,
                                                         LinksColumn=LinksColumn,
                                                         LinksList=LinksList,
                                                         LinkBox=LinkBox,
                                                         LinkStrWidget=LinkStrWidget,
                                                         LinkURLWidget=LinkURLWidget,**kwargs)
        def AddLink_button(self, LinksColumn, LinksList, **kwargs):
            return Page.EditContactPage.AddLinkButton(user_id=self.user_id,
                                                         destination_id=self.destination_id,
                                                         screen_manager=self.screen_manager,
                                                         LinksColumn=LinksColumn,
                                                         LinksList=LinksList,
                                                         **kwargs)

    class EditRelationsPage(BoxLayout):
        '''
        This page can add or remove FAmilt member relationship:
        Family Member:x
        Relationship status :x
        '''
        class AddFamilyMemberButton(Button):
            def __init__(self, user_id, destination_id, screen_manager, FamilyColumn, FamilyList, **kwargs):
                super(Page.EditRelationsPage.AddFamilyMemberButton, self).__init__(**kwargs)
                self.user_id = user_id
                self.destination_id = destination_id
                self.screen_manager = screen_manager
                self.FamilyColumn = FamilyColumn
                self.FamilyList = FamilyList
                self.size_hint_y = None
                self.size_hint_x = 1
                self.height = 30
                self.text = 'Add New Family Member'
                self.font_size = 15


            def on_release(self):
                self.FamilyColumn.remove_widget(self)

                index = len(self.FamilyList)
                self.FamilyList.append(BoxLayout(orientation='horizontal', size_hint_y=None,height=50, padding=5, spacing=10))
                self.FamilyList[index].friendnameinput = TextInput( size_hint_x=0.3,
                                                            size_hint_y=None, height=30)
                self.FamilyList[index].add_widget(self.FamilyList[index].friendnameinput)
                self.FamilyList[index].familyrelationinput = TextInput(size_hint_x=0.3,
                                                                   size_hint_y=None, height=30)
                self.FamilyList[index].add_widget(self.FamilyList[index].familyrelationinput)
                self.FamilyList[index].add_widget(Page.EditRelationsPage.SaveFamilyMember_button(self,self.FamilyColumn,
                                                                                self.FamilyList,
                                                                                self.FamilyList[index],
                                                                                self.FamilyList[index].friendnameinput,
                                                                                self.FamilyList[index].familyrelationinput))

                self.FamilyList[index].add_widget(Page.EditRelationsPage.RemoveFamilyMember_button(self, self.FamilyColumn,
                                                                   self.FamilyList,
                                                                   self.FamilyList[index],
                                                                   self.FamilyList[index].friendnameinput,
                                                                   self.FamilyList[index].familyrelationinput))

                self.FamilyColumn.add_widget(self.FamilyList[index])
                self.FamilyColumn.add_widget(Page.EditRelationsPage.AddFamilyMember_button(self,self.FamilyColumn, self.FamilyList))

        class RemoveFamilyMemberButton(Button):
            def __init__(self, user_id, destination_id, screen_manager, FamilyColumn, FamilyList, FamilyRow,
                         friendnameinput, familyrelationinput, **kwargs):
                super(Page.EditRelationsPage.RemoveFamilyMemberButton, self).__init__(**kwargs)
                self.user_id = user_id
                self.destination_id = destination_id
                self.screen_manager = screen_manager
                self.FamilyColumn = FamilyColumn
                self.FamilyList = FamilyList
                self.FamilyRow = FamilyRow
                self.friendnameinput = friendnameinput
                self.familyrelationinput = familyrelationinput
                self.size_hint_y = None
                self.size_hint_x = 0.05
                self.height = 30
                self.text = '-'
                self.font_size = 20

            def on_release(self):
                if self.friendnameinput.text != '' and self.familyrelationinput.text != '':
                    for friend in amber.database[self.user_id].friends:
                        if self.friendnameinput.text == amber.database[friend].name:
                            personal_docks.PersonalDock.remove_family_member_relationship(amber.database[self.user_id],friend)
                            self.FamilyColumn.remove_widget(self.FamilyRow)
                            index = self.FamilyList.index(self.FamilyRow)
                            self.FamilyList.pop(index)
                            break
                else:
                    self.FamilyColumn.remove_widget(self.FamilyRow)
                    index = self.FamilyList.index(self.FamilyRow)
                    self.FamilyList.pop(index)

        class SaveFamilyMemberButton(Button):
            def __init__(self, user_id, destination_id, screen_manager, FamilyColumn, FamilyList, FamilyRow,
                         friendnameinput, familyrelationinput, **kwargs):
                super(Page.EditRelationsPage.SaveFamilyMemberButton, self).__init__(**kwargs)
                self.user_id = user_id
                self.destination_id = destination_id
                self.screen_manager = screen_manager
                self.FamilyColumn = FamilyColumn
                self.FamilyList = FamilyList
                self.FamilyRow = FamilyRow
                self.friendnameinput = friendnameinput
                self.familyrelationinput = familyrelationinput
                self.size_hint_y = None
                self.size_hint_x = 0.05
                self.height = 30
                self.text = 'Save'
                self.font_size = 10

            def on_release(self):
                if self.friendnameinput.text != '' and self.familyrelationinput.text != '':
                    for friend in amber.database[self.user_id].friends:
                        if self.friendnameinput.text == amber.database[friend].name:
                            personal_docks.PersonalDock.add_family_member_relationship(amber.database[self.user_id],friend,
                                                                                       self.familyrelationinput.text)

                            self.FamilyRow.clear_widgets()

                            self.friendnameinput = Button(text=str(self.friendnameinput.text), size_hint_x=0.3,
                                                       size_hint_y=None, height=30)
                            self.familyrelationinput = Button(text=str(self.familyrelationinput.text), size_hint_x=0.3,
                                                       size_hint_y=None, height=30)
                            self.FamilyRow.add_widget(self.friendnameinput)
                            self.FamilyRow.add_widget(self.familyrelationinput)
                            self.FamilyRow.add_widget(Page.EditRelationsPage.EditFamilyMember_button(self, self.FamilyColumn,
                                                                                         self.FamilyList,
                                                                                         self.FamilyRow,
                                                                                         self.friendnameinput,
                                                                                         self.familyrelationinput))
                            self.FamilyRow.add_widget(Page.EditRelationsPage.RemoveFamilyMember_button(self, self.FamilyColumn,
                                                                                           self.FamilyList,
                                                                                           self.FamilyRow,
                                                                                           self.friendnameinput,
                                                                                           self.familyrelationinput))
                            break
        class EditFamilyMemberButton(Button):
            def __init__(self, user_id, destination_id, screen_manager, FamilyColumn, FamilyList, FamilyRow,
                         friendnameinput, familyrelationinput, **kwargs):
                super(Page.EditRelationsPage.EditFamilyMemberButton, self).__init__(**kwargs)
                self.user_id = user_id
                self.destination_id = destination_id
                self.screen_manager = screen_manager
                self.FamilyColumn = FamilyColumn
                self.FamilyList = FamilyList
                self.FamilyRow = FamilyRow
                self.friendnameinput = friendnameinput
                self.familyrelationinput = familyrelationinput
                self.size_hint_y = None
                self.size_hint_x = 0.05
                self.height = 30
                self.text = 'Edit'
                # self.font_size = 20

            def on_release(self):
                if self.friendnameinput.text != '' and self.familyrelationinput.text != '':
                    for friend in amber.database[self.user_id].friends:
                        if self.friendnameinput.text == amber.database[friend].name:
                            personal_docks.PersonalDock.edit_family_member_relationship(amber.database[self.user_id],friend,
                                                                                       self.familyrelationinput.text)
                        self.FamilyRow.clear_widgets()
                        self.friendnameinput = TextInput(text=self.friendnameinput.text,
                                                      size_hint_x=0.3, size_hint_y=None, height=30)
                        self.familyrelationinput = TextInput(text=self.familyrelationinput.text,
                                                      size_hint_x=0.3, size_hint_y=None, height=30)
                        self.FamilyRow.add_widget(self.friendnameinput)
                        self.FamilyRow.add_widget(self.familyrelationinput)
                        self.FamilyRow.add_widget(Page.EditRelationsPage.SaveFamilyMember_button(self, self.FamilyColumn,
                                                                                       self.FamilyList,
                                                                                       self.FamilyRow,
                                                                                     self.friendnameinput,
                                                                                     self.familyrelationinput))
                        self.FamilyRow.add_widget(Page.EditRelationsPage.RemoveFamilyMember_button(self, self.FamilyColumn,
                                                                                       self.FamilyList,
                                                                                       self.FamilyRow,
                                                                                       self.friendnameinput,
                                                                                       self.familyrelationinput))
                        break

        class AddRelationButton(Button):
            def __init__(self, user_id, destination_id, screen_manager, RelationColumn, RelationList, **kwargs):
                super(Page.EditRelationsPage.AddRelationButton, self).__init__(**kwargs)
                self.user_id = user_id
                self.destination_id = destination_id
                self.screen_manager = screen_manager
                self.RelationColumn = RelationColumn
                self.RelationList = RelationList
                self.size_hint_y = None
                self.size_hint_x = 1
                self.height = 30
                self.text = 'Add New RelationShip status'
                self.font_size = 15

            def on_release(self):
                self.RelationColumn.remove_widget(self)

                index = len(self.RelationList)
                self.RelationList.append(BoxLayout(orientation='horizontal', size_hint_y=None,height=50, padding=5, spacing=10))
                self.RelationList[index].significant_other_id = TextInput( size_hint_x=0.4,
                                           size_hint_y=None, height=30)
                self.RelationList[index].add_widget(self.RelationList[index].significant_other_id)
                self.RelationList[index].Relation = TextInput( size_hint_x=0.4,
                                           size_hint_y=None, height=30)
                self.RelationList[index].add_widget(self.RelationList[index].Relation)
                self.RelationList[index].startdateinput = TextInput( size_hint_x=0.1,
                                               size_hint_y=None, height=30)
                self.RelationList[index].add_widget(self.RelationList[index].startdateinput)
                self.RelationList[index].finishdateinput = TextInput( size_hint_x=0.1,
                                               size_hint_y=None, height=30)
                self.RelationList[index].add_widget(self.RelationList[index].finishdateinput)
                self.RelationList[index].add_widget(Page.EditRelationsPage.SaveRelation_button(self,self.RelationColumn,
                                                                                self.RelationList,
                                                                                self.RelationList[index],
                                                                                self.RelationList[index].significant_other_id,
                                                                                self.RelationList[index].Relation,
                                                                                self.RelationList[index].startdateinput,
                                                                                self.RelationList[index].finishdateinput))
                self.RelationList[index].add_widget(Page.EditRelationsPage.RemoveRelation_button(self,self.RelationColumn,
                                                                                  self.RelationList,
                                                                                  self.RelationList[index],
                                                                                  self.RelationList[index].significant_other_id,
                                                                                  self.RelationList[index].Relation))
                self.RelationColumn.add_widget(self.RelationList[index])
                self.RelationColumn.add_widget(Page.EditRelationsPage.AddRelation_button(self,self.RelationColumn, self.RelationList))
        class RemoveRelationButton(Button):
            def __init__(self, user_id, destination_id, screen_manager,RelationColumn,
                         RelationList,RelationRow,significant_other_id,Relation, **kwargs):
                super(Page.EditRelationsPage.RemoveRelationButton, self).__init__(**kwargs)
                self.user_id = user_id
                self.destination_id = destination_id
                self.screen_manager = screen_manager
                self.RelationColumn=RelationColumn
                self.RelationList=RelationList
                self.RelationRow=RelationRow
                self.significant_other_id=significant_other_id
                self.Relation=Relation
                self.size_hint_y = None
                self.size_hint_x = 0.05
                self.height = 30
                self.text = '-'
                self.font_size=50

            def on_release(self):
                if self.significant_other_id.text!='' and self.Relation.text!='':
                    for friend in amber.database[self.user_id].friends:
                        if self.significant_other_id.text == amber.database[friend].name:

                            personal_docks.PersonalDock.remove_relationship(amber.database[self.user_id],friend,
                                                                 self.Relation.text)
                self.RelationColumn.remove_widget(self.RelationRow)
                index = self.RelationList.index(self.RelationRow)
                self.RelationList.pop(index)
        class EditRelationButton(Button):
            def __init__(self, user_id, destination_id, screen_manager,RelationColumn,RelationList,
                         RelationRow,significant_other_id,Relation,startdate,enddate, **kwargs):
                super(Page.EditRelationsPage.EditRelationButton, self).__init__(**kwargs)
                self.user_id = user_id
                self.destination_id = destination_id
                self.screen_manager = screen_manager
                self.RelationColumn = RelationColumn
                self.RelationList = RelationList
                self.RelationRow = RelationRow
                self.significant_other_id = significant_other_id
                self.Relation = Relation
                self.startdate = startdate
                self.enddate = enddate
                self.size_hint_y = None
                self.size_hint_x = 0.05
                self.height = 30
                self.text = 'Edit'
                self.font_size = 15

            def on_release(self):
                # self.eduBoxWidget.remove_widget(self.startdate)
                # self.eduBoxWidget.remove_widget(self.enddate)
                self.RelationRow.clear_widgets()

                self.significant_other_id=Button(text=self.significant_other_id.text,
                                        size_hint_x=0.4, size_hint_y=None, height=30)
                self.Relation=Button(text=self.Relation.text,
                                        size_hint_x=0.4, size_hint_y=None, height=30)
                self.startdate = TextInput(text=self.startdate.text,
                                        size_hint_x=0.1, size_hint_y=None, height=30)
                self.enddate = TextInput(text=self.enddate.text,
                                      size_hint_x=0.1, size_hint_y=None, height=30)
                self.RelationRow.add_widget(self.significant_other_id)
                self.RelationRow.add_widget(self.Relation)
                self.RelationRow.add_widget(self.startdate)
                self.RelationRow.add_widget(self.enddate)
                self.RelationRow.add_widget(Page.EditRelationsPage.SaveRelation_button(self, self.parentwidget,
                                                                             self.RelationList,
                                                                             self.RelationRow,
                                                                             self.significant_other_id,
                                                                             self.Relation,
                                                                             self.startdate,
                                                                             self.enddate))
                self.RelationRow.add_widget(Page.EditRelationsPage.RemoveRelation_button(self, self.parentwidget,
                                                                               self.RelationList,
                                                                               self.RelationRow,
                                                                               self.significant_other_id,
                                                                               self.Relation))
        class SaveRelationButton(Button):
            def __init__(self, user_id, destination_id, screen_manager,RelationColumn,RelationList,
                         RelationRow,significant_other_id,Relation,startdate,enddate, **kwargs):
                super(Page.EditRelationsPage.SaveRelationButton, self).__init__(**kwargs)
                self.user_id = user_id
                self.destination_id = destination_id
                self.screen_manager = screen_manager
                self.RelationColumn=RelationColumn
                self.RelationList=RelationList
                self.RelationRow=RelationRow
                self.significant_other_id=significant_other_id
                self.Relation=Relation
                self.startdate = startdate
                self.enddate = enddate
                self.size_hint_y = None
                self.size_hint_x = 0.05
                self.height = 30
                self.text = 'Save'
                self.font_size=10

            def on_release(self):
                if self.significant_other_id.text!='' and self.Relation.text!='' and self.startdate.text!='' and self.enddate.text !='' :
                    for friend in amber.database[self.user_id].friends:
                        if self.significant_other_id.text == amber.database[friend].name:

                            if not personal_docks.PersonalDock.edit_relationship(amber.database[self.user_id],friend,
                                                                       self.Relation.text,
                                                                       self.startdate.text,
                                                                       self.enddate.text):

                                personal_docks.PersonalDock.add_relationship(amber.database[self.user_id],friend,
                                                                      self.Relation.text,
                                                                      self.startdate.text,
                                                                      self.enddate.text)

                            self.RelationRow.clear_widgets()

                            self.significant_other_id = Button(text=self.significant_other_id.text,
                                                   size_hint_x=0.4, size_hint_y=None, height=30)
                            self.Relation = Button(text=self.Relation.text,
                                                   size_hint_x=0.4, size_hint_y=None, height=30)
                            self.startdate = Button(text=self.startdate.text,
                                                             size_hint_x=0.1, size_hint_y=None, height=30)
                            self.enddate = Button(text=self.enddate.text,
                                                                 size_hint_x=0.1, size_hint_y=None, height=30)
                            self.RelationRow.add_widget(self.significant_other_id)
                            self.RelationRow.add_widget(self.Relation)
                            self.RelationRow.add_widget(self.startdate)
                            self.RelationRow.add_widget(self.enddate)
                            self.RelationRow.add_widget(Page.EditRelationsPage.EditRelation_button(self, self.parentwidget,
                                                                                         self.RelationList,
                                                                                         self.RelationRow,
                                                                                         self.significant_other_id,
                                                                                         self.Relation,
                                                                                         self.startdate,
                                                                                         self.enddate))
                            self.RelationRow.add_widget(Page.EditRelationsPage.RemoveRelation_button(self, self.parentwidget,
                                                                                                    self.RelationList,
                                                                                                    self.RelationRow,
                                                                                                    self.significant_other_id,
                                                                                                    self.Relation))

                            break

        def __init__(self, user_id, destination_id, screen_manager, **kwargs):
            super(Page.EditRelationsPage, self).__init__(**kwargs)
            self.user_id = user_id
            self.destination_id = destination_id
            self.screen_manager = screen_manager
            self.orientation = 'vertical'
            # self.add_widget(Label(text='EditRelationsPage'))
            self.FamilyPart = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint_y=1)
            self.RelationsPart = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint_y=1)
            self.Familyheader = Label(text='Family Members', size_hint_x=1, size_hint_y=1, height=50)
            self.Relationheader = Label(text='Relationships', size_hint_x=1, size_hint_y=1, height=50)

            self.FamilyPart.add_widget(self.Familyheader)
            self.RelationsPart.add_widget(self.Relationheader)

            ###Family Information
            self.FamilyBoxs = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint_y=None)
            self.FamilyList = []
            for Family in amber.database[user_id].family:
                # if index != 0:
                self.FamilyList.append(BoxLayout(orientation='horizontal', size_hint_y=None, padding=5, spacing=10))
            for index, Family in enumerate(self.FamilyList):
                familyid = amber.database[user_id].family[index][0]
                Family.name = Button(text=amber.database[familyid].name, size_hint_x=0.3,
                                     size_hint_y=None, height=30)
                Family.Relation = Button(text=amber.database[user_id].family[index][1], size_hint_x=0.3,
                                         size_hint_y=None, height=30)
                Family.add_widget(Family.name)
                Family.add_widget(Family.Relation)
                Family.add_widget(Page.EditRelationsPage.EditFamilyMember_button(self.FamilyBoxs,
                                                                                 self.FamilyList,
                                                                                 Family,
                                                                                 Family.name,
                                                                                 Family.Relation))
                Family.add_widget(Page.EditRelationsPage.RemoveFamilyMember_button(self.FamilyBoxs,
                                                                                   self.FamilyList,
                                                                                   Family,
                                                                                   Family.name,
                                                                                   Family.Relation))

                self.FamilyBoxs.add_widget(Family)
            self.FamilyBoxs.add_widget(self.AddFamilyMember_button(self.FamilyBoxs, self.FamilyList))
            self.FamilyBoxs.bind(minimum_height=self.FamilyBoxs.setter('height'))
            self.FamilyBoxScrollView = ScrollView(size_hint=(1, None), size=(200, 200))
            self.FamilyBoxScrollView.add_widget(self.FamilyBoxs)
            self.FamilyPart.add_widget(self.FamilyBoxScrollView)
            self.add_widget(self.FamilyPart)

            ###Relations Information
            self.RelationBoxs = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint_y=None)
            self.RelationList = []
            for Relation in amber.database[user_id].relationships:
                # if index != 0:
                self.RelationList.append(BoxLayout(orientation='horizontal', size_hint_y=None, padding=5, spacing=10))
            for index, Relation in enumerate(self.RelationList):
                Relationid = amber.database[user_id].relationships[index][0]
                Relation.name = Button(text=amber.database[Relationid].name, size_hint_x=0.3,
                                       size_hint_y=None, height=30)
                Relation.type = Button(text=amber.database[user_id].relationships[index][1], size_hint_x=0.3,
                                       size_hint_y=None, height=30)
                Relation.startdateinput = Button(text=amber.database[user_id].relationships[index][2], size_hint_x=0.1,
                                                 size_hint_y=None, height=30)
                Relation.finishdateinput = Button(text=amber.database[user_id].relationships[index][3], size_hint_x=0.1,
                                                  size_hint_y=None, height=30)
                Relation.add_widget(Relation.name)
                Relation.add_widget(Relation.type)
                Relation.add_widget(Relation.startdateinput)
                Relation.add_widget(Relation.finishdateinput)
                Relation.add_widget(Page.EditRelationsPage.EditRelation_button(self.RelationBoxs,
                                                                               self.RelationList,
                                                                               Relation,
                                                                               Relation.name,
                                                                               Relation.type,
                                                                               Relation.startdateinput,
                                                                               Relation.finishdateinput))
                Relation.add_widget(Page.EditRelationsPage.RemoveRelation_button(self.RelationBoxs,
                                                                                 self.RelationList,
                                                                                 Relation,
                                                                                 Relation.name,
                                                                                 Relation.type,
                                                                                 Relation.startdateinput,
                                                                                 Relation.finishdateinput))

                self.RelationBoxs.add_widget(Relation)
            self.RelationBoxs.add_widget(self.AddRelation_button(self.RelationBoxs, self.RelationList))
            self.RelationBoxs.bind(minimum_height=self.RelationBoxs.setter('height'))
            self.RelationBoxScrollView = ScrollView(size_hint=(1, None), size=(200, 200))
            self.RelationBoxScrollView.add_widget(self.RelationBoxs)
            self.RelationsPart.add_widget(self.RelationBoxScrollView)
            self.add_widget(self.RelationsPart)



        def AddFamilyMember_button(self,FamilyColumn,FamilyList,**kwargs):
            return Page.EditRelationsPage.AddFamilyMemberButton(user_id=self.user_id ,
                                                                destination_id=self.destination_id,
                                                                screen_manager=self.screen_manager,
                                                                FamilyColumn=FamilyColumn,
                                                                FamilyList=FamilyList, ** kwargs)
        def RemoveFamilyMember_button(self,FamilyColumn,FamilyList,FamilyRow,friendnameinput,familyrelationinput, **kwargs):
            return Page.EditRelationsPage.RemoveFamilyMemberButton(user_id=self.user_id,
                                                                 destination_id=self.destination_id,
                                                                 screen_manager=self.screen_manager,
                                                                 FamilyColumn=FamilyColumn,
                                                                 FamilyList=FamilyList,
                                                                 FamilyRow=FamilyRow,
                                                                 friendnameinput=friendnameinput,
                                                                 familyrelationinput=familyrelationinput, **kwargs)
        def EditFamilyMember_button(self, FamilyColumn,FamilyList,FamilyRow,friendnameinput,familyrelationinput, **kwargs):
            return Page.EditRelationsPage.EditFamilyMemberButton(user_id=self.user_id,
                                                                 destination_id=self.destination_id,
                                                                 screen_manager=self.screen_manager,
                                                                 FamilyColumn=FamilyColumn,
                                                                 FamilyList=FamilyList,
                                                                 FamilyRow=FamilyRow,
                                                                 friendnameinput=friendnameinput,
                                                                 familyrelationinput=familyrelationinput, **kwargs)
        def SaveFamilyMember_button(self, FamilyColumn,FamilyList,FamilyRow,friendnameinput,familyrelationinput, **kwargs):
            return Page.EditRelationsPage.SaveFamilyMemberButton(user_id=self.user_id,
                                                            destination_id=self.destination_id,
                                                            screen_manager=self.screen_manager,
                                                                 FamilyColumn=FamilyColumn,
                                                                 FamilyList=FamilyList,
                                                                 FamilyRow=FamilyRow,
                                                                 friendnameinput=friendnameinput,
                                                                familyrelationinput=familyrelationinput,**kwargs)


        def AddRelation_button(self,RelationColumn,RelationList, **kwargs):
            return Page.EditRelationsPage.AddRelationButton(user_id=self.user_id,
                                                            destination_id=self.destination_id,
                                                            screen_manager=self.screen_manager,
                                                            RelationColumn=RelationColumn,
                                                            RelationList=RelationList, **kwargs)
        def RemoveRelation_button(self,RelationColumn,RelationList,RelationRow,significant_other_id,Relation, **kwargs):
            return Page.EditRelationsPage.RemoveRelationButton(user_id=self.user_id,
                                                                 destination_id=self.destination_id,
                                                                 screen_manager=self.screen_manager,
                                                                 RelationColumn=RelationColumn,
                                                                 RelationList=RelationList,
                                                                 RelationRow=RelationRow,
                                                                 significant_other_id=significant_other_id,
                                                                 Relation=Relation, **kwargs)
        def EditRelation_button(self,RelationColumn,RelationList,RelationRow,significant_other_id,Relation,startdate,enddate, **kwargs):
            return Page.EditRelationsPage.EditRelationButton(user_id=self.user_id,
                                                                 destination_id=self.destination_id,
                                                                 screen_manager=self.screen_manager,
                                                                 RelationColumn=RelationColumn,
                                                                 RelationList=RelationList,
                                                                 RelationRow=RelationRow,
                                                                 significant_other_id=significant_other_id,
                                                                 Relation=Relation,
                                                                 startdate=startdate,
                                                                 enddate=enddate, **kwargs)
        def SaveRelation_button(self,RelationColumn,RelationList,RelationRow,significant_other_id,Relation,startdate,enddate, **kwargs):
            return Page.EditRelationsPage.SaveRelationButton(user_id=self.user_id,
                                                                 destination_id=self.destination_id,
                                                                 screen_manager=self.screen_manager,
                                                                 RelationColumn=RelationColumn,
                                                                 RelationList=RelationList,
                                                                 RelationRow=RelationRow,
                                                                 significant_other_id=significant_other_id,
                                                                 Relation=Relation,
                                                                 startdate=startdate,
                                                                 enddate=enddate, **kwargs)

    class FriendsPage(BoxLayout):
        '''
        this Page can show Freinds Names and Remove Friends

        '''

        class RemoveFriendButton(Button):
            def __init__(self,user_id, destination_id, screen_manager,FriendTable,FriendRow,FriendnameWidget,FriendID,**kwargs):
                super(Page.FriendsPage.RemoveFriendButton, self).__init__(**kwargs)
                self.user_id = user_id
                self.destination_id = destination_id
                self.screen_manager = screen_manager
                self.FriendTable=FriendTable
                self.FriendRow = FriendRow
                self.FriendnameWidget = FriendnameWidget
                self.FriendID=FriendID
                self.size_hint_y = None
                self.size_hint_x = 0.2
                self.height = 30
                self.text = 'Unfriend'
                self.font_size = 20
            def on_release(self):
                # friendid=self.FriendnameWidget.id
                personal_docks.PersonalDock.remove_friend(amber.database[self.user_id],self.FriendID)
                self.FriendTable.remove_widget(self.FriendRow)

        def __init__(self, user_id, destination_id, screen_manager, **kwargs):
            super(Page.FriendsPage, self).__init__(**kwargs)
            self.user_id = user_id
            self.destination_id = destination_id
            self.screen_manager = screen_manager
            self.orientation = 'vertical'
            self.add_widget(Label(text='Friends'))
            self.FriendTable = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint_y=None)
            self.FriendList = []
            for friend in amber.database[user_id].friends:
                self.FriendList.append(BoxLayout(orientation='horizontal', size_hint_y=None, padding=5, spacing=10))
            for index, friend in enumerate(self.FriendList):
                friendid =amber.database[user_id].friends[index]
                friend.friendwidget = Button(text=amber.database[friendid].name,
                                           id=amber.database[user_id].friends[index], size_hint_x=0.3,
                                           size_hint_y=None, height=30)
                friend.add_widget(friend.friendwidget)
                friend.add_widget(
                self.RemoveFriend_button(self.FriendTable, self.FriendList, friend,friend.friendwidget,friendid))

                self.FriendTable.add_widget(friend)
            self.FriendTable.bind(minimum_height=self.FriendTable.setter('height'))
            self.FriendTableScrollView = ScrollView(size_hint=(1, None), size=(200, 450))
            self.FriendTableScrollView.add_widget(self.FriendTable)
            self.add_widget(self.FriendTableScrollView)

        def RemoveFriend_button(self, FriendTable, FriendRow, FriendnameWidget,FriendID, **kwargs):
             return Page.FriendsPage.RemoveFriendButton(self, user_id=self.user_id,
                                                        destination_id=self.destination_id,
                                                        screen_manager=self.screen_manager,
                                                        FriendTable=FriendTable, FriendRow=FriendRow,
                                                        FriendnameWidget=FriendnameWidget,
                                                        FriendID=FriendID,**kwargs)

    class FollowersPage(BoxLayout):

        class RemoveFollowerButton(Button):
            def __init__(self,user_id, destination_id, screen_manager,FollowerTable,FollowerRow,FollowernameWidget,FollowerID,**kwargs):
                super(Page.FollowersPage.RemoveFollowerButton, self).__init__(**kwargs)
                self.user_id = user_id
                self.destination_id = destination_id
                self.screen_manager = screen_manager
                self.FollowerTable=FollowerTable
                self.FollowerRow = FollowerRow
                self.FollowernameWidget = FollowernameWidget
                self.FollowerID=FollowerID
                self.size_hint_y = None
                self.size_hint_x = 0.2
                self.height = 30
                self.text = 'UnFollow'
                self.font_size = 20
            def on_release(self):
                # Followerid=self.FollowernameWidget.id
                personal_docks.PersonalDock.remove_Follower(amber.database[self.user_id],self.FollowerID)
                self.FollowerTable.remove_widget(self.FollowerRow)


        def __init__(self, user_id, destination_id, screen_manager, **kwargs):
            super(Page.FollowersPage, self).__init__(**kwargs)
            self.user_id = user_id
            self.destination_id = destination_id
            self.screen_manager = screen_manager
            self.orientation = 'vertical'
            self.add_widget(Label(text='FollowersPage'))
            self.FollowerTable = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint_y=None)
            self.FollowerList = []
            for Follower in amber.database[user_id].followers:
                self.FollowerList.append(BoxLayout(orientation='horizontal', size_hint_y=None, padding=5, spacing=10))
            for index, Follower in enumerate(self.FollowerList):
                Followerid = amber.database[user_id].followers[index]
                Follower.Followerwidget = Button(text=amber.database[Followerid].name,
                                             id=amber.database[user_id].followers[index], size_hint_x=0.3,
                                             size_hint_y=None, height=30)
                Follower.add_widget(Follower.Followerwidget)
                Follower.add_widget(
                    self.RemoveFollower_button(self.FollowerTable, self.FollowerList, Follower, Follower.Followerwidget,
                                             Followerid))
                self.FollowerTable.add_widget(Follower)
            self.FollowerTable.bind(minimum_height=self.FollowerTable.setter('height'))
            self.FollowerTableScrollView = ScrollView(size_hint=(1, None), size=(200, 450))
            self.FollowerTableScrollView.add_widget(self.FollowerTable)
            self.add_widget(self.FollowerTableScrollView)

        def RemoveFollower_button(self, FollowerTable, FollowerRow, FollowernameWidget, FollowerID, **kwargs):
            return Page.FollowersPage.RemoveFollowerButton(self, user_id=self.user_id,
                                                       destination_id=self.destination_id,
                                                       screen_manager=self.screen_manager,
                                                       FollowerTable=FollowerTable, FollowerRow=FollowerRow,
                                                       FollowernameWidget=FollowernameWidget,
                                                       FollowerID=FollowerID, **kwargs)

    class FolloweesPage(BoxLayout):

        class RemoveFolloweeButton(Button):
            def __init__(self,user_id, destination_id, screen_manager,FolloweeTable,FolloweeRow,FolloweenameWidget,FolloweeID,**kwargs):
                super(Page.FolloweesPage.RemoveFolloweeButton, self).__init__(**kwargs)
                self.user_id = user_id
                self.destination_id = destination_id
                self.screen_manager = screen_manager
                self.FolloweeTable=FolloweeTable
                self.FolloweeRow = FolloweeRow
                self.FolloweenameWidget = FolloweenameWidget
                self.FolloweeID=FolloweeID
                self.size_hint_y = None
                self.size_hint_x = 0.2
                self.height = 30
                self.text = 'UnFollow'
                self.font_size = 20
            def on_release(self):
                # Followeeid=self.FolloweenameWidget.id
                personal_docks.PersonalDock.remove_Followee(amber.database[self.user_id],self.FolloweeID)
                self.FolloweeTable.remove_widget(self.FolloweeRow)


        def __init__(self, user_id, destination_id, screen_manager, **kwargs):
            super(Page.FolloweesPage, self).__init__(**kwargs)
            self.user_id = user_id
            self.destination_id = destination_id
            self.screen_manager = screen_manager
            self.orientation = 'vertical'
            self.add_widget(Label(text='FolloweesPage'))
            self.FolloweeTable = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint_y=None)
            self.FolloweeList = []
            for Followee in amber.database[user_id].followees:
                self.FolloweeList.append(BoxLayout(orientation='horizontal', size_hint_y=None, padding=5, spacing=10))
            for index, Followee in enumerate(self.FolloweeList):
                Followeeid = amber.database[user_id].followees[index]
                Followee.Followeewidget = Button(text=amber.database[Followeeid].name,
                                             id=amber.database[user_id].followees[index], size_hint_x=0.3,
                                             size_hint_y=None, height=30)
                Followee.add_widget(Followee.Followeewidget)
                Followee.add_widget(
                    self.RemoveFollowee_button(self.FolloweeTable, self.FolloweeList, Followee, Followee.Followeewidget,
                                             Followeeid))
                self.FolloweeTable.add_widget(Followee)
            self.FolloweeTable.bind(minimum_height=self.FolloweeTable.setter('height'))
            self.FolloweeTableScrollView = ScrollView(size_hint=(1, None), size=(200, 450))
            self.FolloweeTableScrollView.add_widget(self.FolloweeTable)
            self.add_widget(self.FolloweeTableScrollView)

        def RemoveFollowee_button(self, FolloweeTable, FolloweeRow, FolloweenameWidget, FolloweeID, **kwargs):
            return Page.FolloweesPage.RemoveFolloweeButton(self, user_id=self.user_id,
                                                       destination_id=self.destination_id,
                                                       screen_manager=self.screen_manager,
                                                       FolloweeTable=FolloweeTable, FolloweeRow=FolloweeRow,
                                                       FolloweenameWidget=FolloweenameWidget,
                                                       FolloweeID=FolloweeID, **kwargs)

    def __init__(self, users_manager, user_id, **kwargs):
        super(Page, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 5
        self.top_bar = BoxLayout(size_hint_y=1, orientation='horizontal', padding=10, spacing=5)
        self.content = Page.ContentManager(size_hint_y=9, user_id=user_id)
        self.content.home_button().on_release()

        self.top_bar.add_widget(self.content.back_button(text="Back"))
        self.top_bar.add_widget(self.content.home_button(text="Home"))
        self.top_bar.add_widget(
            self.content.profile_button(destination_id=user_id, text=amber.database[user_id].name))
        self.top_bar.add_widget(self.content.group_creation_button())
        self.top_bar.add_widget(Page.ContentManager.BackButton(size_hint_x=0.3, screen_manager=users_manager,
                                                               text='Logout',
                                                               background_color=(1.0, 0.0, 0.0, 1.0)))
        self.add_widget(self.top_bar)
        self.add_widget(self.content)

    class SearchButton(Button):

        def __init__(self, search_tb, screen_manager, **kwargs):
            super().__init__(**kwargs)
            self.search_tb = search_tb
            self.screen_manager = screen_manager
            self.text = 'Search'

        def on_release(self):
            if '@' in self.search_tb.text:
                for dock_id in amber.generate_personal_docks():
                    if amber.database[dock_id].master_email == self.search_tb.text:
                        self.screen_manager.profile_button(destination_id=dock_id).on_release()
            else:
                for sea_id in amber.generate_seas():
                    if amber.database[sea_id].name == self.search_tb.text:
                        self.screen_manager.group_button(group_id=sea_id).on_release()

    def __init__(self, users_manager, user_id, **kwargs):
        super(Page, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 5
        self.top_bar = BoxLayout(size_hint_y=1, orientation='horizontal', padding=10, spacing=5)
        self.content = Page.ContentManager(size_hint_y=9, user_id=user_id)
        self.content.home_button().on_release()

        self.top_bar.add_widget(self.content.back_button(text="Back"))
        self.search_tb = TextInput(size_hint_x=2, multiline=False)
        self.top_bar.add_widget(self.search_tb)
        self.top_bar.add_widget(Page.SearchButton(search_tb=self.search_tb, screen_manager=self.content))
        self.top_bar.add_widget(self.content.home_button(text="Home"))
        self.top_bar.add_widget(self.content.profile_button(destination_id=user_id, text=amber.database[user_id].name))
        self.top_bar.add_widget(self.content.group_creation_button(halign="center"))
        self.top_bar.add_widget(Page.ContentManager.BackButton(halign="center", size_hint_x=0.3, screen_manager=users_manager,
                                                               text='Log\nout', background_color=(1.0, 0.0, 0.0, 1.0)))
        self.add_widget(self.top_bar)
        self.add_widget(self.content)

################### Screen Manager ######################
users_manager = ScreenManager(transition=SwapTransition())
users_manager.add_widget(RegisterationScreen(name='Registeration'))
login = Screen(name='login')
login.add_widget(LoginScreen(users_manager=users_manager))
users_manager.add_widget(login)

users_manager.current='login'

######################### Main App
class AmberOcean(App):

  """
  Test App
  """

  def __init__(self, user_id, **kwargs):
    super(AmberOcean, self).__init__(**kwargs)
    self.user_id = user_id

  def build(self):




      #users_manager.current = users_manager.next()

      return users_manager

  def on_pause(self):
    return True

if __name__ == "__main__":
    amber.import_database()
    try:
        AmberOcean(user_id=user_id_for_login).run()
    except:
        import sys
        print(sys.exc_info())
    amber.export_database()
