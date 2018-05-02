import amber
import personal_docks
import seas
import ships
import time
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty, StringProperty,NumericProperty
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
from kivy.uix.screenmanager import *
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.widget import *
from kivy.uix.popup import *
from kivy.clock import *
from amber import *
Builder.load_file("frontend.kv")

user_id_for_login = ""
                
returned_id=""

number_comments = ""
def comment_clicked (cmt_btn):
        txt_splitted = number_comments.text.split()
        number_comments.text = str(int(txt_splitted[0]) + 1) + ' ' + txt_splitted[1]
#function to calculate number of likes
number_likes = ""
number_haha = ""
number_sad= ""
number_love= ""
number_dislike = ""
number_angry = ""



###################  Login 
class LoginScreen(BoxLayout):
    # define the constructor and access the class method and attributes
    def __init__(self, users_manager, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        #**kwargs allow you to pass a variable number of arguments to a function.
        self.users_manager = users_manager
        # BaxLayout Orientation is vertical
        self.orientation = 'vertical'

class Login(Widget):
    def submit_login(self):
        global user_id_for_login
        # save textinput to a variables
        logname = self.login_name.text
        logpass= self.login_password.text
        # test only
        #if logname == 'admin' and logpass == 'admin':
        #users_manager.current = 'home'
        for key, value in database.items():
                if value.master_email == logname:
                        if value.check_password(logpass):
                                        user_id_for_login = key
                                        users_manager.current = 'home'
                        else :
                                popup = Popup(title='Test popup',
                                content=Label(text='Wrong username or password'),
                                size_hint=(None, None), size=self.size)
                                popup.open()

###################  Registeration
class Registeration(Widget):
         global returned_id
         gender = StringProperty(None)
         date = StringProperty(None)
         def ismale(self):
                gender = "male"# print (gender)
         def isfemale(self):
                gender = "female" # print (gender)

         def registerAccount(self):
             # check input data
                    if self.name.text == "":
                        l=Label(text='Please enter Your Name',color=(1,0,0,1),markup=True)
                        self.ids.error.add_widget(l)
                        Clock.schedule_once(lambda dt: self.ids.error.remove_widget(l), 1)
                    elif not self.year.text.isdigit() or not self.month.text.isdigit() or not  self.day.text.isdigit():
                        l=Label(text='Please enter a valid Birthday',color=(1,0,0,1),markup=True)
                        self.ids.error.add_widget(l)
                        Clock.schedule_once(lambda dt: self.ids.error.remove_widget(l), 1)
                    elif self.year.text.isdigit() and self.month.text.isdigit() and  self.day.text.isdigit():
                         if  int(self.day.text) > 31 or int(self.day.text) < 0:
                            l=Label(text='Please enter a valid Birth Day',color=(1,0,0,1),markup=True)
                            self.ids.error.add_widget(l)
                            Clock.schedule_once(lambda dt: self.ids.error.remove_widget(l), 1)
                         elif  int(self.month.text) > 12 or int(self.day.text) < 0 :
                            l=Label(text='Please enter a valid Birth Month',color=(1,0,0,1),markup=True)
                            self.ids.error.add_widget(l)
                            Clock.schedule_once(lambda dt: self.ids.error.remove_widget(l), 1)
                         elif  int(self.year.text) > 2018 or int(self.year.text) < 1900:
                            l=Label(text='Please enter a valid Birth Year',color=(1,0,0,1),markup=True)
                            self.ids.error.add_widget(l)
                            Clock.schedule_once(lambda dt: self.ids.error.remove_widget(l), 1)
                         elif not '@' in self.email.text or self.email.text==""  :
                            l=Label(text='Please enter a valid email',color=(1,0,0,1),markup=True)
                            self.ids.error.add_widget(l)
                            Clock.schedule_once(lambda dt: self.ids.error.remove_widget(l), 1)
                         elif self.password.text=="" :
                            l=Label(text='Please enter your Password',color=(1,0,0,1),markup=True)
                            self.ids.error.add_widget(l)
                            Clock.schedule_once(lambda dt: self.ids.error.remove_widget(l), 1)
                         else:
                            date = datetime.datetime(int(self.year.text), int(self.month.text), int(self.day.text))
                #check valid date
                    
                    #else:
                            #popup = Popup(title='Test popup',
                            #content=Label(text='Please enter a valid Birthday'),
                            #size_hint=(None, None), size=self.size)
                            #popup.open()
                #print(self.password.text+" "+self.email.text+" "+self.phone.text)
                #  if self.name.text == "" or self.gender==""or date==""or self.password.text=="" or self.email.text == "" or self.phone.text== "" :
                #         # label = Label(text='Please Write Your Name',color=(0,0,0,1))
                                    #self.ids.error.add_widget(label)
                    else:
                                returned_id = personal_docks.PersonalDock.RegisterAccount(self.name.text,self.gender,date,self.password.text,
                                                                             self.email.text,self.phone.text)
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
                                self.text = 'Create a new sea'
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
                  ##### Groups
                  group_number = len(list(user.seas))
                  group_label = Label(text='Groups',color=(0,0,0,1))
                  self.ids.groups_l.add_widget(group_label)
                  for i in range(group_number):
                            button = Button(text="Group " + i[0],background_color=(0,0, 1, 0.6),size_hint_y= None,height= 30)
                            self.ids.groups.add_widget(button)
            
                   ## Friends
                  friend_number =len(list(user.friends))
                  Friends_label = Label(text='Freinds',color=(0,0,0,1),size_hint_y=10)
                  self.ids.friends_l.add_widget(Friends_label)
                  for i in range(friend_number):
                                button = Button(text="Friend " + i[0],background_color=(0,1, 0, 0.6),height= 30)
                                self.ids.friends.add_widget(button)
                  ##### Followees
                  Followee_number = len(list(user.followees))
                  Followess_label = Label(text='Followees',color=(0,0,0,1))
                  self.ids.followees.add_widget(Followess_label)
                  for i in range(friend_number):
                                button = Button(text="Followee " + i[0],background_color=(1,0, 0, 0.6))
                                self.ids.followees.add_widget(button)

                  ##### Ships
                  Ships_number = len(list(user.newsfeed_ships()))
                  Ships_label = Label(text='Ships',color=(0,0,0,1))
                  self.ids.ships.add_widget(Ships_label)
                  for i in range(Ships_number):
                                button = Button(text="Ship " + i[0],background_color=(0,1, 1, 0.6),height= 30)
                                self.ids.ships.add_widget(button)
                  ##### Suugested Friends
                  sugg_friend_number=len(list(user.docks_you_may_know()))
                  sugg_friend_label = Label(text='Suggested Friends',color=(0,0,0,1))
                  self.ids.sugg_friend.add_widget(sugg_friend_label)
                  
                  for i in range(sugg_friend_number):
                                button = Button(text="Friend " + i[0],background_color=(1,1, 0, 0.6),height= 30)
                                self.ids.sugg_friend.add_widget(button)
                        ####
                        #sugg_groups_number=len(list(user.seas_you_might_join()))
                  #sugg_group_label = Label(text='Suggested Groups',color=(0,0,0,1))
            #self.ids.sugg_group.add_widget(sugg_group_label)
            #for i in range(sugg_groups_number):
              #button = Button(text="Group " + i[0],background_color=(1,0, 1, 0.6),height= 30)
              #self.ids.sugg_group.add_widget(button)


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

                        if is_able_to_see:
                                self.orientation = 'vertical'
                                self.spacing = 10
                                self.padding = 20
                                self.size_hint = (1, None)
                                self.height = 600

                                Header = BoxLayout(orientation='vertical', spacing=0, padding=20, size_hint=(1, 1))
                                Delete = BoxLayout(orientation='horizontal', size_hint=(1, 1), spacing=0, padding=20)
                                Center = BoxLayout(orientation='vertical', spacing=10, padding=20, size_hint=(1, 1))
                                Footer = BoxLayout(orientation='horizontal', spacing=10, padding=20, size_hint=(1, 1))
                                Likes = BoxLayout(orientation='horizontal', spacing=10, padding=10, size_hint=(1, 1))
                                Comments = BoxLayout(orientation='vertical', spacing=10, padding=10, size_hint=(1, 1))

                                self.add_widget(Delete)
                                self.add_widget(Header)
                                self.add_widget(Center)
                                Footer.add_widget(Likes)
                                Footer.add_widget(Comments)
                                self.add_widget(Footer)

                                # Button for user name
                                name = Button(text=amber.database[amber.database[self.ship_id].creator_id].name,
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
                                        except:
                                                pass

                                delete = Button(text=" Remove this ship ", size_hint=(1, 1),
                                                                on_release=delete_ship)
                                Delete.add_widget(delete)

                                def like_clicked(like_btn, touch):
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
                                        elif (like_btn.text is "None"):
                                                try:
                                                        amber.database[ship_id].remove_reaction(user_id)
                                                except:
                                                        pass
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
                                        values=("Like", "Haha", "Love", "Dislike", "Angry", "None"),
                                        size_hint=(0, 1)
                                )
                                like.bind(text=like_clicked)
                                Likes.add_widget(like)

                                # Label for editing number of likes
                                global number_likes
                                number_likes = Label(
                                        text="0 likes",
                                        size_hint=(0, 1)
                                )
                                global number_haha
                                number_haha = Label(
                                        text="",
                                        size_hint=(0, 1)
                                )
                                global number_love
                                number_love = Label(
                                        text="",
                                        size_hint=(0, 1)
                                )
                                global number_dislike
                                number_dislike = Label(
                                        text="",
                                        size_hint=(0, 1)
                                )

                                global number_angry
                                number_angry = Label(
                                        text="",
                                        size_hint=(0, 1)
                                )
                                Likes.add_widget(number_likes)
                                Likes.add_widget(number_haha)
                                Likes.add_widget(number_love)
                                Likes.add_widget(number_dislike)
                                Likes.add_widget(number_angry)

                                vert_scr = ScrollView(size_hint=(1, None), height=120)
                                comments_box = BoxLayout(orientation='vertical', size_hint_y=None)
                                comments_box.bind(minimum_height=comments_box.setter('height'))
                                vert_scr.add_widget(comments_box)
                                self.add_widget(vert_scr)

                                def add_comment(comment_btn):

                                        def on_text(instance, touch):
                                                if (not new_post.text == ""):
                                                        post.disabled = False

                                        box_l = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
                                        new_post = TextInput(size_hint_y=None, height=40, on_touch_up=on_text)

                                        def increase_likes(instance, touch):
                                                if "Like" in instance.text:
                                                        instance.values[0] = "Like: " + str(int(instance.values[0].split()[1]) + 1)
                                                elif "Love" in instance.text:
                                                        instance.values[2] = "Love: " + str(int(instance.values[0].split()[1]) + 1)
                                                elif "Haha" in instance.text:
                                                        instance.values[1] = "Haha: " + str(int(instance.values[0].split()[1]) + 1)
                                                elif "Dislike" in instance.text:
                                                        instance.values[3] = "Dislike: " + str(int(instance.values[0].split()[1]) + 1)
                                                elif "None" in instance.text:
                                                        instance.values[5] = "None: " + str(int(instance.values[0].split()[1]) + 1)
                                                elif "Angry" in instance.text:
                                                        instance.values[4] = "Angry: " + str(int(instance.values[0].split()[1]) + 1)

                                        def create_comment(post_btn):

                                                comment_btn.disabled = False
                                                written_text = new_post.text
                                                new_label = Label(text=written_text, size_hint_y=None, height=40)
                                                name_btn = Button(text=amber.database[user_id].name,
                                                                                    size_hint_x=0.2, size_hint_y=None, height=30, bold=True)
                                                like_cmt_btn = Spinner(text="Reactions",
                                                                                             values=(
                                                                                             "Like: 0", "Haha: 0", "Love: 0", "Dislike: 0", "Sad: 0", "Angry: 0"),
                                                                                             size_hint_y=None, height=30, size_hint_x=0.2)
                                                """
                                                reply_btn = Button(text="Reply",size_hint_y=None, height=30,
                                                                                         size_hint_x=0.2 )
                                                """
                                                like_cmt_btn.bind(text=increase_likes)

                                                box_l.remove_widget(new_post)
                                                box_l.remove_widget(post_btn)
                                                new_commen_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
                                                new_commen_box.add_widget(name_btn)
                                                new_commen_box.add_widget(new_label)
                                                new_commen_box.add_widget(like_cmt_btn)
                                                # new_commen_box.add_widget(reply_btn)
                                                comments_box.add_widget(new_commen_box)
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
                                global number_comments
                                number_comments = Label(
                                        text="0 Comments",
                                        # color=(0, 0, 0, 1),
                                        size_hint=(0, 1),
                                        pos_hint={'center_x': 0.9, 'center_y': 1}
                                )
                                Comments.add_widget(number_comments)

                                # After writing post
                                text_input = Label(
                                        text=amber.database[ship_id].txt_content,
                                        size_hint=(1, 2),
                                )
                                Center.add_widget(text_input)
                        else:
                                self.add_widget(Label(size_hint=(0, 0), size=(0, 0)))

        class ProfilePage(BoxLayout):

                def __init__(self, user_id, destination_id, screen_manager, **kwargs):
                        super(Page.ProfilePage, self).__init__(**kwargs)
                        self.user_id = user_id
                        self.destination_id = destination_id
                        self.screen_manager = screen_manager
                        self.add_widget(Label(text='Profile'))

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
                self.top_bar.add_widget(self.content.profile_button(destination_id=user_id, text=amber.database[user_id].name))
                self.top_bar.add_widget(self.content.group_creation_button())
                self.top_bar.add_widget(Page.ContentManager.BackButton(size_hint_x=0.3, screen_manager=users_manager,
                                                                                                                             text='Logout', background_color=(1.0, 0.0, 0.0, 1.0)))
                self.add_widget(self.top_bar)
                self.add_widget(self.content)


################### Screen Manager ######################
users_manager = ScreenManager(transition=SwapTransition())

login = Screen(name='login')
login.add_widget(LoginScreen(users_manager=users_manager))
users_manager.add_widget(login)

home = Screen(name='home')
users_manager.add_widget(home)

users_manager.add_widget(RegisterationScreen(name='Registeration'))
######################### Main App
class AmberOcean(App):

    """
    Test App
    """

    def __init__(self, user_id, **kwargs):
        super(AmberOcean, self).__init__(**kwargs)
        self.user_id = user_id

    def build(self):
        home.add_widget(Page(users_manager=users_manager, user_id=self.user_id))

        #users_manager.current = users_manager.next()

        return users_manager

    def on_pause(self):
        return True


if __name__ == "__main__":
    import datetime
    boula = personal_docks.PersonalDock.RegisterAccount(name="Boula", gender=personal_docks.Gender.Male,
                                                        birthday=datetime.datetime(1996, 9, 28),
                                                        password="123", email='email@yahoo.com',
                                                        phone_number='01222222222')
    AmberOcean(user_id=boula).run()
